import urllib
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

URL = 'https://www.etsy.com/ru/shop/GlozisDecor/items'
ACCEPT_LANGUAGE = 'en=gb'

ua = UserAgent()
header = {'user-agent': ua.chrome, 'Accept-Language': ACCEPT_LANGUAGE}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, 'lxml')

for link in soup.find_all("a", class_="buyer-card"):
    print(link.get("href"))
