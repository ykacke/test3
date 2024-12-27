from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us"),
                types.InlineKeyboardButton(text="Пожертвовать", callback_data="donate"),
            ],
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://geeks.kg")
            ],
            [
                types.InlineKeyboardButton(text='Оставить отзыв', callback_data='review'),
                types.InlineKeyboardButton(text='Оставить жалобу', callback_data='complaint')
            ]
        ]
    )
    print(message.from_user.id)
    await message.answer(f"Привет, {name}", reply_markup=kb)


@start_router.message(F.text == "привет")
async def privet_handler(message: types.Message):
    await message.answer("Ну привет")


@start_router.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    print(callback.data)
    await callback.answer()
    await callback.message.answer("Текст о нас")


@start_router.callback_query(F.data == "donate")
async def donation_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Текст для сообщения о пожервовании")