import random
from Functions import *
from Ai import *

player = 0
places = ["","","","","","","","",""]

print("Welcome to the Tic-Tac-Toe game")
players = input("How many players are playing?")

if players in ["1", "one", "One"]:
    #This will be the AI part of the game
    while not WinnerAi(places):
        places = Ai(places)
        gameGUI(places)
        places = SinglePlayer(places)

elif players in ["2", "Two", "two"]:
    print("You have chosen two player game")
    while not Winner(places):
        player += 1
        gameGUI(places)
        places = TwoPlayer(places, player)
