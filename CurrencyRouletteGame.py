import random
import time
import requests
from score import add_score

# Get random number
random_number = random.randrange(1, 100)


# Get USD value with http request and create interval by user difficulty
def get_money_interval(difficulty, guess):
    d = difficulty
    response = requests.get("https://v6.exchangerate-api.com/v6/f1126a3e891ed1c75eefe849/latest/USD")
    res = response.json()
    t = float(res["conversion_rates"]["ILS"]) * random_number
    interval = (t - (5 - d), t + (5 - d))
    if guess < interval[0]:
        return False
    elif guess > interval[1]:
        return False
    else:
        return True


# Get number from user and validate that it's numeric
def get_guess_from_user():
    item = input(f"Guess the value of {random_number} USD in ILS: ")
    while item.isalpha():
        item = input(f"Enter a valid value: ")

    return float(item)


def play(dif):
    print("Hi, and welcome to CurrencyRouletteGame!")
    time.sleep(1)
    guess = get_guess_from_user()
    check_value = get_money_interval(int(dif), guess)
    if check_value:
        print("You won! Great guess!")
        add_score(int(dif))
        time.sleep(2)
    else:
        print("You lose :( maybe next time.")
