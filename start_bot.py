from aiogram import Bot, Dispatcher, types, executor
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет")

@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем я могу помочь?")

@dp.message_handler(text='привет')
async def hello(message:types.Message):
    await message.reply("Привет, как дела?")

@dp.message_handler(commands="test")
async def test(message:types.Message):
    await message.answer_location(0,0)
    await message.answer_photo("https://geeks.kg/back_media/geeks_jr/main_blocks/2023/10/26/89f1c32d-3f4b-48db-bd3f-0b93c84b8b39.png")
    await message.answer_dice()

executor.start_polling(dp)