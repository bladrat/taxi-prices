import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
from geopy.geocoders import Nominatim
import json
from requests.models import Response

from settings import API_TOKEN, CLID, APIKEY

def get_kord(address):

    #Формат подачи "улица Мира 45 Тольятти"
    # улица [Название улицы] [Номер дома] [город]
    
    geolocator = Nominatim(user_agent = 'my_request')
    otkuda_loc = geolocator.geocode(address)
    #print(otkuda_loc)

    return otkuda_loc.latitude, otkuda_loc.longitude

def get_prices_citymobil(otkuda, kuda):
    #Формат подачи "улица Мира 45 Тольятти"
    # улица [Название улицы] [Номер дома] [город]
    otkuda = get_kord(otkuda)
    kuda = get_kord(kuda)
    headers = {
        'authority': 'widget.city-mobil.ru',
        'sec-ch-ua': '"Chromium";v="94", "Yandex";v="21", ";Not A Brand";v="99"',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.0.1996 Yowser/2.5 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://city-mobil.ru',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://city-mobil.ru/',
        'accept-language': 'ru,en;q=0.9',
    }
 
    data = '{"method":"getprice","ver":"4.59.0","phone_os":"widget","os_version":"web mobile-web","locale":"ru","latitude":' + str(otkuda[0]) + ',"longitude":'+ str(otkuda[1])+ ',"del_latitude":'+ str(kuda[0])+ ',"del_longitude":'+ str(kuda[1])+ ',"options":[],"payment_type":["cash"],"tariff_group":[2,4,13,7,5],"source":"O","hurry":1}'

    response = requests.post('https://widget.city-mobil.ru/c-api', headers=headers, data=data).text
    response_dict = json.loads(response)

    return response_dict["prices"][0]["price"]

def get_prices_yandex(otkuda, kuda):
    otkuda = get_kord(otkuda)[::-1]
    kuda = get_kord(kuda)[::-1]

    response = requests.get(f'https://taxi-routeinfo.taxi.yandex.net/taxi_info?rll={otkuda[0]},{otkuda[1]}~{kuda[0]},{kuda[1]}&clid={CLID}&apikey={APIKEY}').text
    response_dict = json.loads(response)

    return response_dict["options"][0]["price"]

def get_all_prices(otkuda, kuda):
    yandex = "Яндекс такси - " + str(get_prices_yandex(otkuda, kuda)) + " руб."
    citymobil = "Ситимобил - " + str(get_prices_citymobil(otkuda, kuda)) + " руб."
    return yandex, citymobil


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

        prices = get_all_prices(meessages[0], meessages[1])

        await msg.answer(prices[0])
        await msg.answer(prices[1])

        
        print(prices)
    else:
        await msg.answer("Вы написали адресса в неправильном формате, попробуйте снова.")
        await msg.answer('Должно выйти что-то похожее на это "улица Знаменка 12 Москва; улица Охотный Ряд 1 Москва"')
   

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)