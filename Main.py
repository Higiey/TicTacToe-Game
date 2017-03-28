import random
from Functions import *

player = 0

places = ["","","","","","","","",""]

print("Welcome to the Tic-Tac-Toe game")

players = input("How many players are playing?")

if players in ["1", "one", "One"]:
    #This will be the AI part of the game
    print("This is a work in progress please choose 2 player")

elif players in ["2", "Two", "two"]:
    print("You have chosen two player game")
    while True:
        player += 1
        gameGUI(places)
        places = TwoPlayer(places, player)
        #Winner(places)
