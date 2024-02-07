#%%
import pandas as pd

df = pd.read_csv('../tweets.csv')
df_5 = df.head()

#%%
total=0
for c in pd.read_csv('../tweets.csv', chunksize=200):
    total += sum(c['x'])
print(total)