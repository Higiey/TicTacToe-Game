import random
from Functions import *
place1 = ""
place2 = ""
place3 = ""
place4 = ""
place5 = ""
place6 = ""
place7 = ""
place8 = ""
place9 = ""

player = 0

places = [place1, place2, place3, place4, place5, place6, place7, place8, place9]

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
        TwoPlayer(places, player)
        Winner(places)
