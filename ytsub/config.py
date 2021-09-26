import os
from typing import Literal, cast

from pydantic import BaseModel

from .config_utils import load

ENV_PREFIX = "APP"

Env = Literal["test", "development", "production"]


def load_env() -> Env:
    _env = os.getenv(f"{ENV_PREFIX}_env", "development")
    assert _env in ["test", "development", "production"]
    return cast(Env, _env)


class Config(BaseModel):
    database_url: str
    database_echo: bool
    jwt_secret: str


env = load_env()
config = load(Config, [f"config/{env}.json"], ENV_PREFIX)
