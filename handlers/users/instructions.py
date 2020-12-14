from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import instructions_callback
from keyboards.inline.instruction_buttons import choice_kkt
from loader import dp


@dp.message_handler(text='Инструкции кассира')
async def show_instructions_buttons(message: Message):
    await message.answer('Выберите необходимую модель ККТ', reply_markup=choice_kkt)


@dp.callback_query_handler(instructions_callback.filter(choice_kkt_instr='atol_with_buttons'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')


@dp.callback_query_handler(instructions_callback.filter(choice_kkt_instr='atol_sigma'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')


@dp.callback_query_handler(instructions_callback.filter(choice_kkt_instr='evotor'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')


@dp.callback_query_handler(instructions_callback.filter(choice_kkt_instr='shtrix_elves'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')


@dp.callback_query_handler(instructions_callback.filter(choice_kkt_instr='mts'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')


@dp.callback_query_handler(instructions_callback.filter(choice_kkt_instr='mercury'))
async def inst_atol_with_buttons(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='TEXT')
# TODO нужно красиво оформить ответ в виде статьи
