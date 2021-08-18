# Coin FLip Streaks
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # list to trach heads or tails
    list = []
    for note in range(100):
        value = random.randint(0,1)
        if(value == 0):
            list.append('H')
        else:
            list.append('T')
    # check for streak of 6 heads or tails
    for check in range(95):
        if(list[check] == 'H' and list[check+1] == 'H' and list[check+2] == 'H' and list[check+3] == 'H' and list[check+4] == 'H' and list[check+5] == 'H'):
            numberOfStreaks += 1
        if(list[check] == 'T' and list[check+1] == 'T' and list[check+2] == 'T' and list[check+3] == 'T' and list[check+4] == 'T' and list[check+5] == 'T'):
            numberOfStreaks += 1

print('Number of Streaks :',numberOfStreaks)
print('Chance of Streak : %s%%'%(numberOfStreaks / 10000))
