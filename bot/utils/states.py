from aiogram.fsm.state import StatesGroup, State


class RequestCHAT(StatesGroup):
    text = State()


class RequestIMAGE(StatesGroup):
    text = State()
