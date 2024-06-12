from aiogram import Bot

from config import TOKEN_TEST


async def channel_send_message(channel_id: int | str, text: str, photo):
    bot_sender = Bot(TOKEN_TEST)
    try:
        await bot_sender.send_photo(channel_id, photo=photo, caption=f'{text}')
    except Exception as e:
        print(e)
    finally:
        await bot_sender.session.close()
