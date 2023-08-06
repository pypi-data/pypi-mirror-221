from .function import WritableFunction
from .settings import (
    set_environment,
    add_api,
    set_interactive_mode,
    remove_api,
    Environment,
)
from .public.dot_get import dot_get
from .public.rest_requests.get import get
from .public.rest_requests.post import post
from .public.rest_requests.put import put
from .public.rest_requests.delete import delete
from .decorate.writable import writable

password: str = ""
