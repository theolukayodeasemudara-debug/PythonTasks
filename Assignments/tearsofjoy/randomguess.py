# 15. Guess the number game
# Generate a random number 1-100. Let the user guess until correct — print 'higher' or 'lower' as hints. Count attempts.
# Expected output: Guess: 50 -> lower / Guess: 25 -> higher / Guess: 37 -> correct! (3 attempts)

import random
count = 0

while True:
    ran_number = random.randrange(1,100)
    number = int(input("guess a number!: "))
    count+=1
    if number > ran_number:
        print('higher')
    elif number < ran_number:
        print('lower')
    elif number == ran_number:
        print(f"correct! ({count} attempts)")
    print(ran_number)
