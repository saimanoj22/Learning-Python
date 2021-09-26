import random
import logging

# logging config message
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of Program')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

logging.debug('Tossing Coin...')

toss = random.randint(0, 1) # 0 is tails, 1 is heads

# since we enter heads/tails but toss is 0/1 we should convert them
if toss == 0:
    toss = 'tails'
if toss == 1:
    toss = 'heads'

logging.debug('Toss : ' + toss + ', Your Guess : ' + guess)

print(toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')