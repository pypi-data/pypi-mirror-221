import inspect
from typing import Any
from codespeak.helpers.auto_detect_abspath_to_project_root import (
    auto_detect_abspath_to_project_root,
)
from codespeak import settings


def guarantee_abspath_to_project_root_exists(object_in_project: Any):
    if settings.abspath_to_project_root is None:
        path = inspect.getabsfile(object_in_project)
        settings.abspath_to_project_root = auto_detect_abspath_to_project_root(path)
