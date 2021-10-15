# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'https://giztech.gizumo-inc.work/lesson/18/220'
site = requests.get(url)
soup = BeautifulSoup(site.content, "html.parser")

for menber in soup.select('.bash'):
    print(menber)