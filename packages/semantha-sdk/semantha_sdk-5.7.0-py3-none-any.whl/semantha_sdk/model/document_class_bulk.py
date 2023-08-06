
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.model.semantha_entity import SemanthaModelEntity, SemanthaSchema

from semantha_sdk.model.custom_field import CustomField
from typing import List
from typing import Optional


@dataclass(frozen=True)
class DocumentClassBulk(SemanthaModelEntity):
    """ author semantha, this is a generated class do not change manually! """
    id: Optional[str]
    name: str
    document_ids: Optional[List[str]]
    sub_classes: Optional[List["DocumentClassBulk"]]
    tags: Optional[List[str]]
    color: Optional[str]
    comment: Optional[str]
    created: Optional[int]
    updated: Optional[int]
    metata: Optional[str]
    custom_fields: Optional[List[CustomField]]

DocumentClassBulkSchema = class_schema(DocumentClassBulk, base_schema=SemanthaSchema)
