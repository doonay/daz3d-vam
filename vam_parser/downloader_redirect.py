#!!! у патреона есть АПИ!!! почитать
#ходить через прокси

import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.patreon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': 'patreon_device_id=db7bdfe9-6cd0-481b-a00e-9f1faa453a15; patreon_location_country_code=LV; patreon_locale_code=ru-RU; __ssid=131fa835dd950b909fbc1b1e0d33b88; cf_clearance=DUR1mNbPE6l9NFMrM3Suw1mvXAnYyq3DvVOoPhdQMY4-1699300931-0-1-f03b0cde.f4acb9c3.a73a533e-250.0.0; can_see_nsfw=1; _ga_XX2BW2EM00=GS1.1.1700249272.1.1.1700249281.0.0.0; patreon_currency_pref=USD; a_csrf=DPrpEJpVlBkrOZbe9zbZXN_sN0vEJ5_gj76ge9Hw4Ug; analytics_session_id=99ad9409-4cbf-496f-8a21-c550c2f2492c; _gid=GA1.2.347035122.1700664100; __cf_bm=0m1wR8HwsQEhHyUBJrC22uQRX3mjt_8Wd3GG.E2NJiw-1700664470-0-AZ7GqfR5MyMa7PPBA+yTB8TS2WqR14kI/EH6CX/TwcKUFCq9n8bw74OEHY2H5yR8wSBbhd1yVz7dol+fZrjzWa43IXXwTOeV49VC50sB8meA; _ga=GA1.1.1048160682.1696929308; _ga_JF55G82FNT=GS1.1.1700662473.28.1.1700665600.0.0.0',
    'referer': 'https://apsolyamov.ru/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

def main(url):
    r = requests.get(url, headers=headers)
    print(r)
    '''
    soup = BeautifulSoup(r.text, 'lxml')
    print(soup)
    temp = soup.find('div', {'class':['sc-kLwhqv', 'iOmgq']})
    print(temp)
    '''
if __name__ == ('__main__'):
    url = 'https://www.patreon.com/posts/alien-android-by-92499880'
    url = 'https://www.patreon.com/posts/aeda-53715048'
    main(url)