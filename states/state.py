from aiogram.dispatcher.filters.state import StatesGroup, State


class FirstTest(StatesGroup):
    msg_list = State()
    name = State()


class AdminSpam(StatesGroup):
    msg_list = State()
    callback = State()
    text = State()
    video = State()
    photo = State()
    confirm = State()


class AdminAddPromo(StatesGroup):
    msg_list = State()
    probability = State()
    promocodes = State()
    confirm = State()
