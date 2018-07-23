# Dawei Huang
# 07/22/2018
# CAAP Computer Science Lab2

import random

rounds = 0
name = "x"
leaderboard = "Leaderboard for Game"
gamePlay = True
life = 3

def gameFunction ():
    while gamePlay == True:
        round0()
        round1()

def round0():
    print("Welcome to The Game\n")
    print(leaderboard +"\n")
    if ("start" == input("Please input 'start' to begin game!: ")):
        global name
        name = input("Please input your name: ")
    else:
        round0()
        
def round1():
    print("\n----------------------------------------\n")
    print("Welcome to Room 1")
    print("\n----------------------------------------\n")
    print("Instructions: The invading aliens have challenged you to a game of blackjack. In order to pass the game you must beat the entire alien team and the dealer. If you lose a game, you will lose one life. You will gain a life if you win and pass this level\n")
    game1 = True
    gamescreen = "Alien Dealer\t\talien1\t\talien2\t\talien3\t\t" + name
    round1 = 1
    dealer = 0
    alien1 = 0
    alien2 = 0
    alien3 = 0
    you = 0
    action = ""
    while game1 == True:
        print("\nThis is Round" + str(round1) + "\n")
        action = input("Type 'go' to receive card and 'fold' to fold")
        while action != "fold" or action != "go":
            action = input("Type 'go' to receive card and 'fold' to fold")
        if action == "go"
            a = random.randint(1, 13)
            a1 = random.randint(1, 13)
            a2 = random.randint(1, 13)
            a3 = random.randint(1, 13)
            b = random.randint(1, 13)
            gamescreen +="\n"+str(a)+"\t\t"+str(a1)+"\t\t"+str(a2)+"\t\t"+str(a3)+"\t\t"+str(b)
            dealer += a
            alien1 += a1
            alien2 += a2
            alien3 += a3
            you += b
            if dealer >
            
        
gameFunction()



