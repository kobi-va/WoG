import time
import os

linux_home = (os.path.expanduser('~'))


def add_score(difficulty):
    difficulty == difficulty
    # Try to read from score.txt (If not found, create one)
    try:
        if os.name == "nt":
            file = open("score.txt", "r")
        else:
            file = open(f"{linux_home}/WoG_Project/score.txt", "r")
    except FileNotFoundError:
        if os.name == "nt":
            file = open("score.txt", "w+")
            time.sleep(1)
        else:
            file = open(f"{linux_home}/WoG_Project/score.txt", "w+")
            time.sleep(1)
    score = file.read()
    # update score in score.txt
    if score == "":
        if os.name == "nt":
            file = open("score.txt", "w+")
        else:
            file = open(f"{linux_home}/WoG_Project/score.txt", "w+")
        file.write(str(int(difficulty * 3) + 5))
    else:
        if os.name == "nt":
            file = open("score.txt", "w+")
        else:
            file = open(f"{linux_home}/WoG_Project/score.txt", "w+")
        file.write(str(int(difficulty * 3) + 5 + int(score)))
