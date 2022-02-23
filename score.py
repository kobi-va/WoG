import os
import Utils

linux_home = (os.path.expanduser('~'))


def add_score(difficulty):
    difficulty == difficulty
    # Try to read from score.txt
    if os.name == "nt":
        if not os.path.isfile(Utils.score_file()):
            try:
                file = open(Utils.score_file(), "w+")
            finally:
                file.close()
    else:
        if not os.path.isfile(f"{linux_home}/WoG_Project/{Utils.score_file()}"):
            try:
                file = open(f"{linux_home}/WoG_Project/{Utils.score_file()}", "w+")
            finally:
                file.close()

    if os.name == "nt":
        with open(Utils.score_file(), "r+") as file:
            score = file.read()
            if score == "":
                with open(Utils.score_file(), "r+") as file:
                    file.write(str(int(difficulty * 3) + 5))
            else:
                with open(Utils.score_file(), "r+") as file:
                    file.write(str(int(difficulty * 3) + 5 + int(score)))
    else:
        with open(f"{linux_home}/WoG_Project/{Utils.score_file()}", "r+") as file:
            score = file.read()
            if score == "":
                with open(f"{linux_home}/WoG_Project/{Utils.score_file()}", "r+") as file:
                    file.write(str(int(difficulty * 3) + 5))
            else:
                with open(f"{linux_home}/WoG_Project/{Utils.score_file()}", "r+") as file:
                    file.write(str(int(difficulty * 3) + 5 + int(score)))
