from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import errors_callback
from keyboards.inline.error_buttons import error_type, choice_model_kkt
from loader import dp


@dp.message_handler(text='Ошибки ККТ')
async def show_instructions_buttons(message: Message):
    await message.answer('Выберите (не знаю что сюда дописать =) )', reply_markup=error_type)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='model'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Выберите необходимую модель ККТ', reply_markup=choice_model_kkt)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='popular'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')


@dp.callback_query_handler(text='back')
async def back(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('Ты нажал "НАЗАД"')
