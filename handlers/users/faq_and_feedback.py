from aiogram.types import Message

from loader import dp


@dp.message_handler(text='FAQ Часто задаваемые вопросы')
async def show_faq(message: Message):
    await message.answer('Список статей с частозадаваемыми вопросам')
