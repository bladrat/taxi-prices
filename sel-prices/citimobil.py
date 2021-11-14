
import requests

def get_price():
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

    data = '{"method":"getprice","ver":"4.59.0","phone_os":"widget","os_version":"web mobile-web","locale":"ru","latitude":55.780914,"longitude":37.631883,"del_latitude":55.739529,"del_longitude":37.621865,"options":[],"payment_type":["cash"],"tariff_group":[2,4,13,7,5],"source":"O","hurry":1}'

    response = requests.post('https://widget.city-mobil.ru/c-api', headers=headers, data=data)

    print(response.text)
