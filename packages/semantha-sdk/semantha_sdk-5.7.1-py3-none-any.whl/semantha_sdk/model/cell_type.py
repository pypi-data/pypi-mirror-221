
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.model.semantha_entity import SemanthaModelEntity, SemanthaSchema

from typing import Optional


@dataclass(frozen=True)
class CellType(SemanthaModelEntity):
    """ author semantha, this is a generated class do not change manually! """
    id: Optional[str] = None
    name: Optional[str] = None
    color: Optional[str] = None

CellTypeSchema = class_schema(CellType, base_schema=SemanthaSchema)
