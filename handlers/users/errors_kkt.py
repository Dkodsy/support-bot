from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import errors_callback
from keyboards.inline.error_buttons import choice_model_kkt, popular_errors, back_to_model
from loader import dp


@dp.message_handler(text='Ошибки ККТ')
async def show_instructions_buttons(message: Message):
    await message.answer(text='Выберите номер ошибки\n'
                              'Если вы не нашли ошибку, то выберите по модели ККТ\n'
                              'Скорее всего вы найдете ошибку там\n', reply_markup=popular_errors)


# реагирование на нажатие кнопки "Выбор ошибки по модели ККТ"
@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='model'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Выберите необходимую модель ККТ', reply_markup=choice_model_kkt)


# реагирование на нажатие кнопки "НАЗАД" - возвращает нас к первоначальной клаве
@dp.callback_query_handler(text='back_to_popular_errors')
async def back_to_popular_err(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer('Выберите ошибку по номеру или по модели ККТ',
                              reply_markup=popular_errors)  # здесь это реализовано через тупой костыль "удалить
    # сообщение и прислать новое
    # TODO в будущем нужно будет переписать кнопки НАЗАД(ну и скорее всего все кнопки)"


# реагирование на нажатие кнопки АТОЛ
@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='atol'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Список ошибок с ссылками на статьи', reply_markup=back_to_model)


# реагирование на нажатие кнопки ЭВОТОР
@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='evotor'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Список ошибок с ссылками на статьи', reply_markup=back_to_model)


# реагирование на нажатие кнопки МТС
@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='mts'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Список ошибок с ссылками на статьи', reply_markup=back_to_model)


# реагирование на нажатие кнопки ШТРИХ ЭЛВЕС
@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='shtrix_elves'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Список ошибок с ссылками на статьи', reply_markup=back_to_model)


# реагирование на нажатие кнопки "НАЗАД" - возвращает нас к выбору модели ККТ
@dp.callback_query_handler(text='back_to_model')
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('Выберите необходимую модель ККТ',
                              reply_markup=choice_model_kkt)  # здесь это реализовано через тупой костыль "удалить
    # сообщение и прислать новое
    # TODO в будущем нужно будет переписать кнопки НАЗАД(ну и скорее всего все кнопки)"
