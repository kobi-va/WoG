import random
import time

from score import add_score


# Generate number between 1 and user difficulty
def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


# Get Number from user and validate that it's numeric
def get_guess_from_user(difficulty):
    guess = input(f"Please guess a number between 1 to {difficulty}: ")
    while not guess.isdigit() or int(guess) < 1:
        guess = input(f"Please guess a valid number: ")

    return guess


# Compare between generated number to user choice
def compare_results(secret_number, user_guess):
    if int(user_guess) == int(secret_number):
        return True


def play(dif):
    print("Hi, and welcome to GuessGame!")
    secret = generate_number(int(dif))
    user_guess = get_guess_from_user(int(dif))
    if compare_results(secret, user_guess):
        print("You Win! you guessed the right number!")
        add_score(int(dif))
        time.sleep(2)
    else:
        print("You Lose :( you guessed the wrong number. maybe next time.")
