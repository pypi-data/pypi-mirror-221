import inspect
from typing import Any, Dict, List, Set, TypedDict, Union

from pydantic import BaseModel

# from codespeak.function.replace_function import replace_function
from codespeak.inference.replace_function import replace_function
import libcst as cst
from codespeak.helpers.align import align
from codespeak.inference.make_inference_response import MakeInferenceResponse
from codespeak.helpers.extract_delimited_python_code_from_string import (
    extract_delimited_python_code_from_string,
)


class ImportTransformer(cst.CSTTransformer):
    def __init__(self, should_remove: bool = False) -> None:
        self.imports: list[cst.ImportFrom | cst.Import] = []
        self.unique_imports: Set[ImportDefinition] = set()
        self.should_remove = should_remove

    def leave_ImportFrom(
        self, original_node: cst.ImportFrom, updated_node: cst.ImportFrom
    ):
        node = updated_node
        self.imports.append(node)
        if isinstance(node.names, cst.ImportStar):
            self.unique_imports.add(
                ImportDefinition(module=node.module.value, name="*", asname=None)  # type: ignore
            )
        else:
            for imported in node.names:
                module = node.module
                if isinstance(module, cst.Attribute):
                    module_name = get_attr_name(module)
                elif isinstance(module, cst.Name):
                    module_name = module.value  # This is a cst.Name node.
                else:
                    raise ValueError("Unexpected module type")
                value_name = imported.name.value
                as_name = imported.asname.name.value if imported.asname else None  # type: ignore
                self.unique_imports.add(
                    ImportDefinition(
                        module=module_name, name=value_name, asname=as_name  # type: ignore
                    )
                )
        if self.should_remove:
            return cst.RemoveFromParent()
        else:
            return node

    def leave_Import(
        self, original_node: cst.Import, updated_node: cst.Import
    ):  # -> Union[cst.Import, cst.RemovalSentinel]:
        node = updated_node
        self.imports.append(node)
        for imported in node.names:
            module = imported.name.value
            as_name = imported.asname.name.value if imported.asname else None  # type: ignore
            if isinstance(module, cst.BaseExpression):
                print("found base expression")
            module = str(module)
            self.unique_imports.add(
                ImportDefinition(module=module, name=None, asname=as_name)
            )
        if self.should_remove:
            return cst.RemoveFromParent()
        else:
            return node


def get_attr_name(attr: cst.Attribute) -> str:
    """Recursive function to get the full name of an attribute."""
    if isinstance(attr.value, cst.Attribute):
        return get_attr_name(attr.value) + "." + attr.attr.value
    else:
        value: Any = attr.value
        if hasattr(value, "value"):
            return value.value + "." + attr.attr.value
        else:
            raise ValueError("Attribute has no value")


class ImportDefinition(BaseModel):
    module: str
    name: str | None = None
    asname: str | None = None

    def __eq__(self, other):
        if isinstance(other, ImportDefinition):
            return (
                self.module == other.module
                and self.name == other.name
                and self.asname == other.asname
            )
        return False

    def __hash__(self):
        return hash((self.module, self.name, self.asname))

    def value_as_str(self) -> str | None:
        if self.asname:
            return f"{self.name} as {self.asname}"
        else:
            return self.name


def print_imports(import_defs: Set[ImportDefinition]) -> None:
    for import_def in import_defs:
        print("\n")
        print(import_def.dict(exclude_none=True))


class ImportsResult(TypedDict):
    code: str
    imports: Set[ImportDefinition]


def get_imports(
    source_code: str | None = None,
    filepath: str | None = None,
) -> Set[ImportDefinition]:
    if source_code is None and filepath is None:
        raise ValueError("Must provide either source_code or filepath")
    _source_code = ""
    if source_code is not None:
        _source_code = source_code
    elif filepath is not None:
        with open(filepath, "r") as f:
            _source_code = f.read()
    tree = cst.parse_module(_source_code)
    visitor = ImportTransformer(should_remove=False)
    tree.visit(visitor)
    return visitor.unique_imports


def pop_imports(
    source_code: str | None = None,
    filepath: str | None = None,
) -> ImportsResult:
    if source_code is None and filepath is None:
        raise ValueError("Must provide either source_code or filepath")
    _source_code = ""
    if source_code is not None:
        _source_code = source_code
    elif filepath is not None:
        with open(filepath, "r") as f:
            _source_code = f.read()
    tree = cst.parse_module(_source_code)
    visitor = ImportTransformer(should_remove=True)
    new_tree = tree.visit(visitor)
    return ImportsResult(code=new_tree.code, imports=visitor.unique_imports)


"""
to start

1. get all the imports in the existing file
2. check if the new imports are already in the existing imports
3. if they are, remove them from the new imports
4. if they are not, add them to the existing imports— the question is do i add them alongside the function or at the top? I think alongside the function for now
"""


def remove_existing_imports_from_incoming_imports(
    existing_imports: Set[ImportDefinition],
    incoming_imports: Set[ImportDefinition],
) -> Set[ImportDefinition]:
    for existing_import in existing_imports:
        if existing_import in incoming_imports:
            incoming_imports.remove(existing_import)
    return incoming_imports


def flatten_imports(imports: Set[ImportDefinition]) -> Dict[str, List[str]]:
    flattened_imports: Dict[str, List[str]] = {}
    for _import in imports:
        if not _import.module in flattened_imports:
            flattened_imports[_import.module] = []
        module = flattened_imports.get(_import.module, [])

        _str = _import.value_as_str()
        if _str is not None:
            module.append(_str)
        flattened_imports[_import.module] = module
    return flattened_imports


def to_incoming_imports_statements(flattened_imports: Dict) -> List[str]:
    statements = []
    for module, imports in flattened_imports.items():
        if len(imports) == 0:
            statements.append(f"import {module}")
        else:
            imports_str = ", ".join(imports)
            statements.append(f"from {module} import {imports_str}")
    return statements


def transform_inference(inference: str, source_file: str) -> MakeInferenceResponse:
    inference_source_code = extract_delimited_python_code_from_string(inference)
    existing_imports = get_imports(filepath=source_file)
    inference_imports_transform = pop_imports(inference_source_code)
    unique_incoming_imports = remove_existing_imports_from_incoming_imports(
        existing_imports=existing_imports,
        incoming_imports=inference_imports_transform["imports"],
    )
    flattened_imports = flatten_imports(unique_incoming_imports)
    incoming_imports_statements = to_incoming_imports_statements(flattened_imports)
    new_source_code = inference_imports_transform["code"]
    return MakeInferenceResponse(
        source_code=new_source_code, import_statements=incoming_imports_statements
    )
