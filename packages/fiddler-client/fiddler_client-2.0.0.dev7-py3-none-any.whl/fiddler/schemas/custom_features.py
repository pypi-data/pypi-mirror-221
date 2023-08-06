from enum import Enum
from typing import List, Optional, Type, TypeVar

from pydantic import BaseModel

T = TypeVar('T', bound='CustomFeature')


class CustomFeatureType(str, Enum):
    FROM_COLUMNS = 'FROM_COLUMNS'
    FROM_TEXT_EMBEDDING = 'FROM_TEXT_EMBEDDING'
    FROM_IMAGE_EMBEDDING = 'FROM_IMAGE_EMBEDDING'


class CustomFeature(BaseModel):
    name: str
    type: CustomFeatureType
    n_clusters: Optional[int] = 5
    centroids: Optional[List] = None

    class Config:
        allow_mutation = False

    @classmethod
    def from_dict(cls: Type[T], deserialized_json: dict) -> T:
        feature_type = CustomFeatureType(deserialized_json['type'])
        if feature_type == CustomFeatureType.FROM_COLUMNS:
            return Multivariate.parse_obj(deserialized_json)
        elif feature_type == CustomFeatureType.FROM_TEXT_EMBEDDING:
            return TextEmbedding.parse_obj(deserialized_json)
        elif feature_type == CustomFeatureType.FROM_IMAGE_EMBEDDING:
            return ImageEmbedding.parse_obj(deserialized_json)
        else:
            raise ValueError(f'Unsupported feature type: {feature_type}')


class Multivariate(CustomFeature):
    columns: List[str]
    monitor_components: bool = False


class VectorFeature(CustomFeature):
    source_column: Optional[str] = None
    column: str


class TextEmbedding(VectorFeature):
    type: CustomFeatureType = CustomFeatureType.FROM_TEXT_EMBEDDING


class ImageEmbedding(VectorFeature):
    type: CustomFeatureType = CustomFeatureType.FROM_IMAGE_EMBEDDING
