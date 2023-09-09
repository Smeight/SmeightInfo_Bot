import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

import admin
from admin import admins

import config
from config import TOKEN

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Путь к файлу с постом
post_file_path = 'post.txt'


# Команда /start для начала общения с ботом
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    await bot.send_message(admins["Илья"], f"Ботом воспользовался:\n"
                                      f"Кто: @{user.username}\n"
                                      f"Написал: '{message.text}'\n"
                                      f"Имя: {user.first_name}\n"
                                      f"Фамилия: {user.last_name}\n"
                                      f"ID чата: {message.chat.id}")
    await message.reply(
        f"Привет, {user.first_name}! Я бот, который поможет тебе узнать меня лучше. Что бы ты хотел узнать?",
        reply_markup=main_keyboard()
    )


# Команда /help для сообщения админу
@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    await message.reply(
        f"По любым вопросам с 10 до 22 ежедневно - @smeight",
        reply_markup=main_keyboard()
    )


# Команда /repository для ссылки на репозиторий бота
@dp.message_handler(commands=['repository'])
async def start(message: types.Message):
    user = message.from_user
    await message.reply(
        f"https://github.com/Smeight/SmeightInfo_Bot/blob/main/main.py",
        reply_markup=main_keyboard()
    )


# Функция для чтения текста из файла
def read_post_from_file():
    with open(post_file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Команда /post для отправки текста из файла
@dp.message_handler(commands=['post'])
async def send_post(message: types.Message):
    # Читаем текст из файла
    post = read_post_from_file()
    await message.reply(
        f"{post}",
        reply_markup=main_keyboard()
    )


# Клавиатура с основными функциями
def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    keyboard.add("1. Последнее селфи", "2. Фото из старшей школы")
    keyboard.add("3. Увлечение", "4. Войс: Про GPT")
    keyboard.add("5. Войс: SQL vs NoSQL", "6. Войс: Первая любовь")
    keyboard.add("7. Получить список команд")
    return keyboard


# Обработка запроса на отправку последнего селфи
@dp.message_handler(lambda message: message.text == "1. Последнее селфи")
async def send_selfie(message: types.Message):
    # Логика отправки последнего селфи
    await message.answer_photo(photo=open('selfie.jpg', 'rb'))
    await message.answer("Вот мое последнее селфи.", reply_markup=main_keyboard())


# Обработка запроса на отправку фото из старшей школы
@dp.message_handler(lambda message: message.text == "2. Фото из старшей школы")
async def send_school_photo(message: types.Message):
    # Логика отправки фото из школы
    await message.answer_photo(photo=open('school_photo.jpg', 'rb'))
    await message.answer("Вот мое фото из старшей школы.", reply_markup=main_keyboard())


# Обработка запроса на отправку информации о хобби
@dp.message_handler(lambda message: message.text == "3. Увлечение")
async def send_hobby_info(message: types.Message):
    # Рассказ про мое хобби
    await message.answer("Я люблю спорт, очень долго занимался футболом и хоккеем, но сейчас предпочитаю футбол и "
                         "баскетбол. Стараюсь как можно чаще выходить играть и развиваться в своем хобби. Мое рабочее "
                         "хобби - это программирование, я люблю изучать постоянно новые вещи и совершенствовать "
                         "свои навыки.", reply_markup=main_keyboard())


# Обработка запроса на отправку голосового сообщения GPT
@dp.message_handler(lambda message: message.text == "4. Войс: Про GPT")
async def send_gpt_voice(message: types.Message):
    # Логика отправки войса про GPT
    await message.answer_voice(voice=open('gpt_voice.ogg', 'rb'))
    await message.answer("Рассказываю про чат-gpt выше.", reply_markup=main_keyboard())


# Обработка запроса на отправку голосового сообщения о SQL vs NoSQL
@dp.message_handler(lambda message: message.text == "5. Войс: SQL vs NoSQL")
async def send_sql_vs_nosql_voice(message: types.Message):
    # Логика отправки войса про SQL
    await message.answer_voice(voice=open('sql_vs_nosql_voice.ogg', 'rb'))
    await message.answer("Вот голосовое сообщение о SQL vs NoSQL.", reply_markup=main_keyboard())


# Обработка запроса на отправку голосового сообщения о первой любви
@dp.message_handler(lambda message: message.text == "6. Войс: Первая любовь")
async def send_first_love_voice(message: types.Message):
    # Логика отправки войса про первую любовь
    await message.answer_voice(voice=open('first_love_voice.ogg', 'rb'))
    await message.answer("Вот голосовое сообщение о моей первой любви.", reply_markup=main_keyboard())


# Обработка запроса на получение списка команд
@dp.message_handler(lambda message: message.text == "7. Получить список команд")
async def send_commands(message: types.Message):
    # Список команд для общения с ботом
    commands = "Ссылка на репозиторий: /repository\n" \
              "Нашли проблемы в работе бота: /help\n" \
              "Мой последний пост в соц сети: /post"
    await message.answer(commands, reply_markup=main_keyboard())


# Функция запуска бота
def main():
    executor.start_polling(dp, skip_updates=False)


if __name__ == '__main__':
    main()
