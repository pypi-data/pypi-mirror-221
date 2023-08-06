import os
import shutil
import tempfile
import warnings
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import parse_obj_as

from fiddler import ModelInfo
from fiddler.constants import MULTI_PART_CHUNK_SIZE
from fiddler.core_objects import ModelInputType, ModelTask
from fiddler.libs.http_client import RequestClient
from fiddler.schemas.model_schema import ModelSchema
from fiddler.schemas.model_spec import ModelSpec
from fiddler.schemas.model_task_params import ModelTaskParams
from fiddler.schemas.xai_params import XaiParams
from fiddler.utils.logger import get_logger
from fiddler.v2.api.model_artifact_deploy import (
    ModelArtifactDeployer,
    MultiPartModelArtifactDeployer,
)
from fiddler.v2.schema.model import Model
from fiddler.v2.schema.model_deployment import ArtifactType, DeploymentParams
from fiddler.v2.utils.compatibility_helpers import (
    project_id_compat,
    model_id_compat,
    dataset_id_compat,
    is_sync_id_compat,
    model_dir_compat,
)
from fiddler.v2.utils.decorators import check_version, handle_api_error_response
from fiddler.v2.utils.helpers import get_model_artifact_info, read_model_yaml
from fiddler.v2.utils.response_handler import (
    APIResponseHandler,
    PaginatedResponseHandler,
)
from fiddler.v2.utils.validations import validate_artifact_dir

logger = get_logger(__name__)


class ModelMixin:
    ADD_SURROGATE_MODEL_API_VERSION = '>=22.12.0'
    ADD_MODEL_ARTIFACT_API_VERSION = '>=22.12.0'
    DELETE_MODEL_API_VERSION = '>=22.12.0'

    client: RequestClient
    organization_name: str

    @handle_api_error_response
    def get_models(self, project_name: str) -> List[Model]:
        """
        Get list of all models belonging to a project

        :params project_name: The project for which you want to get the models
        :returns: List containing Model objects
        """
        response = self.client.get(
            url='models',
            params={
                'organization_name': self.organization_name,
                'project_name': project_name,
            },
        )
        items = PaginatedResponseHandler(response).get_pagination_items()
        return parse_obj_as(List[Model], items)

    @handle_api_error_response
    def get_model_names(self, project_name: str) -> List[str]:
        """List the ids of all models in the project.

        :param project_name: The unique identifier of the project on Fiddler
        :returns: List of strings containing the ids of each model.
        """
        models = self.get_models(project_name=project_name)
        return [m.name for m in models]

    @handle_api_error_response
    def get_model(self, project_name: str, model_name: str) -> Model:
        """
        Get the details of a model.

        :params project_name: The project to which the model belongs to
        :params model_name: The model name of which you need the details
        :returns: Model object which contains the details
        """
        response = self.client.get(
            url=f'models/{self.organization_name}:{project_name}:{model_name}',
        )
        response_handler = APIResponseHandler(response)
        return Model.deserialize(response_handler)

    def get_model_info(
        self,
        project_id: str = None,
        model_id: str = None,
        project_name: str = None,
        model_name: str = None,
    ) -> ModelInfo:
        """Get ModelInfo for a model.

        :params project_id: The project to which the model belongs to
        :params model_id: The model name of which you need the details
        :params project_name: The project to which the model belongs to
        :params model_name: The model name of which you need the details

        :returns: A fiddler.ModelInfo object describing the model.
        """
        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )
        model_name = model_id_compat(
            model_id=model_id,
            model_name=model_name,
        )
        model_info_dict = self.get_model(
            project_name=project_name, model_name=model_name
        ).info
        return ModelInfo.from_dict(model_info_dict)

    @handle_api_error_response
    def add_model(  # noqa: C901
        self,
        project_id: str = None,
        model_id: str = None,
        dataset_id: str = None,
        model_info: Optional[ModelInfo] = None,
        is_sync: Optional[bool] = True,
        task: Optional[ModelTask] = None,
        input_type: Optional[ModelInputType] = None,
        schema: Optional[ModelSchema] = None,
        spec: Optional[ModelSpec] = None,
        task_params: Optional[ModelTaskParams] = None,
        xai_params: Optional[XaiParams] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        algorithm: Optional[str] = None,
        framework: Optional[str] = None,
        event_id_col: Optional[str] = None,
        event_ts_col: Optional[str] = None,
        event_ts_format: Optional[str] = None,
        wait: bool = True,
        project_name: str = None,
        model_name: str = None,
        dataset_name: Optional[str] = None,
    ) -> Model:
        """
        Onboard model to Fiddler Platform
        :params project_id: The project to which the model belongs to
        :params model_id: The model name of which you need the details
        :param dataset_id: name of the dataset
        :param is_sync: Wait for job to complete or return after submitting
        :param project_name: project name where the model will be added
        :param model_name: name of the model
        :param dataset_name: name of the dataset
        :param model_info: (Deprecated) model related information from user
        :param task: Task the model is designed to address
        :param input_type: Whether the model is in the tabular or text
        :param schema: ModelSchema object
        :param spec: ModelSpec object
        :param task_params: ModelTaskParams object
        :param xai_params: XaiParams object
        :param display_name: Display name for the model
        :param description: Description for the model
        :param algorithm: Algorithm used for this model
        :param framework: Framework used for this model
        :param event_id_col: Column name to use as event id
        :param event_ts_col: Column name to use as event timestamp
        :param event_ts_format: Format of the event timestamp specified in event_ts_col
        :param wait: Whether to wait for job to complete or return after submitting
            the job
        """

        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )

        model_name = model_id_compat(
            model_id=model_id,
            model_name=model_name,
        )

        dataset_name = dataset_id_compat(
            dataset_id=dataset_id,
            dataset_name=dataset_name,
        )

        if model_info:
            warnings.warn(
                'model_info is deprecated from 2.0.0. Use schema and spec instead',
                DeprecationWarning,
            )
            if dataset_name:
                model_info.datasets = [dataset_name]
        elif not (schema and spec and input_type and task):
            raise ValueError(
                'Model requires either model_info or input_type, task, schema and spec'
            )

        request_body = {
            'name': model_name,
            'project_name': project_name,
            'organization_name': self.organization_name,
        }

        if model_info:
            request_body['info'] = model_info.to_dict()
        if dataset_name:
            request_body['dataset_name'] = dataset_name
        if input_type:
            request_body['input_type'] = input_type.value
        if task:
            request_body['task'] = task.value
        if schema:
            request_body['schema'] = schema.dict()
        if spec:
            request_body['spec'] = spec.dict()
        if task_params:
            request_body['task_params'] = task_params.dict()
        if xai_params:
            request_body['xai_params'] = xai_params.dict()
        if description:
            request_body['description'] = description
        if algorithm:
            request_body['algorithm'] = algorithm
        if framework:
            request_body['framework'] = framework
        if display_name:
            request_body['display_name'] = display_name
        if event_id_col:
            request_body['event_id_col'] = event_id_col
        if event_ts_col:
            request_body['event_ts_col'] = event_ts_col
        if event_ts_format:
            request_body['event_ts_format'] = event_ts_format

        response = self.client.post(
            url='models',
            data=request_body,
        )

        logger.info('Model %s added to %s project', model_name, project_name)

        model = Model.deserialize(APIResponseHandler(response))
        if model.job_uuid and wait:
            job_name = f'Model[{project_name}/{model_name}] - Initializing monitoring'
            self.wait_for_job(uuid=model.job_uuid, job_name=job_name)  # noqa

        return model

    @handle_api_error_response
    def update_model(
        self,
        model_name: str,
        project_name: str,
        info: Optional[ModelInfo] = None,
        file_list: Optional[List[Dict[str, Any]]] = None,
        framework: Optional[str] = None,
        requirements: Optional[str] = None,
    ) -> Model:
        """
        Update model metadata like model info, file

        :param project_name: project name where the model will be added
        :type project_name: string
        :param model_name: name of the model
        :type model_name: string
        :param info: model related information passed as dictionary from user
        :type info: ModelInfo object
        :param file_list: Artifact file list
        :type info: List of dictionaries
        :param framework: Model framework name
        :type framework: string
        :param requirements: Requirements
        :type requirements: string
        :return: Model object which contains the model details
        """
        body = {}

        if info:
            body['info'] = info.to_dict()

        if file_list:
            body['file_list'] = file_list

        if framework:
            body['framework'] = framework

        if requirements:
            body['requirements'] = requirements

        response = self.client.patch(
            url=f'models/{self.organization_name}:{project_name}:{model_name}',
            data=body,
        )
        logger.info('Model[%s/%s] - Updated model', project_name, model_name)

        return Model.deserialize(APIResponseHandler(response))

    @handle_api_error_response
    def delete_model(
        self,
        project_id: str = None,
        model_id: str = None,
        model_name: str = None,
        project_name: str = None,
    ) -> None:
        """
        Delete a model

        :params model_id: Model name to be deleted
        :params project_id: Project name to which the model belongs to.
        :params model_name: Model name to be deleted
        :params project_name: Project name to which the model belongs to.

        :returns: None
        """
        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )

        model_name = model_id_compat(
            model_id=model_id,
            model_name=model_name,
        )
        logger.info('Deleting model %s from %s project', model_name, project_name)
        self.client.delete(
            url=f'models/{self.organization_name}:{project_name}:{model_name}',
        )
        logger.info('Deleted model %s from %s project', model_name, project_name)

    @handle_api_error_response
    def add_model_surrogate(
        self,
        project_id: str = None,
        model_id: str = None,
        deployment_params: Optional[DeploymentParams] = None,
        model_name: str = None,
        project_name: str = None,
        wait: bool = True,
    ) -> str:
        """
        Add surrogate model to an existing model

        :params project_id: Project name to which the model belongs to.
        :params model_id: Model name to be added
        :param model_name: Model name
        :param project_name: Project name
        :param deployment_params: Model deployment parameters
        :param wait: Whether to wait for job to complete or return after submitting
            the job
        :return: Async job uuid
        """
        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )

        model_name = model_id_compat(
            model_id=model_id,
            model_name=model_name,
        )
        return self._deploy_surrogate_model(
            model_name=model_name,
            project_name=project_name,
            deployment_params=deployment_params,
            wait=wait,
            update=False,
        )

    @check_version(version_expr='>=23.1.0')
    @handle_api_error_response
    def update_model_surrogate(
        self,
        project_id: str = None,
        model_id: str = None,
        deployment_params: Optional[DeploymentParams] = None,
        is_sync: bool = True,
        model_name: str = None,
        project_name: str = None,
        wait: bool = True,
    ) -> str:
        """
        Re-generate surrogate model

        :params project_id: Project name to which the model belongs to.
        :params model_id: Model name to be updated
        :param model_name: Model name
        :param is_sync: Whether to wait for job to complete or return after submitting
            the job
        :param project_name: Project name
        :param deployment_params: Model deployment parameters
        :param wait: Whether to wait for job to complete or return after submitting
            the job

        :return: Async job uuid
        """
        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )

        model_name = model_id_compat(
            model_id=model_id,
            model_name=model_name,
        )

        wait = is_sync_id_compat(is_sync=is_sync, wait=wait)
        return self._deploy_surrogate_model(
            model_name=model_name,
            project_name=project_name,
            deployment_params=deployment_params,
            wait=wait,
            update=True,
        )

    def _deploy_surrogate_model(
        self,
        model_name: str,
        project_name: str,
        deployment_params: Optional[DeploymentParams] = None,
        wait: bool = True,
        update: bool = False,
    ) -> str:
        """
        Add surrogate model to an existing model
        :param model_name: Model name
        :param project_name: Project name
        :param deployment_params: Model deployment parameters
        :param wait: Whether to wait for job to complete or return after submitting
            the job
        :param update: Set True for re-generating surrogate model, otherwise False
        :return: Async job uuid
        """
        payload = {
            'model_name': model_name,
            'project_name': project_name,
            'organization_name': self.organization_name,
        }

        if deployment_params:
            deployment_params.artifact_type = ArtifactType.SURROGATE
            payload['deployment_params'] = deployment_params.dict(exclude_unset=True)

        model_id = f'{self.organization_name}:{project_name}:{model_name}'
        url = f'models/{model_id}/deploy-surrogate'
        method = self.client.put if update else self.client.post
        response = method(url=url, data=payload)

        data = APIResponseHandler(response).get_data()
        job_uuid = data['job_uuid']

        logger.info(
            'Model[%s/%s] - Submitted job (%s) for deploying a surrogate model',
            project_name,
            model_name,
            job_uuid,
        )

        if wait:
            job_name = f'Model[{project_name}/{model_name}] - Deploy a surrogate model'
            self.wait_for_job(uuid=job_uuid, job_name=job_name)  # noqa

        return job_uuid

    def _deploy_model_artifact(
        self,
        project_name: str,
        model_name: str,
        artifact_dir: str,
        deployment_params: Optional[DeploymentParams] = None,
        wait: bool = True,
        update: bool = False,
    ) -> str:
        """
        Upload and deploy model artifact for an existing model
        :param model_name: Model name
        :param project_name: Project name
        :param artifact_dir: Model artifact directory
        :param deployment_params: Model deployment parameters
        :param wait: Whether to wait for async job to finish or return
        :param update: Set True for updating artifact, False for adding artifact
        :return: Async job uuid
        """
        artifact_dir = Path(artifact_dir)
        validate_artifact_dir(artifact_dir)

        if (
            deployment_params
            and deployment_params.artifact_type == ArtifactType.SURROGATE
        ):
            raise ValueError(
                f'{ArtifactType.SURROGATE} artifact_type is an invalid value for this '
                f'method. Use {ArtifactType.PYTHON_PACKAGE} instead.'
            )

        self._update_model_on_artifact_upload(
            model_name=model_name, project_name=project_name, artifact_dir=artifact_dir
        )

        with tempfile.TemporaryDirectory() as tmp:
            # Archive model artifact directory
            logger.info(
                'Model[%s/%s] - Tarring model artifact directory - %s',
                project_name,
                model_name,
                artifact_dir,
            )
            file_path = shutil.make_archive(
                base_name=str(Path(tmp) / 'files'),
                format='tar',
                root_dir=str(artifact_dir),
                base_dir='.',
            )

            logger.info(
                'Model[%s/%s] - Model artifact tar file created at %s',
                project_name,
                model_name,
                file_path,
            )

            # Choose deployer based on archive file size
            if os.path.getsize(file_path) < MULTI_PART_CHUNK_SIZE:
                deployer_class = ModelArtifactDeployer
            else:
                deployer_class = MultiPartModelArtifactDeployer

            deployer = deployer_class(
                client=self.client,
                model_name=model_name,
                project_name=project_name,
                organization_name=self.organization_name,
                update=update,
            )

            job_uuid = deployer.deploy(
                file_path=Path(file_path), deployment_params=deployment_params
            )

        logger.info(
            'Model[%s/%s] - Submitted job (%s) for deploying model artifact',
            project_name,
            model_name,
            job_uuid,
        )

        if wait:
            job_name = f'Model[{project_name}/{model_name}] - Deploy model artifact'
            self.wait_for_job(uuid=job_uuid, job_name=job_name)  # noqa

        return job_uuid

    @handle_api_error_response
    def add_model_artifact(
        self,
        project_id: str = None,
        model_id: str = None,
        model_dir: str = None,
        deployment_params: Optional[DeploymentParams] = None,
        model_name: str = None,
        project_name: str = None,
        artifact_dir: str = None,
        wait: bool = True,
    ) -> str:
        """
        Add model artifact to an existing model

        :params project_id: Project name to which the model belongs to.
        :params model_id: Model name to be added
        :param model_dir: Model artifact directory
        :param model_name: Model name
        :param project_name: Project name
        :param artifact_dir: Model artifact directory
        :param deployment_params: Model deployment parameters
        :param wait: Whether to wait for async job to finish or return
        :return: Async job uuid
        """
        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )

        model_name = model_id_compat(
            model_id=model_id,
            model_name=model_name,
        )
        artifact_dir = model_dir_compat(
            model_dir=model_dir,
            artifact_dir=artifact_dir,
        )
        return self._deploy_model_artifact(
            project_name=project_name,
            model_name=model_name,
            artifact_dir=artifact_dir,
            deployment_params=deployment_params,
            wait=wait,
            update=False,
        )

    @check_version(version_expr='>=22.12.0')
    @handle_api_error_response
    def update_model_artifact(
        self,
        project_id: str = None,
        model_id: str = None,
        model_dir: str = None,
        deployment_params: Optional[DeploymentParams] = None,
        is_sync: bool = True,
        model_name: str = None,
        project_name: str = None,
        artifact_dir: str = None,
        wait: bool = True,
    ) -> str:
        """
        Update model artifact of an existing model

        :params project_id: Project name to which the model belongs to.
        :params model_id: Model name to be added
        :param model_dir: Model artifact directory
        :param model_name: Model name
        :param project_name: Project name
        :param artifact_dir: Model artifact directory
        :param deployment_params: Model deployment parameters
        :param wait: Whether to wait for async job to finish or return
        :return: Async job uuid
        """
        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )

        model_name = model_id_compat(
            model_id=model_id,
            model_name=model_name,
        )
        artifact_dir = model_dir_compat(
            model_dir=model_dir,
            artifact_dir=artifact_dir,
        )
        wait = is_sync_id_compat(is_sync=is_sync, wait=wait)
        return self._deploy_model_artifact(
            project_name=project_name,
            model_name=model_name,
            artifact_dir=artifact_dir,
            deployment_params=deployment_params,
            wait=wait,
            update=True,
        )

    def _update_model_on_artifact_upload(
        self, model_name: str, project_name: str, artifact_dir: Path
    ) -> None:
        """Update model metadata based on artifact dir contents"""
        file_list = get_model_artifact_info(artifact_dir=artifact_dir)
        model_info = read_model_yaml(artifact_dir=artifact_dir)

        self.update_model(
            model_name=model_name,
            project_name=project_name,
            info=model_info,
            file_list=file_list,
        )

    @handle_api_error_response
    def download_artifacts(self, project_name: str, model_name: str, output_dir: Path):
        """
        download the model binary, package.py and model.yaml to the given
        output dir.

        :param project_name: Project name
        :param model_name: Model name
        :param output_dir: output directory
        :return: None
        """

        if output_dir.exists():
            raise ValueError(f'output dir already exists {output_dir}')

        model_id = f'{self.organization_name}:{project_name}:{model_name}'
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Download tar file
            tar_file_path = os.path.join(tmp_dir, 'artifact.tar')

            with self.client.get(url=f'models/{model_id}/download-artifacts') as r:
                r.raise_for_status()
                with open(tar_file_path, mode='wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            os.makedirs(output_dir, exist_ok=True)
            shutil.unpack_archive(tar_file_path, extract_dir=output_dir, format='tar')
