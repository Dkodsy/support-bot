from aiogram.types import Message

from keyboards.inline.error_buttons import choice_kkt_err

from loader import dp


@dp.message_handler(text='Ошибки ККТ')
async def show_instructions_buttons(message: Message):
    await message.answer('Выберите необходимую модель ККТ', reply_markup=choice_kkt_err)
