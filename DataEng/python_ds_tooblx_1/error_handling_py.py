#%%
def square_n(n):
    if n < 0:
        raise ValueError('"Number" must be non-negative')
    try:
        print(n**0.5)
    except TypeError:
        print('"Number" must be int or float')

square_n(16)
square_n(-9)
# %%
