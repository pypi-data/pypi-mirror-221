from typing import Dict
from pydantic import BaseModel
import os
from enum import Enum


api_identifier = str
api_key = str
ApiKeys = Dict[api_identifier, api_key]


class Environment(Enum):
    PROD = "prod"
    DEV = "dev"


def default_env() -> Environment:
    env = os.getenv("ENV")
    if env is not None:
        env = env.lower()
        if env in [e.value for e in Environment]:
            return Environment(env)
    return Environment.DEV


environment: Environment = default_env()
verbose: bool = False
is_interactive_mode: bool = False
api_keys: ApiKeys = {}
abspath_to_project_root: str | None = None
current_api_identifier: api_identifier | None = None
_use_local_api: bool = False


def get_api_keys() -> ApiKeys:
    global api_keys
    return api_keys


def get_abspath_to_project_root() -> str:
    global abspath_to_project_root
    return abspath_to_project_root or ""


def add_api(api_identifier: str, api_key: str):
    api_identifier = api_identifier.lower()
    global current_api_identifier
    current_api_identifier = api_identifier
    api_keys[api_identifier] = api_key


def get_current_api_identifier() -> api_identifier | None:
    global current_api_identifier
    return current_api_identifier


def remove_api(api_identifier: str):
    global api_keys
    if api_identifier in api_keys:
        api_keys.pop(api_identifier)


def set_interactive_mode(should_use_interactive_mode: bool):
    global is_interactive_mode
    is_interactive_mode = should_use_interactive_mode


def set_environment(env: Environment | str):
    global environment
    if isinstance(env, Environment):
        environment = env
    else:
        env = env.lower()
        if env not in [e.value for e in Environment]:
            raise Exception("Environment doesn't exist, use 'prod' or 'dev'")
        environment = Environment(env)
