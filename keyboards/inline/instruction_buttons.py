from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import instructions_callback

choice_kkt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='ККТ "АТОЛ(кнопочные)"',
                                 callback_data=instructions_callback.new(choice_kkt_instr='atol_with_buttons')),
            InlineKeyboardButton(text='💰 "АТОЛ Sigma"',
                                 callback_data=instructions_callback.new(choice_kkt_instr='atol_sigma')),

        ],
        [
            InlineKeyboardButton(text='ККТ "ЭВОТОР"',
                                 callback_data=instructions_callback.new(choice_kkt_instr='evotor')),
            InlineKeyboardButton(text='ККТ "ШТРИХ Элвес МФ"',
                                 callback_data=instructions_callback.new(choice_kkt_instr='shtrix_elves')),
        ],
        [
            InlineKeyboardButton(text='ККТ "МТС"',
                                 callback_data=instructions_callback.new(choice_kkt_instr='mts')),
            InlineKeyboardButton(text='ККТ "Меркурий"',
                                 callback_data=instructions_callback.new(choice_kkt_instr='mercury'))
        ]
    ])
