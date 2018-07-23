# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
import map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves = int(0)
name = ""
leaderboard = Leaderboard()


# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
    global name
    global moves
    score = Score(name, moves)
    if won:
        leaderboard.update(score)
    print("\nGame Over.")
    leaderboard.print_board()


# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
    while True:
        global name
        global moves
        print(
            "Welcome to Life of the Mind... it is your job to transverse the difficulties of social life at the "
            "University of Chicago, but how exactly will you do it??? To exit type :q at any point")
        name = input("\nLet's play. Enter your name. > ")
        if (name == ':q'):
            exit(1)

        difficulty = ""
        while True:
            difficulty = str(input("Which difficulty are you capable of: Noob (1), Intermediary Noob (2), or HardCore Noob (3)"))
            if int(difficulty) == 1 or difficulty == 2 or difficulty == 3:
                break
            else:
                print("Type in one of those options.")
        a_map = map('central_corridor')
        a_game = Engine(a_map)
        moves = a_game.play()
        game_over(a_game.won())

play_game()
