import numpy as np

height = np.round(np.random.normal(1.80,0.20,100),2)
weight = np.round(np.random.normal(70.32,15,100),2)

np_city = np.column_stack((height,weight))
#print(np_city)
np_mean = np.mean(np_city[:,1])
np_median = np.median(np_city[:,1])
np_corrcoef = np.corrcoef(np_city[:,0], np_city[:,1])
print(np.std(np_city[:,0]))


# height = np.array([[1.78, 1.881, 1.65, 1.50], 
# [77, 90, 80, 60]])

# print(height[0,:]) 

# weight = [77, 90, 80, 60]

# np_height = np.array(height)
# np_weight = np.array(weight)

# bmi = np_weight / (np_height**2)

# int_bmi = []

# for i in bmi:
#     i = round(i, 2)
#     int_bmi.append(i)
# print(bmi)
# print(int_bmi)
# print(bmi[bmi < 29])

