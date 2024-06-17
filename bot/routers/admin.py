from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.core.keyboards.admin import start_admin, pagination_kb
from bot.utils.channel_sender import channel_send_message
from bot.utils.cheker import start_checker
from bot.utils.get_channel import get_chat_member

from ai import giga_chat
from bot.utils.states import RequestCHAT

start_router = Router()


@start_router.message(CommandStart())
async def hello_message(message: types.Message):
    await start_checker(message.from_user.id)
    await message.answer(text='Здравствуйте. Я ваш персональный помошник "Гига-чад". Чем я могу вам помочь?',
                         reply_markup=start_admin())


@start_router.callback_query(F.data == 'giga_chat')
async def req_for_chat(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите свой запрос:")
    await state.set_state(RequestCHAT.text)


@start_router.callback_query(F.data == 'giga_rules')
async def rules_request(call: types.CallbackQuery):
    await call.message.edit_text("Введите свой запрос:")


@start_router.callback_query(F.data == 'history_of_tokens')
async def history_of_tokens(call: types.CallbackQuery):
    await call.message.edit_text("Введите свой запрос:")


@start_router.message(RequestCHAT.text)
async def chat_answer(message: types.Message, state: FSMContext):
    await state.clear()
    load = await message.answer("Ожидайте ответа...")
    text = await giga_chat.send_prompt(message.text, await giga_chat.get_access_token())
    await load.edit_text(text)

