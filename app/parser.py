import os

import requests
from bs4 import BeautifulSoup
import json

from config.settings import BASE_DIR

r = requests.get('https://seongwonhan88.github.io')

html = r.text
header = r.headers
status = r.status_code
is_ok = r.ok
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('h2 > a')

data = {}

for title in titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)