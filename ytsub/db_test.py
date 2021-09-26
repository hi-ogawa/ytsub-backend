import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from .config import config

pytestmark = pytest.mark.asyncio


async def test_connection():
    engine = create_async_engine(config.database_url, echo=config.database_echo)
    async with engine.connect() as conn:
        await conn.close()
    await engine.dispose()


async def test_Session(Session: type[AsyncSession]):
    async with Session() as session:
        res = await session.execute(text("SELECT 1, 2, 3"))
        assert res.first() == (1, 2, 3)


async def test_session(session: AsyncSession):
    res = await session.execute(text("SELECT 1, 2, 3"))
    assert res.first() == (1, 2, 3)
