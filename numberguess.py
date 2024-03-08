"""Guess a number between 1 and 10"""

import random
guess = int(input( 'Guess a number between 1 and 10: '))
number = 0
count= 0
while guess != number:
    count += 1
    number = random.randrange(1,11)

    if guess == number:
        print(f'Yes! the number chosen is {number} in {count} tries')
    else:
        print(f'Nope! you guessed {guess} but the number was {number} ')