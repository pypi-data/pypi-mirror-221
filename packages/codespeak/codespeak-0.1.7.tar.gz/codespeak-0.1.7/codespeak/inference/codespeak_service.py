import json
import re
import httpx
from codespeak.function.function_lite import FunctionLite
import codespeak
from codespeak import settings


def url():
    if settings._use_local_api:
        return "http://localhost:8000"
    return "https://codespeak-api-production.up.railway.app"


@staticmethod
async def make_inference(function_lite: FunctionLite, api_identifier: str) -> str:
    print("Making inference...")
    path = "/v1/inferences/make"
    data = {
        "function_lite": function_lite.dict(),
        "api": api_identifier,
        "password": codespeak.password,
    }
    response_text = ""
    _url = f"{url()}{path}"
    async with httpx.AsyncClient() as client:
        async with client.stream("POST", url=_url, json=data, timeout=30) as response:
            async for chunk in response.aiter_bytes():
                text = chunk.decode()
                response_text += text
                print(text, end="")
    print("\n")
    return response_text
