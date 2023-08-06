import asyncio
import inspect
from typing import Any, Callable, Dict, List, Tuple, TypedDict
from pydantic import BaseModel
from codespeak.function.function_lite import FunctionLite
from codespeak.inference import codespeak_service
from codespeak.helpers.extract_delimited_python_code_from_string import (
    extract_delimited_python_code_from_string,
)
from codespeak.inference.make_inference_response import MakeInferenceResponse
from codespeak.inference.replace_function import replace_function
from codespeak.inference.transform_inference import transform_inference


class InferenceEngine(BaseModel):
    api_identifier: str
    function_lite: FunctionLite

    def make_inference(self, source_file: str) -> MakeInferenceResponse:
        inference = asyncio.run(
            codespeak_service.make_inference(self.function_lite, self.api_identifier)
        )
        transformed_inference = self.transform_inference(inference, source_file)
        # print("SOURCE:\n")
        # print(source_code)
        return transformed_inference

    def write_inference(
        self, inference: MakeInferenceResponse, source_file: str
    ) -> None:
        replace_function(
            filepath=source_file,
            function_name=self.function_lite.declaration.name,
            new_source_code=inference["source_code"],
            incoming_import_statements=inference["import_statements"],
        )

    def add_back_decorator(self, source_code: str) -> str:
        decorator = self.function_lite.declaration.source_code.split("\n")[0]
        source_code = source_code.strip("\n")
        return decorator + "\n" + source_code

    def transform_inference(
        self, inference: str, source_file: str
    ) -> MakeInferenceResponse:
        transformed_inference = transform_inference(inference, source_file)
        transformed_inference["source_code"] = self.add_back_decorator(
            transformed_inference["source_code"]
        )
        return transformed_inference

    # i'll have the option to reload it and execute it with a load, or just execute the source with exec
    # i'd probably rather reload it so I know it's working in its natural habitat, but that doesn't matter right now
