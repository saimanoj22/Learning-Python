import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    list = []
    for note in range(100):
        value = random.randint(0,1)
        if(value == 0):
            list.append('H')
        else:
            list.append('T')

