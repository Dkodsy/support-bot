from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import errors_callback

back = InlineKeyboardButton(text='НАЗАД', callback_data='back_to_type_error')  # кнопка "назад"

# клавиатура для выбора (распространненых ошибок или по компаниям ККТ)
error_type = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Найти ошибку по номеру',
                                 callback_data=errors_callback.new(choice_kkt_err='popular'))
        ],
        [
            InlineKeyboardButton(text='Выбор ошибки по модели ККТ',
                                 callback_data=errors_callback.new(choice_kkt_err='model'))
        ]
    ]
)

# клавиатура для выбора модели ККТ
choice_model_kkt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='АТОЛ', callback_data=errors_callback.new(choice_kkt_err='atol')),
            InlineKeyboardButton(text='ЭВОТОР', callback_data=errors_callback.new(choice_kkt_err='evotor')),
            InlineKeyboardButton(text='МТС', callback_data=errors_callback.new(choice_kkt_err='mts')),

        ],
        [
            back
        ]
    ]
)

# список распространненых ошибок
