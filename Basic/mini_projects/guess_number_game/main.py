import random #https://docs.python.org/3/library/random.html

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}"))
        print(guess)
        if guess < random_number:
            print('Try again! this time higher!')
        elif guess > random_number:
            print('Try again! this time lower!')

    print('congrats! you have guessed the number correctly!')


    guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} to low (L), too high (H), or correct (C)?').lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! The computer guessed your number ({guess}) correctly!")
