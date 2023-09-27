import numpy as np
np.random.seed(123)

moedas = []

for x in range(10):
    moeda = np.random.randint(0,2)
    if moeda == 0:
        moedas.append('cara')
    else:
        moedas.append('coroa')