import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
from geopy.geocoders import Nominatim
import json
from requests.models import Response

from settings import API_TOKEN, CLID, APIKEY

import parser

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет, это бот для сравнения цен такси. Напиши место отправки в формате 'улица <название улицы> <номер дома> <город> и место куда нужно добраться через ';'. Должно выйти что-то такое 'улица Знаменка 12 Москва; улица Охотный Ряд 1 Москва'")
    print("start/help")
@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):

    print(msg.text)
    if ";" in msg.text:
        meessages = msg.text.split(';')

        prices = parser.get_all_prices(meessages[0], meessages[1])

        await msg.answer(prices[0])
        await msg.answer(prices[1])

        
        print(prices)
    else:
        await msg.answer("Вы написали адресса в неправильном формате, попробуйте снова.")
        await msg.answer('Должно выйти что-то похожее на это "улица Знаменка 12 Москва; улица Охотный Ряд 1 Москва"')
   

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)