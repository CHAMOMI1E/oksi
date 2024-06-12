from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.core.keyboards.admin import start_admin, edit_group, start_owner, pagination_kb
from bot.utils.channel_sender import channel_send_message
from bot.utils.get_channel import get_chat_member

from ai import giga_chat
from bot.utils.states import RequestCHAT

start_router = Router()


@start_router.message(CommandStart())
async def hello_message(message: types.Message):
    await message.answer(text='Здравствуйте. Я ваш персональный помошник "Окси". Чем я могу вам помочь?',
                         reply_markup=pagination_kb(router=start_router))


@start_router.callback_query(F.data == 'giga_chat')
async def req_for_chat(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите свой запрос:")
    await state.set_state(RequestCHAT.text)


@start_router.callback_query(F.data == 'giga_image')
async def req_for_image(call: types.CallbackQuery, state: FSMContext):
    await call.message.reply_photo()


@start_router.callback_query(F.data == 'edit_channel')
async def test(call: types.CallbackQuery):
    await call.message.answer('test', reply_markup=paginator())


@start_router.message(RequestCHAT.text)
async def chat_answer(message: types.Message, state: FSMContext):
    await state.clear()
    load = await message.answer("Ожидайте ответа...")
    await load.edit_text(await giga_chat.send_prompt(message.text, await giga_chat.get_access_token()))
