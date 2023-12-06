# %%
import numpy as np

fl = 'MNIST_test.txt'

data = np.loadtxt(fl, delimiter=',', skiprows=1)
data

# %%
import pandas as pd

file_nba = 'nba_per_game_processed.csv'

df = pd.read_csv(file_nba)
print(df.head())
# %%
