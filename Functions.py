
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
    else:
        print("This didn't work")

    Person = (int(player)%2)
    if Person == 1:
        Person = 1
        Person = 2
    elif Person == 0:


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
