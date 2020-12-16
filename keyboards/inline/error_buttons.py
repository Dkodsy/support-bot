from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import errors_callback

# список распространненых ошибок
popular_errors = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='№210', callback_data=errors_callback.new(choice_kkt_err='№210')),
            InlineKeyboardButton(text='№211', callback_data=errors_callback.new(choice_kkt_err='#211')),
            InlineKeyboardButton(text='№217', callback_data=errors_callback.new(choice_kkt_err='№217r')),
            InlineKeyboardButton(text='№218', callback_data=errors_callback.new(choice_kkt_err='№218')),
            InlineKeyboardButton(text='№231', callback_data=errors_callback.new(choice_kkt_err='№231')),
            InlineKeyboardButton(text='№234', callback_data=errors_callback.new(choice_kkt_err='№234')),

        ],
        [
            InlineKeyboardButton(text='№235', callback_data=errors_callback.new(choice_kkt_err='№235')),
            InlineKeyboardButton(text='№240', callback_data=errors_callback.new(choice_kkt_err='№240')),
            InlineKeyboardButton(text='№244', callback_data=errors_callback.new(choice_kkt_err='№244')),
            InlineKeyboardButton(text='№3807', callback_data=errors_callback.new(choice_kkt_err='№3807')),
            InlineKeyboardButton(text='№3924', callback_data=errors_callback.new(choice_kkt_err='№3924')),
            InlineKeyboardButton(text='№3933', callback_data=errors_callback.new(choice_kkt_err='№3933')),

        ],
        [
            InlineKeyboardButton(text='Выбор ошибки по модели ККТ',
                                 callback_data=errors_callback.new(choice_kkt_err='model'))
        ],
    ],
    row_width=1
)
back_to_popular_errors = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='НАЗАД', callback_data='back_to_popular_errors')  # кнопка "назад к выбору ошибок"
    ]
])

# клавиатура для выбора модели ККТ
choice_model_kkt = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='АТОЛ', callback_data=errors_callback.new(choice_kkt_err='atol')),
        InlineKeyboardButton(text='ЭВОТОР', callback_data=errors_callback.new(choice_kkt_err='evotor')),
    ],
    [
        InlineKeyboardButton(text='МТС', callback_data=errors_callback.new(choice_kkt_err='mts')),
        InlineKeyboardButton(text='ШТРИХ Элвес', callback_data=errors_callback.new(choice_kkt_err='shtrix_elves')),
    ],
    [
        InlineKeyboardButton(text='НАЗАД', callback_data='back_to_popular_errors')  # кнопка "назад к выбору ошибок"
    ]
]
)

# клавиатура для возврата к выбору модели
back_to_model = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='НАЗАД', callback_data='back_to_model')  # кнопка "назад к выбору моделей ККТ"
    ]
]
)
