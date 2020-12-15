from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import errors_callback

back = InlineKeyboardButton(text='НАЗАД', callback_data='back_error')  # кнопка "назад"

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
popular_errors = InlineKeyboardMarkup(  # ToDo Заполнить номера ошибок корректно(прописать колбэк дату)
    inline_keyboard=[
        [
            InlineKeyboardButton(text='№211', callback_data=errors_callback.new(choice_kkt_err='atol')),
            InlineKeyboardButton(text='№217', callback_data=errors_callback.new(choice_kkt_err='evotor')),
            InlineKeyboardButton(text='№218', callback_data=errors_callback.new(choice_kkt_err='mts')),
            InlineKeyboardButton(text='№231', callback_data=errors_callback.new(choice_kkt_err='atol')),
            InlineKeyboardButton(text='№234', callback_data=errors_callback.new(choice_kkt_err='evotor')),
            InlineKeyboardButton(text='№3807', callback_data=errors_callback.new(choice_kkt_err='atol')),

        ],
        [
            InlineKeyboardButton(text='№235', callback_data=errors_callback.new(choice_kkt_err='atol')),
            InlineKeyboardButton(text='№3933', callback_data=errors_callback.new(choice_kkt_err='atol')),
            InlineKeyboardButton(text='№3924', callback_data=errors_callback.new(choice_kkt_err='atol')),
            InlineKeyboardButton(text='№240', callback_data=errors_callback.new(choice_kkt_err='atol')),
            InlineKeyboardButton(text='№210', callback_data=errors_callback.new(choice_kkt_err='atol')),
            InlineKeyboardButton(text='№244', callback_data=errors_callback.new(choice_kkt_err='atol')),

        ],
        [
            InlineKeyboardButton(text='Выбор ошибки по модели ККТ',
                                 callback_data=errors_callback.new(choice_kkt_err='model'))
        ],
    ],
    row_width=1
)
