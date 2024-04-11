from aiogram import Bot, Dispatcher, types, executor
from config import token
import logging


bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Курсы'),
    types.KeyboardButton('Контакты'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Записаться')
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Привет {message.from_user.first_name}", reply_markup=start_keyboard)  
    await message.answer(f"{message}")

@dp.message_handler(text='О нас')
async def about(message:types.Message):
    await message.answer("Geeks - это айти курсы в Бишкеке, Такшкенте и Оше! Основана в 2019")

@dp.message_handler(text='Контакты')
async def contacts(message:types.Message):
    await message.answer_contact("0777121212", "Nurbolot", "Erkinbaev")
    await message.answer_contact("0555141516", "Ulan", "Ashirov")
    await message.answer_contact("+996 225 082021", "Geeks", "Admin")

@dp.message_handler(text='Адрес')
async def contacts(message:types.Message):
    await message.answer("Отправляю местоположение...")
    await message.answer_location(40.52, 72.8030)

courses_buttons = [
    types.KeyboardButton("Back-End"),
    types.KeyboardButton("Front-End"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("IOS"),
    types.KeyboardButton("UI/IX"),
    types.KeyboardButton("Назад")
]
courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_buttons)

@dp.message_handler(text='Back-End')
async def backend(message:types.Message):
    await message.answer("Кто такой разработчик backend? Он ответственен за «внутренние» процессы web-продуктов и выбирает системы для хранения, гарантирует максимальный уровень производительности при малом объеме сбоев. Бэкэнд разработчик продумывает построение логики для реализации разных задумок, «строит» фундамент и опорную систему для проекта — от простого сайта для магазина одежды до сложных вычислительных систем и нейронных сетей.")

@dp.message_handler(text='Front-End')
async def frontend(message:types.Message):
    await message.answer("Хотите стать Frontend разработчиком и зарабатывать до 25000 сомов в месяц уже во время обучения? Тогда добро пожаловать в нашу школу программирования Geeks! У нас не просто проверенная годами качественная методика, но и обучение перспективной, высокооплачиваемой IT профессии, а не просто языку программирования. С нами соберете портфолио, научитесь работать в команде и станете востребованным Фронтенд веб разработчиком, который сможет выполнять заказы удаленно для разных заказчиков из любой точки мира.")

@dp.message_handler(text='Android')
async def android(message:types.Message):
    await message.answer("Никому не секрет, что Android – это наиболее популярная и распространенная мобильная платформа в мире. Плюс в отличие от iOS, она используется на самых разнообразных устройствах.")

@dp.message_handler(text='IOS')
async def ios(message:types.Message):
    await message.answer("iOS-разработчик, или iOS developer, — это программист, который пишет сервисы и программы для айфонов. Из-за особенностей устройств Apple и их операционной системы для них нужно писать специальный код. Основной язык, на котором пишут код iOS-разработчики")

@dp.message_handler(text='Записаться')
async def uiux(message:types.Message):
    await message.answer("Записаться на наши курсы вы сможете написав нам в direct в instagram 'geeks_edu', 'geeks_osh', 'geeks_kb' или  'geeks_tashkent' в зависимости от города в котором находитесь ")

@dp.message_handler(text='Назад')
async def back(message:types.Message):
    await message.answer("Выход", reply_markup=start_keyboard)

@dp.message_handler(text='Курсы')
async def courses(message:types.Message):
    await message.answer("Наши курсы 👇", reply_markup=courses_keyboard)

@dp.message_handler(text='UI/IX')
async def uiux(message:types.Message):
    await message.answer("Задались вопросом, как стать UX/UI-дизайнером с нуля, тогда вы не зря находитесь на нашем сайте, здесь вы можете записаться на курсы UX/UI-design, научиться создавать дизайн веб-сайтов и мобильных приложений, освоить самый популярный сервис Figma и закреплять обретенные навыки на практике во время обучения.")

@dp.message_handler()
async def textnotfound(message:types.Message):
    await message.reply("Я вас не понял, введите комманду /start")


executor.start_polling(dp)