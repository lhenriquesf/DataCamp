#%%
from random import randint
import time

numbers = [randint(-100, 100) for i in range(100000)]

start = time.perf_counter()
max_sum = float('-inf')
current_sum = 0

for num in numbers:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

# MAIS EFICIENTE
# for num in range(1,len(numbers)):
#     if current_sum + numbers[num] > numbers[num]:
#         current_sum += numbers[num]
#     else:
#         current_sum = numbers[num]

#     if current_sum > max_sum:
#         max_sum = current_sum

end = time.perf_counter()

print("Maior soma de subarray:", max_sum)
print("Tempo do algorítimo:", end-start)
# %%
x = lambda: 'xxx'
x()

# %%
matrix = [[y+1 for y in range(3)] for x in range(3)]
print(matrix)
# %%
