from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import token
import logging, time, sqlite3


bot = Bot(token=token)
memory = MemoryStorage()
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect("internship.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER, 
                username VARCHAR(255),
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                created VARCHAR(255)
);
""")


cursor.execute("""CREATE TABLE IF NOT EXISTS internship(
                first_name VARCHAR(100),
                last_name VARCHAR(100),
                created VARCHAR(100)
);
""")

start_inline_buttons = [
    types.InlineKeyboardButton("Стажировка", callback_data='intership_callback'),
    types.InlineKeyboardButton("Наш сайт", url='https://geeks.kg/'),
    types.InlineKeyboardButton("Наш инстаграм", url='https://instagram.com/geeks_osh/'),
]
start_keyboard = types.InlineKeyboardMarkup().add(*start_inline_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    cursor.execute(f"SELECT id FROM users WHERE id = {message.from_user.id};")
    result = cursor.fetchall()
    print(result)    
    if result == []:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?);",
                    (message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name, time.ctime() ))
        cursor.connection.commit()
    await message.answer(f'привет, {message.from_user.full_name}', reply_markup=start_keyboard)


@dp.callback_query_handler(lambda call: call.data == "intership_callback")
async def internship_callback(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, "Отправьте свои данные (Имя Фамилия)")


@dp.message_handler()
async def process_name(message: types.Message, state: FSMContext):
    first_name, last_name = message.text.split(' ', 1)
    cursor.execute("INSERT INTO internship (first_name, last_name, created) VALUES (?, ?, ?);",
                   (first_name, last_name, time.ctime()))
    cursor.connection.commit()
    await message.answer("Ваши Данные успешно сохранены!")
    await bot.send_message(chat_id=(-1002002055590), text=f"Новая заявка на стажировку:\nИмя: {first_name}\nФамилия: {last_name}")

executor.start_polling(dp, skip_updates=True)