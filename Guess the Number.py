from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(answer, guess, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if answer < guess:
        print('Too high.')
        return turns - 1
    elif answer > guess:
        print('Too low.')
        return turns - 1
    else:
        print(f'You got it! The answer was {answer}')

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    guess = 0

    turns = set_difficulty()

    while guess != answer:
        print(f'You have {turns} attempts remaining to guess the number')
        guess = int(input('Make a guess: '))
        turns = check_answer(answer=answer, guess=guess, turns=turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif answer != guess:
            print("Guess again.")

game()
