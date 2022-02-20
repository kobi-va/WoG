import os
from os import system


def score_file():
    scores_file_name = "score.txt"
    return scores_file_name


def screen_clear():
    if os.name == "nt":
        system("cls")
    else:
        system("clear")
