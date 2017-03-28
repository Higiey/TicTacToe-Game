
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
    selectedPlace = input("Where do you want to go player 1?")
    if player%2 = 0:
        PlyerId
    if selectedPlace in ["top left"] and places[0] != PlayerId:
        places[0] = "X"
        return places[0]
    elif selectedPlace in ["top middle"] and places[1] != "X":
        places[1] = "X"
        return places[1]
    elif selectedPlace in ["top left"] and places[2] != "X":
        places[2] = "X"
        return places[2]
    elif selectedPlace in ["middle left"] and places[3] != "X":
        places[3] = "X"
        return places[3]
    elif selectedPlace in ["middle"] and places[4] != "X":
        places[4] = "X"
        return places[4]
    elif selectedPlace in ["middle right"] and places[5] != "X":
        places[5] = "X"
        return places[5]
    elif selectedPlace in ["bottom left"] and places[6] != "X":
        places[6] = "X"
        return places[6]
    elif selectedPlace in ["bottom middle"] and places[7] != "X":
        places[7] = "X"
        return places[7]
    elif selectedPlace in ["bottom right"] and places[8] != "X":
        places[8] = "X"
        return places[8]
    else:
        print("Please try again, Invalid input")
