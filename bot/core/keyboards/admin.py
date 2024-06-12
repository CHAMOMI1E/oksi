from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.formatting import Text
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_widgets.pagination import KeyboardPaginator

from bot.core.kb_wrap import kb_wrap


@kb_wrap(keyboard_type='inline', adjust_keyboard=1)
def start_admin(builder: InlineKeyboardBuilder) -> InlineKeyboardMarkup:
    builder.button(text='Попробовать', callback_data='giga_chat')
    builder.button(text='Картинка', callback_data='giga_image')


@kb_wrap(keyboard_type='inline', adjust_keyboard=1)
def start_owner(builder: InlineKeyboardBuilder) -> InlineKeyboardMarkup:
    builder.button(text="Добавить группу каналов", callback_data="add_channel")
    builder.button(text='Изменить группу каналов', callback_data='edit_channel')


@kb_wrap(keyboard_type='inline', adjust_keyboard=1)
def edit_group(builder: InlineKeyboardBuilder) -> InlineKeyboardMarkup:
    for group in range(10):
        builder.button(text=f'{group}', callback_data=f'edit_{group}')


def pagination_kb(router: Router):
    buttons = [
        InlineKeyboardButton(text=f"Button {i}", callback_data=f"button_{i}")
        for i in range(1, 1000)
    ]
    paginator = KeyboardPaginator(
        router=router,
        data=buttons,
        per_page=20,
        per_row=2
    )
    return paginator.as_markup()
