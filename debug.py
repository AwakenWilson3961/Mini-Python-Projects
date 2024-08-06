import time
import random

print('Welcome!')

time.sleep(1)

detect_Answer = input('Press 1 to start game 2 to exit: ')

while True:
    if detect_Answer == ('1'):
        print('Starting game...')
        time.sleep(1)
        secret_number = random.randint(1, 10)
        print('Guess a number between 1-10!')
        user_guess = int(input('Your guess: '))
        if user_guess == secret_number:
            print('Correct!')
        else:
            #print('Please try the numbers within range!')
            print('Better luck next time!')
            print('The correct number was: ' + str(secret_number))
        continue
    else:
        if detect_Answer == ('2'):
            print('Program terminated!')
        else:
            print('Not a valid input!')
            break
