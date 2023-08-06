
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.model.semantha_entity import SemanthaModelEntity, SemanthaSchema

from typing import Optional


@dataclass(frozen=True)
class DocumentTypeChange(SemanthaModelEntity):
    """ author semantha, this is a generated class do not change manually! """
    name: Optional[str]
    do_object_detection: Optional[bool]
    do_contradiction_detection: Optional[bool]
    do_sub_document_splitting: Optional[bool]
    split_modus: Optional[str]
    split_by_type: Optional[str]
    split_by_regex: Optional[str]
    use_similarity_model_for_extraction: Optional[bool]
    do_paragraph_merging_for_text_files: Optional[bool]

DocumentTypeChangeSchema = class_schema(DocumentTypeChange, base_schema=SemanthaSchema)
