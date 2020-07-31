import csv
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
#print(champion_list)

champion_page_list = []
for champion in champion_list:
    champion_page = f'https://lolcounter.com/champions/{champion}'
    champion_page_list.append(champion_page)
#print(champion_page_list)

with open('champion_counters.csv', mode='a') as champ_file:
        champ_file_writer = csv.writer(champ_file, dialect='excel')
        header = ['Champion', 'Weak Against (Counter)', 'Strong Against']
        champ_file_writer.writerow(header)

        iterator = 0
        for champion_link in champion_page_list:
            champion_page = req.get(champion_link)
            champion_soup = bs(champion_page.content, 'html.parser')
            weak_against = champion_soup.find('div', {'class': 'weak-block'})
            weak_list = []

            for weak in weak_against.findAll('div', {'class': 'name'}):
                weak_list.append(weak.text)
            strong_against = champion_soup.find('div', {'class': 'strong-block'})
            strong_list = []
            for strong in strong_against.findAll('div', {'class': 'name'}):
                strong_list.append(strong.text)
            row = [champion_list[iterator],weak_list,strong_list]
            champ_file_writer.writerow(row)
            iterator+=1
    