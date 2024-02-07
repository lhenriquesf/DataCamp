#%%
def raise_val(num):
    def inner(x):
        raised = x**num
        return raised
    return inner

square = raise_val(2)
cube = raise_val(3)

print(square(7), cube(6))
# %%
