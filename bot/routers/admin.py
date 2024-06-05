from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.core.keyboards.admin import start_admin
from bot.utils.channel_sender import channel_send_message
from bot.utils.get_channel import get_chat_member

from ai import giga_chat
from bot.utils.states import RequestCHAT

admin_router = Router()


@admin_router.message(CommandStart())
async def hello_message(message: types.Message):
    # await message.answer(f'{message}')
    await message.answer(text='Здравствуйте. Я ваш персональный помошник "Окси". Чем я могу вам помочь?',
                         reply_markup=start_admin())


@admin_router.callback_query(F.data == 'giga_chat')
async def req_for_chat(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите свой запрос:")
    await state.set_state(RequestCHAT.text)


@admin_router.message(RequestCHAT.text)
async def chat_answer(message: types.Message, state: FSMContext):
    await state.clear()
    load = await message.answer("Ожидайте ответа...")
    await load.edit_text(giga_chat.send_prompt(message.text, giga_chat.get_access_token()))
