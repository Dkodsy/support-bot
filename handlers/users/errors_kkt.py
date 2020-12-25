from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import menu_cd
from keyboards.inline.error_buttons import main_error_menu, choice_model_kkt, back_to_choice_model_kkt

from loader import dp


@dp.message_handler(text='Ошибки ККТ')
async def show_errors_main_menu(message: Message):
    markup = await main_error_menu()
    await message.answer(text='Выберите номер ошибки\n'
                              'Если вы не нашли ошибку, то выберите по модели ККТ\n'
                              'Скорее всего вы найдете ошибку там\n', reply_markup=markup)


# реагирование на нажатие кнопки "Выбор ошибки по модели ККТ"
@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='model_kkt'))
async def show_menu_choice_model_kkt(call: CallbackQuery):
    markup = await choice_model_kkt()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Выберите необходимую модель ККТ', reply_markup=markup)


# реагирование на нажатие кнопки АТОЛ
@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='atol'))
async def about_atol_errors(call: CallbackQuery):
    back_to_model = await back_to_choice_model_kkt()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Список ошибок с ссылками на статьи', reply_markup=back_to_model)


# реагирование на нажатие кнопки ЭВОТОР
@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='evotor'))
async def about_evotor_errors(call: CallbackQuery):
    back_to_model = await back_to_choice_model_kkt()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Список ошибок с ссылками на статьи', reply_markup=back_to_model)


# реагирование на нажатие кнопки МТС
@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='mts'))
async def about_mtc_errors(call: CallbackQuery):
    back_to_model = await back_to_choice_model_kkt()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Список ошибок с ссылками на статьи', reply_markup=back_to_model)


# реагирование на нажатие кнопки ШТРИХ ЭЛВЕС
@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='shtrix_elves'))
async def about_shtrix_errors(call: CallbackQuery):
    back_to_model = await back_to_choice_model_kkt()
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Список ошибок с ссылками на статьи', reply_markup=back_to_model)


# реагирование на нажатие кнопки "НАЗАД" - возвращает нас к первоначальной клаве
@dp.callback_query_handler(menu_cd.filter(category='main_errors'))
async def back_to_errors_main_menu(call: CallbackQuery):
    markup = await main_error_menu()
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer('Выберите ошибку по номеру или по модели ККТ',
                              reply_markup=markup)  # здесь это реализовано через тупой костыль "удалить
    # сообщение и прислать новое


# реагирование на нажатие кнопки "НАЗАД" - возвращает нас к выбору модели ККТ
@dp.callback_query_handler(menu_cd.filter(category='errors',
                                          subcategory='back_to_choice_model_kkt'))
async def back_to_model_kkt(call: CallbackQuery):
    markup = await choice_model_kkt()
    await call.message.delete()  # так же через костыль
    await call.message.answer('Выберите необходимую модель ККТ',
                              reply_markup=markup)
