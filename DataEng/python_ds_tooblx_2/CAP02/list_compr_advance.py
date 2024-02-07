#%%
num_list = [num**2 for num in range(1,10) if num%2 == 0]
print(num_list)
# %%
num_list_2= [num_2**2 if num_2%2 ==0 else num_2 for num_2 in range(1,10)]
print(num_list_2)
# %%
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship = []
for member in fellowship:
    if len(member) >= 7:
        new_fellowship.append(member)
print(new_fellowship)
# %%
(num for num in range(10**1000000))
# %%
def sequence_n(n):
    i=0
    while i<n:
        yield i
        i+=1

rt= sequence_n(5)
print(list(rt))
for i in rt:
    print(i)
# %%
# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)
# %%