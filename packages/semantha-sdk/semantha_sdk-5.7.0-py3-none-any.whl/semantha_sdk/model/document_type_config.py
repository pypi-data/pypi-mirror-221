
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from semantha_sdk.model.semantha_entity import SemanthaModelEntity, SemanthaSchema

from semantha_sdk.model.area import Area
from typing import List
from typing import Optional


@dataclass(frozen=True)
class DocumentTypeConfig(SemanthaModelEntity):
    """ author semantha, this is a generated class do not change manually! """
    do_linebased_processing: Optional[bool]
    viewport: Optional[Area]
    ignored_pages: Optional[List[int]]
    do_language_detection: Optional[bool]
    do_object_detection: Optional[bool]
    do_sub_document_splitting: Optional[bool]
    split_modus: Optional[str]
    split_by_type: Optional[str]
    split_by_regex: Optional[str]
    based_on_document_type: Optional[str]
    do_auto_splitting: Optional[bool]
    auto_split_distance: Optional[float]
    use_similarity_model_for_extraction: Optional[bool]
    do_contradiction_detection: Optional[bool]
    do_paragraph_merging_for_text_files: Optional[bool]

DocumentTypeConfigSchema = class_schema(DocumentTypeConfig, base_schema=SemanthaSchema)
