import time
import os
from Live import load_game, welcome, clear_score
import Utils

# Get gamer name
your_name = input("Hi, What is your name?: ")
while not your_name.isalpha():
    your_name = input("Please write a valid name: ")

# Run welcome message
welcome(your_name)

# Remove old score txt file
if os.path.isfile('./score.txt'):
    clear_score()

# Run WoG
load_game()
print()

# Ask for retry
retry = input("Another game? (Y/N): ")
while retry == "Y":
    Utils.screen_clear()
    load_game()
    time.sleep(2)
    print()
    retry = input("Another game? (Y/N): ")
if retry == "N":
    print("Bye Bye!")
# Run Flask web app
    if os.path.isfile('./score.txt'):
        print("To see your total scores please visit http://localhost:1234/")

        if os.name == "nt":
            os.system("start /min python MainScores.py")
        else:
            os.system('python MainScores.py')
    time.sleep(30)
    exit()
else:
    time.sleep(4)
    exit()
