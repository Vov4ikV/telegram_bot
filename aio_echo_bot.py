from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN
from scripts.get_weather import get_weather_spb
from scripts.get_vacancy_python import get_random_vacancy
from scripts.get_course_update import get_course

# токен вашего бота, полученный у @BotFather
API_TOKEN: str = BOT_TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')

# Этот хэндлер будет срабатывать на отправку боту фото
@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

# Этот хэндлер будет срабатывать на отправку боту стикера
@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)


# Home_work
@dp.message(Command(commands=['vacancy']))
async def get_vacancy(message: Message):
    await message.answer(get_random_vacancy())

@dp.message(Command(commands=['courses']))
async def get_course_command(message: Message):
    my_dict = get_course()
    string_zero = ""
    for item in my_dict.items():
        string_zero += f'{item[0]}: {item[1]} \n'
    await message.answer(string_zero)

@dp.message(Command(commands=['weather']))
async def get_weather_command(message: Message):
    weather = get_weather_spb()
    date = weather[0]
    night = f'\n\n {weather[1] ["weather_day"]}: {weather[1] ["temperature"]}, {weather[1] ["tooltip"]}, Влажность: {weather[1] ["weather-humidity"]} \n'
    day = f'\n {weather[2] ["weather_day"]}: {weather[2] ["temperature"]}, {weather[2] ["tooltip"]}, Влажность: {weather[2] ["weather-humidity"]} \n'
    evenin = f'\n {weather[3] ["weather_day"]}: {weather[3] ["temperature"]}, {weather[3] ["tooltip"]}, Влажность: {weather[3] ["weather-humidity"]} \n'
    await message.answer(date+night+day+evenin)

# Регистрируем хэндлеры
# dp.message.register(process_start_command, Command(commands=["start"]))
# dp.message.register(process_help_command, Command(commands=['help']))
# dp.message.register(send_photo_echo, F.photo)
# dp.message.register(send_sticker_echo, F.sticker)
# dp.message.register(send_echo)


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
# @dp.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text='Данный тип апдейтов не поддерживается '
#                                  'методом send_copy')


if __name__ == '__main__':
    dp.run_polling(bot)


# Этот хэндлер будет срабатывать на отправку боту любого сообщения
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)
