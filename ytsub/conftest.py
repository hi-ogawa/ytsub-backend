#
# pytest configuration
#

import pytest

from .config import env
from .db import session_generator, sessionmaker_generator

assert env == "test"


@pytest.fixture
async def Session():
    async for Session_ in sessionmaker_generator():
        yield Session_


@pytest.fixture
async def session():
    async for session_ in session_generator():
        yield session_
