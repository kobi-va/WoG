import time


def add_score(difficulty):
    difficulty == difficulty
    # Try to read from score.txt (If not found, create one)
    try:
        file = open("score.txt", "r")
    except FileNotFoundError:
        file = open("score.txt", "w+")
        time.sleep(1)
    score = file.read()
    # update score in score.txt
    if score == "":
        file = open("score.txt", "w+")
        file.write(str(int(difficulty * 3) + 5))
    else:
        file = open("score.txt", "w+")
        file.write(str(int(difficulty * 3) + 5 + int(score)))
