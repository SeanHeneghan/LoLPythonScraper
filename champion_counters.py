import requests as req
from bs4 import BeautifulSoup as bs

CHAMP_URL = 'https://lolcounter.com/champions'
page = req.get(CHAMP_URL)

soup = bs(page.content, 'html.parser')

all_champs = soup.find('div', {'class': 'champions'})
#print(all_champs)

champion_list = []
for div in soup.findAll('div', {'style': 'background: #000;opacity: .8;padding: 2px;text-align: center;position: relative;top: 67px; font-size: 13px;color: #FFF;'}):
    champion_list.append(div.text)