
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.model.semantha_entity import SemanthaModelEntity, SemanthaSchema

from semantha_sdk.model.custom_field import CustomField
from typing import List
from typing import Optional


@dataclass(frozen=True)
class DocumentClassNode(SemanthaModelEntity):
    """ author semantha, this is a generated class do not change manually! """
    id: Optional[str]
    name: str
    parent_id: Optional[str]
    metadata: Optional[str]
    documents_count: Optional[int]
    custom_fields: Optional[List[CustomField]]

DocumentClassNodeSchema = class_schema(DocumentClassNode, base_schema=SemanthaSchema)
