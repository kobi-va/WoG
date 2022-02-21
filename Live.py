import GuessGame
import MemoryGame
import CurrencyRouletteGame
import os

linux_home = (os.path.expanduser('~'))


# WoG Welcome message
def welcome(name):
    print(f"Hello {name}, and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    print()


# WoG Clear old score txt and start from 0
def clear_score():
    if os.name == "nt":
        os.system("del /F /Q score.txt")
    else:
        os.system(f"rm -f {linux_home}/WoG_Project/score.txt")


# Run the chosen game
def load_game():
    print("Please choose a game to play: \n1. Memory Game - a sequence of numbers will appear for 1 second and you "
          "have to guess it back.\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency "
          "Roulette - try and guess the value of a random amount of USD in ILS")

    choose = input("Write the number of your choice: ")
    while not choose.isdigit() or int(choose) > 3 or int(choose) == 0:
        choose = input("This is not a valid choice. please choose again: ")

    dif = input("Amazing choice! Now please choose the game difficulty from 1-5: ")
    while not dif.isdigit() or int(dif) > 5 or int(dif) == 0:
        dif = input("This is not a valid choice. please choose again: ")

    print()

    if int(choose) == 1:
        MemoryGame.play(dif)

    if int(choose) == 2:
        GuessGame.play(dif)

    if int(choose) == 3:
        CurrencyRouletteGame.play(dif)
