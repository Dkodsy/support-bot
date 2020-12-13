from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.inline.instruction_buttons import choice
from loader import dp


@dp.message_handler(text='Инструкции кассира')
async def show_instructions_buttons(message: Message):
    await message.answer('Выберите необходимую модель ККТ', reply_markup=choice)

