#%%
# BUILT-IN FUNCTIONS
nums_list = list(range(0,11))

sqrd_nums = map(lambda x : x**2,nums_list)
print(list(sqrd_nums))

# %%
nums_list2 = [*range(1,13,2)]
print(nums_list2)

# %%
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Rewrite the for loop to use enumerate
indexed_names = []
for i, name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names)]
print(indexed_names_unpack)

# %%
import numpy as np

#%%
np_nums = np.array(range(2,6))
print(np_nums**2)

#%%
# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')