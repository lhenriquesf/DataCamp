#%%
from urllib.request import urlretrieve, urlopen, Request
import pandas as pd
import requests

#%%
url1 = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
#urlretrieve(url, 'winequality-red.csv')

csv = pd.read_csv(url1, sep=';')
print(csv.head())


# %%
url2 = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls' 
xls = pd.read_excel(url2, sheet_name=None)

# Print the sheetnames to the shell
print(xls.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xls['1700'].head())

# %%
url3 = 'https://wikipedia.org/'

#%%
req = Request(url3)
res = urlopen(req)

html = res.read()
print(html)

res.close()
# %%
r = requests.get(url3)
text = r.text
# %%
