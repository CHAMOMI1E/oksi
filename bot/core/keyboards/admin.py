from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.core.decorators import kb_wrap


@kb_wrap(keyboard_type='inline', adjust_keyboard=1)
def start_admin(builder: InlineKeyboardBuilder) -> InlineKeyboardMarkup:
    builder.button(text='Попробовать', callback_data='giga_chat')
