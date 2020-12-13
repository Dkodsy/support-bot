from aiogram.types import InlineKeyboardMarkup

from keyboards.inline.callback_datas import instructions_callback

choice = InlineKeyboardMarkup(row_width=2)

atol_with_buttons = InlineKeyboardMarkup(text='ККТ "АТОЛ(кнопочные)"',
                                         callback_data=instructions_callback.new(choice_kkt='atol_with_buttons'))
choice.insert(atol_with_buttons)

atol_sigma = InlineKeyboardMarkup(text='💰 "АТОЛ Sigma"',
                                  callback_data=instructions_callback.new(choice_kkt='atol_sigma'))
choice.insert(atol_sigma)

evotor = InlineKeyboardMarkup(text='ККТ "ЭВОТОР"',
                              callback_data=instructions_callback.new(choice_kkt='evotor'))
choice.insert(evotor)

shtrix_elves = InlineKeyboardMarkup(text='ККТ "ШТРИХ Элвес МФ"',
                                    callback_data=instructions_callback.new(choice_kkt='shtrix_elves'))
choice.insert(shtrix_elves)

mts = InlineKeyboardMarkup(text='ККТ "МТС"',
                           callback_data=instructions_callback.new(choice_kkt='mts'))
choice.insert(mts)

mercury = InlineKeyboardMarkup(text='ККТ "Меркурий"', callback_data=instructions_callback.new(choice_kkt='mercury'))
choice.insert(mercury)
