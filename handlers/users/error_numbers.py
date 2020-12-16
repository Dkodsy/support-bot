from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import errors_callback
from keyboards.inline.error_buttons import back_to_popular_errors
from loader import dp


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№210'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№211'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№217'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№218'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№231'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№234'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№235'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№240'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№244'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№3807'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№3924'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)


@dp.callback_query_handler(errors_callback.filter(choice_kkt_err='№3933'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=back_to_popular_errors)
