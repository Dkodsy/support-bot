from aiogram.dispatcher.filters.state import StatesGroup, State


class Feedback(StatesGroup):
    Number = State()
    Question = State()
