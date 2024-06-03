from aiogram import Router, types, F
from aiogram.filters import CommandStart

from bot.utils.channel_sender import channel_send_message
from bot.utils.get_channel import get_chat_member

from ai import giga_chat

admin_router = Router()


@admin_router.message(F.text)
async def hello_message(message: types.Message):
    # await channel_send_message(channel_id="@oksi_test", text=giga_chat.send_prompt(
    #     message.text, giga_chat.get_access_token()))
    load = await message.answer("Ожидайте ответа...")
    await load.edit_text(giga_chat.send_prompt(message.text, giga_chat.get_access_token()))
