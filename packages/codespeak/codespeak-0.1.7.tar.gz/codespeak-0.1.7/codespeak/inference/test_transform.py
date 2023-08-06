import inspect
from typing import Any, Dict, List, Set, TypedDict, Union

from pydantic import BaseModel

# from codespeak.function.replace_function import replace_function
from codespeak.inference.replace_function import replace_function
import libcst as cst
from codespeak.helpers.align import align
from codespeak.inference.inference_engine import MakeInferenceResponse
from codespeak.inference.transform_inference import (
    pop_imports,
    get_imports,
    to_incoming_imports_statements,
    remove_existing_imports_from_incoming_imports,
    flatten_imports,
)

# def fake(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)

#     return wrapper


"""
1. take all the code up until the first function
2. 
"""

existing_source_code = align(
    """
    from inspect import getsourcefile
    from codespeak.function.replace_function import replace_function
    import libcst as cst
    from codespeak.helpers.align import align, malign, grind as gd

    def run_it_up():
        return True
    """
)

# from codespeak import *
# from codespeak.app.runner import writable
# from codespeak.helpers.align import travesty, align
new_source_code = align(
    """
    from libcst import cst
    from libg import ggg
    def test_me():
        return True
    """
)


def test_replace_function():
    """this is my function"""


existing_imports = get_imports(existing_source_code)
incoming_imports_transform = pop_imports(new_source_code)

# print_imports(existing_imports)
# print_imports(incoming_imports)

unique_incoming_imports = remove_existing_imports_from_incoming_imports(
    existing_imports=existing_imports,
    incoming_imports=incoming_imports_transform["imports"],
)


if __name__ == "__main__":
    x = 3
    # print_imports(unique_incoming_imports)
    # print_unique_imports(unique_imports)
    # new_module = cst.Module(body=all_imports)
    # print(new_module.code)
    filepath = inspect.getsourcefile(test_replace_function) or ""
    print(incoming_imports_transform["code"])
    flattened_imports = flatten_imports(unique_incoming_imports)
    sss = to_incoming_imports_statements(flattened_imports)
    # print(sss)
    replace_function(
        filepath=filepath,
        function_name="test_replace_function",
        new_source_code=incoming_imports_transform["code"],
        incoming_import_statements=sss,
    )


# # Use a libcst.CSTVisitor to find all top-level import statements

# def visit_ImportFrom(self, node: cst.ImportFrom) -> None:
#     module_name = node.module
#     if module_name is not None:
#         if isinstance(node.names, cst.ImportStar):
#             print(f"from {module_name.value} import *")
#         else:
#             for imported_name in node.names:
#                 if imported_name.asname is not None:
#                     print(
#                         f"from {module_name.value} import {imported_name.name.value} as {imported_name.asname.name.value}"
#                     )
#                 else:
#                     print("working here")
#                     print(
#                         f"from {module_name.value} import {imported_name.name.value}"
#                     )

# def visit_Import(self, node: cst.Import) -> None:
#     for imported_name in node.names:
#         if imported_name.asname is not None:
#             print(
#                 f"import {imported_name.name.value} as {imported_name.asname.name.value}"
#             )
#         else:
#             print(f"import {imported_name.name.value}")

# for _import in existing_imports + incoming_imports:
#     if isinstance(_import, cst.Import):
#         for imported in _import.names:
#             module = imported.name.value
#             as_name = imported.asname.name.value if imported.asname else None  # type: ignore
#             if isinstance(module, cst.BaseExpression):
#                 print("found base expression")
#             module = str(module)
#             unique_imports.add(
#                 ImportDefinition(module=module, name=None, asname=as_name)
#             )
#     elif isinstance(_import, cst.ImportFrom):
#         for imported in _import.names:  # type: ignore ——add star support later
#             module = _import.module
#             if isinstance(module, cst.Attribute):
#                 module_name = get_attr_name(module)
#             elif isinstance(module, cst.Name):
#                 module_name = module.value  # This is a cst.Name node.
#             else:
#                 raise ValueError("Unexpected module type")
#             value_name = imported.name.value
#             as_name = imported.asname.name.value if imported.asname else None
#             unique_imports.add(
#                 ImportDefinition(module=module_name, name=value_name, asname=as_name)
#             )
