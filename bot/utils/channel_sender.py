from aiogram import Bot

from config import TOKEN_TEST


async def channel_send_message(channel_id: int | str, text: str):
    bot_sender = Bot(TOKEN_TEST)
    try:
        await bot_sender.send_message(channel_id, text)
    except Exception as e:
        print(e)
    finally:
        await bot_sender.session.close()
