import pytest
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from .user import User

pytestmark = pytest.mark.asyncio


async def test_user(session: AsyncSession):
    async with session.begin():
        await session.execute(delete(User))
        session.add(User(username="john", password_digest="xxyyzz"))
