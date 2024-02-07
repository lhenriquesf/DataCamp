#%%
nums = [12,8,21,3,16]
#%%
new_nums = [num+1 for num in nums]
print(new_nums)
# %%
new_nums=[]
for num in nums:
    new_nums.append(num+1)
print(new_nums)

# %%
pairs_1 = []
for num1 in range(0,2):
    for num2 in range(6,8):
        pairs_1.append((num1,num2))
print(pairs_1)
# %%
pairs_2 = [(num3,num4) for num3 in range(0,2) for num4 in range(6,8)]
print(pairs_2)
# %%
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]
print(matrix)
# Print the matrix
for row in matrix:
    print(row)

# %%
matrix = []
for r in range(5):
    new_r = []
    for c in range(5):
        new_r.append(c)
    matrix.append(new_r)

for row in matrix:
    print(row)
# %%
