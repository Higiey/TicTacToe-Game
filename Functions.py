
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
    PlayerID = ""
    selectedPlace = input("Where do you want to go player 1?")
    if player%2 == 0:
        PlayerId = "O"
    elif player%2 != 0:
        PlayerId = "X"
    else:
        print("This didn't work")

    if selectedPlace in ["top left"] and places[0] == "":
        places[0] = PlayerId
        return places[0]
    elif selectedPlace in ["top middle"] and places[1] == "":
        places[1] = PlayerId
        return places[1]
    elif selectedPlace in ["top right"] and places[2] == "":
        places[2] = PlayerId
        return places[2]
    elif selectedPlace in ["middle left"] and places[3] == "":
        places[3] = PlayerId
        return places[3]
    elif selectedPlace in ["middle"] and places[4] == "":
        places[4] = PlayerId
        return places[4]
    elif selectedPlace in ["middle right"] and places[5] == "":
        places[5] = PlayerId
        return places[5]
    elif selectedPlace in ["bottom left"] and places[6] == "":
        places[6] = PlayerId
        return places[6]
    elif selectedPlace in ["bottom middle"] and places[7] == "":
        places[7] = PlayerId
        return places[7]
    elif selectedPlace in ["bottom right"] and places[8] == "":
        places[8] = PlayerId
        return places[8]
    else:
        print("Please try again, Invalid input")


#Find another way of doing this.
def Winner(places):
    if places[0] and places[1] and places[2] in ["X"]:
        print("You won player 1")
    elif places[3] and places[4] and palces[5] in ["X"]:
        print("You wone player 1")
    elif places[6] and places[7] and place[8] in ["X"]:
        print("Player 1 won")
    elif places[0] and places[4] and places[8] in ["X"]:
        print("Player 1 won")
    elif places[2] and places[4] and palces[6] in ["X"]:
        print("Player 1 won")
    elif places[1] and places[4] and places[7] in ["X"]:
        print("Player 1 won")
    elif places[0] and places[3] and places[6] in ["X"]:
        print("Player 1 won")
