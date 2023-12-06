
#%%
import json

#%%
file = 'BTC.json'
with open(file, 'r') as json_file:
    json_data = json.load(json_file)

for key, value in json_data.items():
    print(f'{key} : {value}')


# %%
import requests
#%%
# ID = tt3896198
url = 'http://www.omdbapi.com/?t=good+time&apikey=793b3397'
res = requests.get(url)

json_dt = res.json()

for k, v in json_dt.items():
    print(f'{k} : {v}')
#%%
