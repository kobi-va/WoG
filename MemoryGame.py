import random
import time
from score import add_score
import Utils


# Generate random list
def generate_sequence(difficulty):
    random_list = random.sample(range(1, 101), difficulty)
    return random_list


# Get the list from the user and validate that it's numeric
def get_list_from_user(difficulty):
    print("Type the list numbers in the exact order:")
    user_list = []
    for i in range(1, difficulty + 1):
        item = input(f"Enter number at index {i}: ")
        while item.isalpha():
            item = input(f"Enter a valid number at index {i}: ")
        user_list.append(int(item))

    return user_list


# Compare between generated list to user's list
def is_list_equal(difficulty, generated_numbers):
    user_list = get_list_from_user(int(difficulty))
    if generated_numbers == user_list:
        return True
    else:
        return False


def play(dif):
    print("Hi, and welcome to MemoryGame!")
    time.sleep(1)
    print("Now, you will see a random list for 0.7 seconds. Try to remember it :)")
    time.sleep(6)
    generated_numbers = generate_sequence(int(dif))
    print(generated_numbers)
    time.sleep(0.7)
    Utils.screen_clear()
    print("Now it's your turn:")
    time.sleep(1)
    if is_list_equal(dif, generated_numbers) is True:
        print("You Won! you have an amazing memory!")
        add_score(int(dif))
        time.sleep(2)
    else:
        print("You lose :( maybe next time.")
