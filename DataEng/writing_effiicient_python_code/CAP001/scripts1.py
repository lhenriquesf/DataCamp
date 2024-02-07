#%%
#Non Pythonic
numbers = [1,2,3,4,5]
double_numbers = []

for i in range(len(numbers)):
    double_numbers.append(numbers[i]*2)
print(double_numbers)

# %%
#Pythonic
double_numbers_2 = [x*2 for x in numbers]

print(double_numbers_2)
# %%
