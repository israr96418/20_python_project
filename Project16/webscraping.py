# Web scarping also more interesting
import requests
from bs4 import BeautifulSoup
url = "https://www.codewithtomi.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2', {'class': 'post-title'})
print(title)
print(title[0].get_text())