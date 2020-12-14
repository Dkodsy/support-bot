from aiogram.types import InlineKeyboardMarkup

from keyboards.inline.callback_datas import instructions_callback

choice_kkt = InlineKeyboardMarkup(row_width=2)

atol_with_buttons = InlineKeyboardMarkup(text='ККТ "АТОЛ(кнопочные)"',
                                         callback_data=instructions_callback.new(choice_kkt_instr='atol_with_buttons'))
choice_kkt.insert(atol_with_buttons)

atol_sigma = InlineKeyboardMarkup(text='💰 "АТОЛ Sigma"',
                                  callback_data=instructions_callback.new(choice_kkt_instr='atol_sigma'))
choice_kkt.insert(atol_sigma)

evotor = InlineKeyboardMarkup(text='ККТ "ЭВОТОР"',
                              callback_data=instructions_callback.new(choice_kkt_instr='evotor'))
choice_kkt.insert(evotor)

shtrix_elves = InlineKeyboardMarkup(text='ККТ "ШТРИХ Элвес МФ"',
                                    callback_data=instructions_callback.new(choice_kkt_instr='shtrix_elves'))
choice_kkt.insert(shtrix_elves)

mts = InlineKeyboardMarkup(text='ККТ "МТС"',
                           callback_data=instructions_callback.new(choice_kkt_instr='mts'))
choice_kkt.insert(mts)

mercury = InlineKeyboardMarkup(text='ККТ "Меркурий"', callback_data=instructions_callback.new(choice_kkt_instr='mercury'))
choice_kkt.insert(mercury)
