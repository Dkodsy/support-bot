from aiogram.types import InlineKeyboardMarkup

from keyboards.inline.callback_datas import errors_callback

choice_kkt_err = InlineKeyboardMarkup()

atol = InlineKeyboardMarkup(text='АТОЛ', callback_data=errors_callback.new(choice_kkt_err='atol'))
choice_kkt_err.insert(atol)

evotor = InlineKeyboardMarkup(text='ЭВОТОР', callback_data=errors_callback.new(choice_kkt_err='evotor'))
choice_kkt_err.insert(evotor)

mts = InlineKeyboardMarkup(text='МТС', callback_data=errors_callback.new(choice_kkt_err='mts'))
choice_kkt_err.insert(mts)
