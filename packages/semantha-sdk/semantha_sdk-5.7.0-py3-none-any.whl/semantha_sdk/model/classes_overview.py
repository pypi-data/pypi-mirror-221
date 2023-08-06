
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.model.semantha_entity import SemanthaModelEntity, SemanthaSchema

from typing import List
from typing import Optional


@dataclass(frozen=True)
class ClassesOverview(SemanthaModelEntity):
    """ author semantha, this is a generated class do not change manually! """
    id: Optional[str]
    name: str
    read_only: Optional[bool]
    attributes: Optional[List["ClassesOverview"]]
    object_property_id: Optional[str]

ClassesOverviewSchema = class_schema(ClassesOverview, base_schema=SemanthaSchema)
