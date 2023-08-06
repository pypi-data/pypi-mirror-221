
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.model.semantha_entity import SemanthaModelEntity, SemanthaSchema

from semantha_sdk.model.label import Label
from semantha_sdk.model.metadata_value import MetadataValue
from typing import List
from typing import Optional


@dataclass(frozen=True)
class Attribute(SemanthaModelEntity):
    """ author semantha, this is a generated class do not change manually! """
    id: Optional[str]
    name: str
    read_only: Optional[bool]
    functional: Optional[bool]
    labels: Optional[List[Label]]
    metadata: Optional[List[MetadataValue]]
    comment: Optional[str]
    datatype: str
    relevant_for_relation: Optional[bool]
    object_property_id: Optional[str]

AttributeSchema = class_schema(Attribute, base_schema=SemanthaSchema)
