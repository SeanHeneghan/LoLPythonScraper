import requests as req
from bs4 import BeautifulSoup as bs

URL = 'https://www.nerfplz.com/2019/11/tier-list-best-lol-champion-picks-tier.html'
page = req.get(URL)

soup = bs(page.content, 'html.parser')

buffs_nerfs = soup.find('div', {'class': 'sch2'})

print(buffs_nerfs.text)

tier_list = soup.find(id='highlight-plugin')
print(tier_list.prettify())