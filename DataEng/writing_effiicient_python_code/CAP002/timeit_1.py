#%%
import numpy as np

times = %timeit -o rand_nums = np.random.rand(1000)

print('melhor tempo:', times.best)
print('pior tempo:', times.worst)
# %%
print(times.timings)
# %%
f_time = %timeit -o formal_dict = dict()
l_time = %timeit -o literal_dict = {}

diff = (f_time.average - l_time.average) * (10**9)
print(f'l_time é melhor que f_time por {diff} ns')
# %%
