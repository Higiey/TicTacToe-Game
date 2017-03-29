
def gameGUI(places):
    print("-"*55)
    print("| {:^15} | {:^15} | {:^15} |".format("","",""))
    print("| {:^15} | {:^15} | {:^15} |"
          .format(places[0],places[1],places[2]))
    print("| {:^15} | {:^15} | {:^15} |".format("","",""))
    print("-"*55)
    print("| {:^15} | {:^15} | {:^15} |".format("","",""))
    print("| {:^15} | {:^15} | {:^15} |"
          .format(places[3],places[4],places[5]))
    print("| {:^15} | {:^15} | {:^15} |".format("","",""))
    print("-"*55)
    print("| {:^15} | {:^15} | {:^15} |".format("","",""))
    print("| {:^15} | {:^15} | {:^15} |"
          .format(places[6],places[7],places[8]))
    print("| {:^15} | {:^15} | {:^15} |".format("","",""))
    print("-"*55)

def TwoPlayer(places, player):
    PlayerId = ""
    if player%2 == 0:
        PlayerId = "O"
    elif player%2 != 0:
        PlayerId = "X"

    Person = (int(player)%2)
    if Person == 1:
        Person = 1
    elif Person == 0:
        Person = 2

    selectedPlace = input("Where do you want to go player " + str(Person) + "?")

    if selectedPlace in ["top left"] and places[0] == "":
        places[0] = PlayerId
    elif selectedPlace in ["top middle"] and places[1] == "":
        places[1] = PlayerId
    elif selectedPlace in ["top right"] and places[2] == "":
        places[2] = PlayerId
    elif selectedPlace in ["middle left"] and places[3] == "":
        places[3] = PlayerId
    elif selectedPlace in ["middle"] and places[4] == "":
        places[4] = PlayerId
    elif selectedPlace in ["middle right"] and places[5] == "":
        places[5] = PlayerId
    elif selectedPlace in ["bottom left"] and places[6] == "":
        places[6] = PlayerId
    elif selectedPlace in ["bottom middle"] and places[7] == "":
        places[7] = PlayerId
    elif selectedPlace in ["bottom right"] and places[8] == "":
        places[8] = PlayerId
    else:
        print("Please try again, Invalid input")
    return places

def SinglePlayer(places):
    selectedPlace = input("Where would to like to go? : ")
    if selectedPlace in ["top left"] and places[0] == "":
        places[0] = "O"
    elif selectedPlace in ["top middle"] and places[1] == "":
        places[1] = "O"
    elif selectedPlace in ["top right"] and places[2] == "":
        places[2] = "O"
    elif selectedPlace in ["middle left"] and places[3] == "":
        places[3] = "O"
    elif selectedPlace in ["middle"] and places[4] == "":
        places[4] = "O"
    elif selectedPlace in ["middle right"] and places[5] == "":
        places[5] = "O"
    elif selectedPlace in ["bottom left"] and places[6] == "":
        places[6] = "O"
    elif selectedPlace in ["bottom middle"] and places[7] == "":
        places[7] = "O"
    elif selectedPlace in ["bottom right"] and places[8] == "":
        places[8] = "O"
    else:
        print("Please try again, Invalid input")
    return places

def Winner(places):
    if places[0] == places[1] == places [2] == "O" or places[3] == places[4] == places[5] == "O" or places[6] == places[7] == places[8] == "O":
        print("Player 2 has won")
        return True
    elif places[0] == places[3] == places[6] == "O" or places[1] == places[4] == places[7] == "O" or places[2] == places[5] == places[8] == "O":
        print("Player 2 has won")
        return True
    elif places[0] == places[4] == places[8] == "O" or places[2] == places[4] == places[6] == "O":
        print("Player 2 has won")
        return True
    elif places[0] == places[1] == places [2] == "X" or places[3] == places[4] == places[5] == "X" or places[6] == places[7] == places[8] == "X":
        print("Player 1 has won")
        return True
    elif places[0] == places[3] == places[6] == "X" or places[1] == places[4] == places[7] == "X" or places[2] == places[5] == places[8] == "X":
        print("Player 1 has won")
        return True
    elif places[0] == places[4] == places[8] == "X" or places[2] == places[4] == places[6] == "X":
        print("Player 1 has won")
        return True
    elif "" not in places:
        print ("Tie")
        return True

def WinnerAi(places):
    if places[0] == places[1] == places [2] == "O" or places[3] == places[4] == places[5] == "O" or places[6] == places[7] == places[8] == "O":
        print("You have won")
        return True
    elif places[0] == places[3] == places[6] == "O" or places[1] == places[4] == places[7] == "O" or places[2] == places[5] == places[8] == "O":
        print("You have won")
        return True
    elif places[0] == places[4] == places[8] == "O" or places[2] == places[4] == places[6] == "O":
        print("You have won")
        return True
    elif places[0] == places[1] == places [2] == "X" or places[3] == places[4] == places[5] == "X" or places[6] == places[7] == places[8] == "X":
        print("The computer won")
        return True
    elif places[0] == places[3] == places[6] == "X" or places[1] == places[4] == places[7] == "X" or places[2] == places[5] == places[8] == "X":
        print("The computer won")
        return True
    elif places[0] == places[4] == places[8] == "X" or places[2] == places[4] == places[6] == "X":
        print("the computer won")
        return True
    elif "" not in places:
        print ("Tie")
        return True
