import inspect
import json
from typing import Any, Callable, Dict, List, ClassVar, Tuple
from codespeak.function.function_declaration import FunctionDeclaration
from codespeak.function.function_lite import FunctionLite
from codespeak.helpers.self_type import self_type_if_exists
from codespeak.inference.replace_function import replace_function
from codespeak.inference.inference_engine import InferenceEngine, MakeInferenceResponse
from codespeak.frame import Frame
from codespeak.function.function_attributes import FunctionAttributes
from codespeak.function.function_declaration_lite import FunctionDeclarationLite
from codespeak import settings


class WritableFunction:
    func: Callable

    def __init__(self, func: Callable) -> None:
        if not hasattr(func, FunctionAttributes.frame):
            raise Exception(
                "No frame found. Make sure this is an inferred function—it should use codespeak's @infer decorator"
            )
        self.func = func

    @property
    def declaration(self) -> FunctionDeclaration:
        return getattr(self.func, FunctionAttributes.declaration)

    @property
    def frame(self) -> Frame:
        return Frame.for_function(self.func)

    def _make_and_write_inference(self, source_file: str) -> MakeInferenceResponse:
        function_lite = self.to_function_lite()
        api_identifier = settings.get_current_api_identifier()
        if api_identifier is None:
            raise ValueError("No api set. Add an api with codespeak.add_api()")
        inference_engine = InferenceEngine(
            function_lite=function_lite,
            api_identifier=api_identifier,
        )
        inference = inference_engine.make_inference(source_file=source_file)
        inference_engine.write_inference(inference=inference, source_file=source_file)
        return inference

    def source_file(self) -> str:
        ff = inspect.getsourcefile(self.func)
        if ff is None:
            raise ValueError("Function must be defined in a file")
        return ff

    def write(self) -> None:
        self._write(self.source_file())

    def _write(self, source_file: str) -> None:
        self._make_and_write_inference(source_file=source_file)

    def to_function_lite(self) -> FunctionLite:
        return FunctionLite(
            declaration=self.declaration.to_declaration_lite(),
            custom_types=self.frame.custom_types(),
        )

    @staticmethod
    def from_function_object(func: Callable[..., Any]) -> "WritableFunction":
        """get classified Function object for an inferred function"""
        return WritableFunction(func=func)
