#This is the ai part of the program,
#This will need to be able to do:
#   -Take in moves
#   -Work out where the best placce would be to go
#   -Place a move in that place
#   -Loop round with the program until it ends with a win or draw

def Ai(places):
    places[0] = "X"
    if places[1] in ["O"]:
        places[4] = "X"
        if places[2] or places[3] or places[5] or places[6] or place[7] in ["O"]:
            places[8] = "X"
        elif places[8] in ["O"]:
            places[6] = "X"
            if palces[2] or places[5] or places[7] in ["O"]:
                places[3] = "X"
            elif places[3] in ["O"]:
                places[2] = "X"
    elif places[2] in ["O"]:
        places[6] = "X"
        if places[1] or places[4] or places[5] or places[7] or places[8] in ["O"]:
            places[3] = "X"
        elif places[3] in ["O"]:
            places[8] = "X"
            if places[1] or places[4] or places[5] in ["O"]:
                places[7] = "X"
            elif places[7] in ["O"]:
                places[4] = "X"
    elif places[3] in ["O"]:
        places[4] = "X"
        if places[1] or place[2] or places[5] or places[6] or places[7] in ["O"]:
            places[8] = "X"
        elif places[7] in ["O"]:
            places[2] = "X"
            if places[5] or places[6] or places[7] in ["O"]:
                places[1] = "X"
            elif places[1] in ["O"]:
                places[6] = "X"
    elif places[4] in ["O"]:
        places[8] = "X"
        if places[1] in ["O"]:
            places[7] = "X"
            if places[2] or places[3] or palces[5] in ["O"]:
                places[6] = "X"
            elif places[6] in ["O"]:
                places[2] = "X"
                if places[3] in ["O"]:
                    places[5] = "X"
                elif places[5] in ["O"]:
                    places[3] = "X"
        elif places[2] in ["O"]:
            places[6] = "X"
            if places[1] or places[7] in ["O"]:
                places[3] = "X"
            elif places[3] or places[5]:
                places[7] = "X"
        elif places[3] in ["O"]:
            places[5] = "X"
            if palces[1] or places[6] or places[7] in ["O"]:
                places[2] = "X"
            elif places[2] in ["O"]:
                places[6] = "X"
                if places[1] in ["O"]:
                    places[7] = "X"
                elif places[7] in ["O"]:
                    places[1] = "X"
        elif places[5] in ["O"]:
            places[3] = "X"
            if places[1] or places[2] or places[7] in ["O"]:
                places[6] = "X"
            elif places[6] in ["O"]:
                places[2] = "X"
                if places[1] in ["O"]:
                    places[7] = "X"
                elif places[7] in ["O"]:
                    places[1] = "X"
        elif places[6] in ["O"]:
            places[2] = "X"
            if places[1] or places[7] in ["O"]:
                places[5] = "X"
            elif places[3] or places[5] in ["O"]:
                places[1] = "X"
        elif places[7] in ["O"]:
            places[1] = "X"
            if places[3] or places[5] or places[6] in ["O"]:
                places[2] = "X"
            elif places[2] in ["O"]:
                places[6] = "X"
                if places[3] in ["O"]:
                    places[5] = "X"
                elif places[5] in ["O"]:
                    places[3] = "X"
    elif places[5] in ["O"]:
        places[4] = "X"
        if places[1] or places[2] or places[3] or places[6] or places[7] in ["O"]:
            places[8] = "X"
        elif places[8] in ["O"]:
            places[2] = "X"
            if places[1] in ["O"]:
                places[6] = "X"
            elif places[3] or places[6] or places[7] in ["O"]:
                places[1] = "X"
    elif places[6] in ["O"]:
        places[2] = "X"
        if places[1] in ["O"]:
            places[8] = "X"
            if places[3] or places[4] or places[7] in ["O"]:
                places[5] = "X"
            elif places[5] in ["O"]:
                places[4] = "X"
        elif places[3] or places[4] or places[5] or places[7] or places[8] in ["O"]:
            places[1] = "X"
    elif places[7] in ["O"]:
        places[4] = "X"
        if places[1] or places[2] or places[3] or palces[5] or places[6] in ["O"]:
            places[8] = "X"
        elif places[8] in ["O"]:
            places[6] = "X"
            if places[1] or places[2] or palces[5] in ["O"]:
                places[3] = "X"
            elif palces[3] in ["O"]:
                places[2] = "X"
    elif places[8] in ["O"]:
        places[2] = "X"
        if places[3] or places[4] or places[5] or places[6] or places[7] in ["O"]:
            places[1] = "X"
        elif places[1] in ["O"]:
            places[6] = "X"
            if places[4] or places[5] or places[7] in ["O"]:
                places[3] = "X"
            elif places[3] in ["O"]:
                places[4] = "X"
    return places
