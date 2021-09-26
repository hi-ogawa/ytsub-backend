from collections.abc import AsyncGenerator
from typing import cast

from aiohttp.web import Application
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from .config import config


async def engine_generator() -> AsyncGenerator[AsyncEngine, None]:
    engine = create_async_engine(config.database_url, echo=config.database_echo)
    yield engine
    await engine.dispose()


async def connection_generator() -> AsyncGenerator[AsyncConnection, None]:
    async for engine in engine_generator():
        async with engine.begin() as connection:
            yield connection


async def sessionmaker_generator() -> AsyncGenerator[type[AsyncSession], None]:
    async for engine in engine_generator():
        yield cast(
            type[AsyncSession],
            sessionmaker(bind=engine, future=True, class_=AsyncSession),
        )


async def session_generator() -> AsyncGenerator[AsyncSession, None]:
    async for Session in sessionmaker_generator():
        async with Session() as session:
            yield session


async def inject_session(app: Application) -> AsyncGenerator[None, None]:
    async for Session in sessionmaker_generator():
        app["Session"] = Session
        yield
