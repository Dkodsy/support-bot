from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from data.config import GROUP_ID
from keyboards.default.menu import cancel, menu
from loader import dp, bot
from states.feedback_state import Feedback


@dp.message_handler(text='FAQ Часто задаваемые вопросы')
async def show_faq(message: Message):
    await message.answer('Список статей с частозадаваемыми вопросам')


@dp.message_handler(text='Заказать звонок')
async def feedback(message: Message):
    await message.answer('Пожалуйста, напишите номер телефона, по которому мы можем с вами связаться.',
                         reply_markup=cancel)

    await Feedback.Number.set()


@dp.message_handler(text='⬅️ Отмена', state='*')
async def back_to_menu(message: Message, state: FSMContext):
    await message.answer('Вы отменили заявку', reply_markup=menu)
    await state.finish()


@dp.message_handler(state=Feedback.Number)
async def answer_number(message: Message, state: FSMContext):
    number = message.text

    await state.update_data(number=number)
    await message.answer('Пожалуйста, опишите свою проблему или вопрос, который хотите задать:', reply_markup=cancel)
    await Feedback.Question.set()


@dp.message_handler(state=Feedback.Question)
async def answer_question(message: Message, state: FSMContext):
    data = await state.get_data()
    number = data.get('number')
    question = message.text

    await message.answer('Ваша заявка уже передана специалисту, ждите звонка!', reply_markup=menu)
    await bot.send_message(chat_id=GROUP_ID, text=f'Нам оставили заявку!\n'
                                                  f'Номер - {number}\n'
                                                  f'Проблема - {question}')
    await state.finish()
