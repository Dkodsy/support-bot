from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import menu_cd


# клавиатура для выбора "ошибок ККТ"
async def main_error_menu():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='❗ Ресурс ФН менее 30 дней',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_resource_fn')),
                InlineKeyboardButton(text='❗️ОФД не ОТВЕЧАЕТ',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_ofd_do_not')),
            ],
            [
                InlineKeyboardButton(text='№210',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№210')),
                InlineKeyboardButton(text='№211',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№211')),
                InlineKeyboardButton(text='№217',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№217')),

            ],
            [
                InlineKeyboardButton(text='№218',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№218')),
                InlineKeyboardButton(text='№231',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№231')),
                InlineKeyboardButton(text='№234',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№234')),
            ],
            [
                InlineKeyboardButton(text='№235',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№235')),
                InlineKeyboardButton(text='№240',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№240')),
                InlineKeyboardButton(text='№244',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№244')),

            ],
            [
                InlineKeyboardButton(text='№3807',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№3807')),
                InlineKeyboardButton(text='№3924',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№3924')),
                InlineKeyboardButton(text='№3933',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='error_number_№3933')),
            ],
            [
                InlineKeyboardButton(text='Выбор ошибки по модели ККТ',
                                     callback_data=menu_cd.new(category='errors',
                                                               subcategory='model_kkt'))
            ],
        ],
        row_width=1
    )
    return markup


# клавиатура для выбора модели ККТ
async def choice_model_kkt():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='АТОЛ',
                                 callback_data=menu_cd.new(category='errors',
                                                           subcategory='atol')),
            InlineKeyboardButton(text='ЭВОТОР',
                                 callback_data=menu_cd.new(category='errors',
                                                           subcategory='evotor')),
        ],
        [
            InlineKeyboardButton(text='МТС/LiteBox',
                                 callback_data=menu_cd.new(category='errors',
                                                           subcategory='mts')),
            InlineKeyboardButton(text='ШТРИХ',
                                 callback_data=menu_cd.new(category='errors',
                                                           subcategory='shtrix_elves')),
        ],
        [
            InlineKeyboardButton(text='НАЗАД', callback_data=menu_cd.new(category='main_errors', subcategory='0'))
            # кнопка "назад к выбору ошибок"
        ]
    ]
    )
    return markup


async def back_to_main_error_menu():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='НАЗАД', callback_data=menu_cd.new(category='main_errors', subcategory='0'))
            # кнопка "назад к выбору ошибок"
        ]
    ])
    return markup


async def back_to_choice_model_kkt():
    # клавиатура для возврата к выбору модели
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='НАЗАД', callback_data=menu_cd.new(category='errors',
                                                                         subcategory='back_to_choice_model_kkt'))
            # кнопка "назад к выбору моделей ККТ"
        ]
    ]
    )
    return markup
