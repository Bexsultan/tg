from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

import parser

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

characters = "Morty Smith, Rick Sanchez, Summer Smith, Jerry Smith, Squanchy, Beth Smith, Krombopulos Michael, Reverse Giraffe, Birdperson".split(", ")

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ могу показать тебе информацию о персонажах из мультика Рик и Морти! Чтобы увидеть введите /help")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("/get_characters - показать персонажей из Рик и Морти!")


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_button(callback_query: types.CallbackQuery):
    code = callback_query.data
    
    try:
        info = parser.get_character_data_by_name(code)

        await bot.send_message(callback_query.from_user.id, info)
    except:
        await bot.send_message(callback_query.from_user.id, "Персонаж не найден")

@dp.message_handler(commands=["get_characters"])
async def echo_message(msg: types.Message):
    inline_buttons = InlineKeyboardMarkup()
    for name in characters:
        inline_buttons.add(InlineKeyboardButton(name, callback_data=name))

    await bot.send_message(msg.from_user.id, f"Выберите один из персонажей", reply_markup=inline_buttons)


if __name__ == '__main__':
    executor.start_polling(dp)