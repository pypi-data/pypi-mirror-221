"""
Fiddler Client Module
=====================

A Python client for Fiddler service.

TODO: Add Licence.
"""

from fiddler import utils
from fiddler._version import __version__
from fiddler.constants import CSV_EXTENSION
from fiddler.core_objects import (
    ArtifactStatus,
    BaselineType,
    BatchPublishType,
    Column,
    DatasetInfo,
    DataType,
    DeploymentType,
    ExplanationMethod,
    FiddlerPublishSchema,
    FiddlerTimestamp,
    ModelInfo,
    ModelInputType,
    ModelTask,
    WeightingParams,
    WindowSize,
)
from fiddler.packtools import gem
from fiddler.schemas.custom_features import Multivariate, TextEmbedding
from fiddler.utils import logger
from fiddler.utils.validator import (
    PackageValidator,
    ValidationChainSettings,
    ValidationModule,
)
from fiddler.v2.api.api import FiddlerApi, FiddlerClient
from fiddler.v2.api.explainability_mixin import (
    DatasetDataSource,
    RowDataSource,
    SqlSliceQueryDataSource,
)
from fiddler.v2.schema.alert import (
    AlertCondition,
    AlertType,
    BinSize,
    ComparePeriod,
    CompareTo,
    Metric,
    Priority,
)

logger = logger.get_logger(__name__)

SUPPORTED_API_VERSIONS = ['v2']


__all__ = [
    '__version__',
    'BatchPublishType',
    'Column',
    'Multivariate',
    'TextEmbedding',
    'ImageEmbedding',
    'ColorLogger',
    'DatasetInfo',
    'DataType',
    'FiddlerClient',
    'FiddlerApi',
    'FiddlerTimestamp',
    'FiddlerPublishSchema',
    'gem',
    'ModelInfo',
    'ModelInputType',
    'ModelTask',
    'WeightingParams',
    'ExplanationMethod',
    'PackageValidator',
    'ValidationChainSettings',
    'ValidationModule',
    'utils',
    # Exposing constants
    'CSV_EXTENSION',
]
