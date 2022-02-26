import time
import os
from Live import load_game, welcome, clear_score
import Utils

linux_home = (os.path.expanduser('~'))

# Get gamer name
your_name = input("Hi, What is your name?: ")
while not your_name.isalpha():
    your_name = input("Please write a valid name: ")

# Run welcome message
welcome(your_name)

# Remove old score txt file
if os.name == "nt":
    if os.path.exists(f'./{Utils.score_file()}'):
        clear_score()
else:
    if os.path.exists(f'{linux_home}/WoG_Project/{Utils.score_file()}'):
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
    if os.name == "nt":
        if os.path.isfile(f'./{Utils.score_file()}'):
            print("To see your total scores please visit http://localhost:1234/")
            print()
            os.system("start /min python MainScores.py")
        else:
            time.sleep(30)
            exit()
    else:
        if os.path.isfile(f'{linux_home}/WoG_Project/{Utils.score_file()}'):
            print("To see your total scores please visit http://localhost:1234/")
            print()
            os.system('python3 ~/WoG_Project/MainScores.py')
        else:
            time.sleep(30)
            exit()
else:
    time.sleep(4)
    exit()
