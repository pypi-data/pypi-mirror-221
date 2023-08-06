from typing import List, TypedDict


class MakeInferenceResponse(TypedDict):
    source_code: str
    import_statements: List[str]
