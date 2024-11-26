import art
import random
print(art.logo)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100")
easy_hard = input('Choose a difficulty, Type "easy" or "hard":').lower()

n_to_guess = random.randint(1,101)
n_of_guesses = 0
guess = ''
if easy_hard == 'easy':
    n_of_guesses += 10
    print(f'You have {n_of_guesses} attempts remaining to guess the number.')
    while guess != n_to_guess:
        guess = int(input('Make a guess:'))
        if guess > n_to_guess:
            print('Too high')
        elif guess < n_to_guess:
            print('Too low')
        elif guess == n_to_guess:
            print(f'Well done! The answer was {n_to_guess}.')
            exit()
        n_of_guesses -= 1
        print('Guess again.')
        if n_of_guesses >= 1:
            print(f'You have {n_of_guesses} attempts remaining to guess the number.')
        else:
            print('You ran out of guesses, refresh the page to try again.')
    else:
        print(f'Well done! The answer was {n_to_guess}.')
else:
    n_of_guesses += 5
    print(f'You have {n_of_guesses} attempts remaining to guess the number.')
    while guess != n_to_guess:
        guess = int(input('Make a guess:'))
        if guess > n_to_guess:
            print('Too high')
        elif guess < n_to_guess:
            print('Too low')
        elif guess == n_to_guess:
            print(f'Well done! The answer was {n_to_guess}.')
            exit()
        n_of_guesses -= 1
        print('Guess again.')
        if n_of_guesses >= 1:
            print(f'You have {n_of_guesses} guesses remaining.')
        else:
            print('You ran out of guesses, refresh the page to try again.')
            break


