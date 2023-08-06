
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.model.semantha_entity import SemanthaModelEntity, SemanthaSchema

from typing import Optional


@dataclass(frozen=True)
class CustomField(SemanthaModelEntity):
    """ author semantha, this is a generated class do not change manually! """
    name: Optional[str]
    value: Optional[str]
    type: Optional[str]

CustomFieldSchema = class_schema(CustomField, base_schema=SemanthaSchema)
