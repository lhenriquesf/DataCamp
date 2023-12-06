#%%
filename = 'teste.txt'

with open(filename, 'r') as f:
    print(f.read())

print("Arquivo foi fechado?", f.closed)

#%%
'''
file = open(filename, mode='r')

text = file.read()
file.close()

print(text)
'''