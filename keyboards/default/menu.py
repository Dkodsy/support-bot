from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Инструкции кассира'),
            KeyboardButton(text='Ошибки ККТ'),
        ],
        [
            KeyboardButton(text='FAQ Часто задаваемые вопросы')
        ],
    ],
    resize_keyboard=True,
)
