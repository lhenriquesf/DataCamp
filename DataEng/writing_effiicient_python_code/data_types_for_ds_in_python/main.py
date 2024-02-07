# %%
lista = ['pop','smoke','bang','nade']

#%%
# List Comprehension
list_t = [i.title() for i in lista]
print(list_t)
#%%
print(list_t.get('pop'))
# %%
# Map with Lambda
list_t2 = map(lambda item: item.title(), lista)
print(list(list_t2))
# %%
idades = ['2','3','4','8']
print(f"As idades são {', '.join(idades[0:3])} e {idades[-1]}")
# %%
x = 'figado'.startswith('f')
print(x)
# %%
# Create an empty dictionary: squirrels_by_park
squirrels_by_park = dict()

# Loop over the squirrels list and unpack each tuple
for park, squirrel_details in squirrels:
    # Add each squirrel_details to the squirrels_by_park dictionary 
    squirrels_by_park[park] = squirrel_details
    
# Sort the squirrels_by_park dict alphabetically by park
for park in sorted(squirrels_by_park):
    # Print each park and its value in squirrels_by_park
    print(f'{park}: {squirrels_by_park[park]}')

#%%
print(f'{0.000010:.2f}')

# %%
notas = [2,3.4,5,6,6,2,3.4]
set_notas = set(notas)
print(len(set_notas))
# %%
set_notas.pop()
# %%
# Import defaultdict
from collections import defaultdict

# Create a defaultdict with a default type of list: male_penguin_weights
male_penguin_weights = defaultdict(list)

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Use the species as the key, and append the body_mass to it
    male_penguin_weights[species].append(body_mass)
    
# Print the first 2 items of the male_penguin_weights dictionary
print(list(male_penguin_weights.items())[:2])

#%%s
numbers = [5,6,-15,2,4,-1,12,-8]
min_value = float('-inf')

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        soma = 0
        for k in range(i, j+1):
            soma+=numbers[k]
        if soma > min_value:
            min_value = soma

print(min_value)
# %%
numbers = [5, 6, -15, 2, 4, -1, 12, -8]

max_sum = float('-inf')
current_sum = 0

for num in numbers:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print("Maior soma de subarray:", max_sum)