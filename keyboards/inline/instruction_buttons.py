from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import menu_cd


async def instructions_buttons():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='ККТ "АТОЛ (кнопочные)"',
                                     callback_data=menu_cd.new(category='instructions',
                                                               subcategory='atol_with_buttons')),
            ],
            [
                InlineKeyboardButton(text='"АТОЛ Sigma"',
                                     callback_data=menu_cd.new(category='instructions', subcategory='atol_sigma')),
            ],
            [
                InlineKeyboardButton(text='ККТ "ЭВОТОР"',
                                     callback_data=menu_cd.new(category='instructions', subcategory='evotor')),
            ],
            [
                InlineKeyboardButton(text='ККТ "ШТРИХ"',
                                     callback_data=menu_cd.new(category='instructions', subcategory='shtrix_elves')),
            ],
            [
                InlineKeyboardButton(text='ККТ "МТС/LiteBox"',
                                     callback_data=menu_cd.new(category='instructions', subcategory='mts')),
            ],
            [
                InlineKeyboardButton(text='ККТ "Меркурий"',
                                     callback_data=menu_cd.new(category='instructions', subcategory='mercury'))
            ]
        ])
    return markup
