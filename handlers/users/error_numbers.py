from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import menu_cd
from keyboards.inline.error_buttons import back_to_main_error_menu
from loader import dp


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№210'))
async def error_number_210(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№211'))
async def error_number_211(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№217'))
async def error_number_217(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№218'))
async def error_number_218(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№231'))
async def error_number_231(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№234'))
async def error_number_234(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№235'))
async def error_number_235(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№240'))
async def error_number_240(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№244'))
async def error_number_244(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№3807'))
async def error_number_3807(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№3924'))
async def error_number_3924(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='error_number_№3933'))
async def error_number_3933(call: CallbackQuery):
    markup = await back_to_main_error_menu()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Что это ошибка означает, бла бла бла', reply_markup=markup)
