from sqlalchemy import select

from db.SQL.models.base import async_session
from db.SQL.models.chat import ChatHistory
from db.SQL.models.user import User


async def search_for_id(id_tg: int):
    async with async_session() as session:
        query = select(User).where(User.id_tg == id_tg)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        return user


async def add_user(id_tg: int):
    async with async_session() as session:
        user = User(id_tg=id_tg)
        session.add(user)
        await session.flush()
        history = ChatHistory(id_tg=user.id_tg)
        session.add(history)

        await session.commit()
