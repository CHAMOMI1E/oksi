from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_widgets.pagination import KeyboardPaginator

from bot.core.kb_wrap import kb_wrap


@kb_wrap(keyboard_type='inline', adjust_keyboard=1)
def start_admin(builder: InlineKeyboardBuilder) -> InlineKeyboardMarkup:
    builder.button(text='Попробовать', callback_data='giga_chat')
    builder.button(text='Взаимодействие с правилами', callback_data='giga_rules')
    builder.button(text="Посмотреть историю использования токенов", callback_data="history_of_tokens")
    builder.button(text="test", callback_data='cancel')


def pagination_kb(router: Router):
    buttons = [
        InlinerKeyboardButton(text=f"Button {i}", callback_data=f"button_{i}")
        for i in range(1, 1000)
    ]
    paginator = KeyboardPaginator(
        router=router,
        data=buttons,
        per_page=20,
        per_row=2
    )
    return paginator.as_markup()
