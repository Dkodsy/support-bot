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
        [
            KeyboardButton(text='Заказать звонок')
        ]
    ],
    resize_keyboard=True,
)

cancel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️ Отмена')
        ]
    ],
    resize_keyboard=True
)
