from aiogram import Bot

from config import TOKEN_TEST


async def get_chat_member(id_channel: str) -> dict:
    bot_getter = Bot(TOKEN_TEST)
    try:
        chat_id = id_channel
        members_count = await bot_getter.get_chat_member_count(chat_id=chat_id)
        return f'Количество участников в канале: {members_count}'
    except Exception as e:
        return f'Произошла ошибка: {e}'
    finally:
        await bot_getter.session.close()
