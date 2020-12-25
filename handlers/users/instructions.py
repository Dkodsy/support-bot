from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import menu_cd
from keyboards.inline.instruction_buttons import instructions_buttons
from loader import dp


@dp.message_handler(text='Инструкции кассира')
async def show_instructions_buttons(message: Message):
    markup = await instructions_buttons()
    await message.answer('Выберите необходимую модель ККТ', reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter(category='instructions', subcategory='atol_with_buttons'))
async def atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')


@dp.callback_query_handler(menu_cd.filter(category='instructions', subcategory='atol_sigma'))
async def atol_sigma(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')


@dp.callback_query_handler(menu_cd.filter(category='instructions', subcategory='evotor'))
async def evotor(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')


@dp.callback_query_handler(menu_cd.filter(category='instructions', subcategory='shtrix_elves'))
async def shtrix_elves(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')


@dp.callback_query_handler(menu_cd.filter(category='instructions', subcategory='mts'))
async def mts(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')


@dp.callback_query_handler(menu_cd.filter(category='instructions', subcategory='mercury'))
async def mercury(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')
# TODO нужно красиво оформить ответ в виде статьи
