from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import errors_callback
from keyboards.inline.error_buttons import choice_model_kkt, popular_errors
from loader import dp


@dp.message_handler(text='Ошибки ККТ')
async def show_instructions_buttons(message: Message):
    await message.answer(text='Выберите номер ошибки\n'
                              'Если вы не нашли ошибку, то выберите по модели ККТ\n'
                              'Скорее всего вы найдете ошибку там\n', reply_markup=popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='model'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Выберите необходимую модель ККТ', reply_markup=choice_model_kkt)


@dp.callback_query_handler(text='back_error')
async def back(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer('Выберите ошибку по номеру или по модели ККТ',
                              reply_markup=popular_errors)  # здесь это реализовано через тупой костыль "удалить
    # сообщение и прислать новое
    # TODO в будущем нужно будет переписать эту кнопку(скорее всего кнопкИ)"
