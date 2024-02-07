#%%
word = 'Data'
it = iter(word)
print(*it)
# %%
file = open('file.txt')
it = iter(file)
print(next(it))
# %%
small_value = iter(range(10))
print(list(small_value))
# %%
values = range(20)
print(values)
values_list = list(values)
print(values_list)
# %%
avengers = ['Hawkeye', 'Iron man', 'Thor', 'Quicksilver', 'Hulk']
names = ['Barton', 'Stark', 'Odinson', 'Maximoff', 'Banner']

z = zip(avengers, names)
print(*z)

#%%
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']
mutant_list = list(enumerate(mutants))

print(mutant_list)