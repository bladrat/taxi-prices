import requests
from geopy.geocoders import Nominatim
import json
import ast


def get_prices(otkuda, kuda):
    #Формат подачи "улица Мира 45 Тольятти"
    # улица [Название улицы] [Номер дома] [город]
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

    return response_dict["prices"][0]["price"], response_dict["prices"][1]["price"]

 
def get_kord(address):
    geolocator = Nominatim(user_agent = 'my_request')
    otkuda_loc = geolocator.geocode(address)
    print(otkuda_loc)
    return otkuda_loc.latitude, otkuda_loc.longitude
 


a = get_prices(get_kord('улица Мира 45 Тольятти'), get_kord('улица Мира 101 Тольятти'))
print(a)
