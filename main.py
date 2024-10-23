# Katelyn Curtiss
# October 22 2024
# Random numbers


import random as rd
colors = ['purple', 'red', 'pink', 'navy']

# print(colors)

# randint ( ) method
start = 0
stop = 3
#rand_integer = rd.randint(start, stop)
rand_integer = rd.randrange(start, stop)

print(f'The random number is: {rand_integer}')
print(f'Randomly selected color = {colors[rand_integer]}')