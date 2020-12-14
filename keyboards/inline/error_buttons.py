from aiogram.types import InlineKeyboardMarkup

from keyboards.inline.callback_datas import errors_callback

error_type = InlineKeyboardMarkup()  # клавиатура для выбора (распространненых ошибок или по компаниям ККТ)
common_error = InlineKeyboardMarkup(text='Популярные ошибки',
                                    callback_data=errors_callback.new(choice_kkt_err='popular'))
error_type.insert(common_error)

model_kkt = InlineKeyboardMarkup(text='Выбор по модели ККТ', callback_data=errors_callback.new(choice_kkt_err='model'))
error_type.insert(model_kkt)

choice_model_kkt = InlineKeyboardMarkup()  # клавиатура для выбора компании ККТ

atol = InlineKeyboardMarkup(text='АТОЛ', callback_data=errors_callback.new(choice_kkt_err='atol'))
choice_model_kkt.insert(atol)

evotor = InlineKeyboardMarkup(text='ЭВОТОР', callback_data=errors_callback.new(choice_kkt_err='evotor'))
choice_model_kkt.insert(evotor)

mts = InlineKeyboardMarkup(text='МТС', callback_data=errors_callback.new(choice_kkt_err='mts'))
choice_model_kkt.insert(mts)