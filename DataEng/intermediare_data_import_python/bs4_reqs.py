#%%
from bs4 import BeautifulSoup
import requests

#%%
url = 'https://www.crummy.com/software/BeautifulSoup'
req = requests.get(url)

#%%
html_doc = req.text
soup = BeautifulSoup(html_doc)

#%%
print(soup)
# %%
print(soup.title,'\n')
print(soup.get_text())
# %%
for link in soup.find_all('a'):
    print(link.get('href'))