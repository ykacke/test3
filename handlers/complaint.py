from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

questions_router = Router()

class Questions(StatesGroup):
    name = State()
    complaint_details = State()
    phone_number = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

@questions_router.message(Command('complaint'))
async def complaint_details(message: types.Message, state: FSMContext):
    await message.answer("Здравствуйте! Как вас зовут?")
    await state.set_state(Questions.complaint_details)

@questions_router.message(Questions.complaint_details)
async def ask_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Пожалуйста, укажите ваш номер телефона.")
    await state.set_state(Questions.phone_number)

@questions_router.message(Questions.phone_number)
async def ask_food_rating(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("Какую оценку вы поставите нашей еде? (от 1 до 10)")
    await state.set_state(Questions.food_rating)

@questions_router.message(Questions.food_rating)
async def ask_cleanliness_rating(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or not (1 <= int(message.text) <= 10):
        await message.answer("Пожалуйста, введите число от 1 до 10.")
        return
    await state.update_data(food_rating=int(message.text))
    await message.answer("Как вы оцениваете чистоту заведения? (от 1 до 10)")
    await state.set_state(Questions.cleanliness_rating)

@questions_router.message(Questions.cleanliness_rating)
async def ask_extra_comments(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or not (1 <= int(message.text) <= 10):
        await message.answer("Пожалуйста, введите число от 1 до 10.")
        return
    await state.update_data(cleanliness_rating=int(message.text))
    await message.answer("Хотите оставить дополнительные комментарии или жалобу?")
    await state.set_state(Questions.extra_comments)

@questions_router.message(Questions.extra_comments)
async def finish_feedback(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    data = await state.get_data()
    await message.answer(
        f"Спасибо за ваш отзыв, {data['name']}!\n"
        f"Ваш номер: {data['phone_number']}\n"
        f"Оценка еды: {data['food_rating']}\n"
        f"Оценка чистоты: {data['cleanliness_rating']}\n"
        f"Ваши комментарии: {data['extra_comments']}"
    )
    await state.clear()
