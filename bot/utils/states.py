from aiogram.fsm.state import StatesGroup, State


class RequestCHAT(StatesGroup):
    text = State()
