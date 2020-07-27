import requests as req
from bs4 import BeautifulSoup as bs

URL = 'https://www.nerfplz.com/2019/11/tier-list-best-lol-champion-picks-tier.html'
page = req.get(URL)

soup = bs(page.content, 'html.parser')

buffs_nerfs = soup.find('div', {'class': 'sch2'})

print(buffs_nerfs.text)

#tier_html = soup.find(id='highlight-plugin')
#print(tier_html.prettify())

mid_lane = soup.find('tr', {'class': 'tiermid'}).findAll('td')
print("MID LANE GODS: " + mid_lane[1].text)

jungle = soup.find('tr', {'class': 'tierjungle'}).findAll('td')
print("JUNGLE GODS: " + jungle[1].text)

top_lane = soup.find('tr', {'class': 'tiertop'}).findAll('td')
print("TOP LANE GODS: " + top_lane[1].text)

adc = soup.find('tr', {'class': 'tieradc'}).findAll('td')
print("BOT LANE GODS: " + adc[1].text)

support = soup.find('tr', {'class': 'tiersupport'}).findAll('td')
print("SUPPORT GODS: " + support[1].text)

upcoming = soup.find('div', {'class': 'descText2'})
print(upcoming.text)