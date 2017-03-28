#'''
#This program should be able to predict where you are going to place an X and win most of the time
#	However this will be difficult as it will need to take into account where the past moves are and where future
#		moves will be, I will need to find a way to overcome this.
#	To do list:
#		Create the gui to show the board
#		Create a way to update the board with an 'x' ore 'o'
#
#
#
#

import random



print("Welcome to Tic Tac Toe")
game = input("Do you want to challenge the program to a game?").lower()

if game in ['yes','y']:
	True
	Gamemode = input("How many players?")
elif game in ['no','n']:
	print("Goodbye")

place1 = ''
place2 = ''
place3 = ''
place4 = ''
place5 = ''
place6 = ''
place7 = ''
place8 = ''
place9 = ''

#This is the game board
def gameGUI():

	print('-------------------------------------------------\n:\t\t:\t\t:\t\t:\n:\t',place1,'\t:\t',place2,'\t:\t',place3,'\t:\n:\t\t:\t\t:\t\t:')
	print('-------------------------------------------------\n:\t\t:\t\t:\t\t:\n:\t',place4,'\t:\t',place5,'\t:\t',place6,'\t:\n:\t\t:\t\t:\t\t:')
	print('-------------------------------------------------\n:\t\t:\t\t:\t\t:\n:\t',place7,'\t:\t',place8,'\t:\t',place9,'\t:\n:\t\t:\t\t:\t\t:')
	print('-------------------------------------------------')


#Check if a player has won.
#This needs to be redone as it doesn't work at all.
	#It says a player has won even when the line hasn't been completed with the same character
def Winner(input, player1,player2):
	if place1 and place2 and place3 in ['X'] or place4 and place5 and place6 in ['X'] or place7 and place8 and place9 in ['X'] or place1 and place4 and place7 in ['X'] or place2 and place5 and place8 in ['X'] or place3 and place6 and place9 in ['X'] or place1 and place5 and place9 in ['X'] or place3 and place5 and place7 in ['X']:
		return 1
	elif place1 and place2 and place3 in ['O'] or place4 and place5 and place6 in ['O'] or place7 and place8 and place9 in['O'] or place1 and place4 and place7 in ['O'] or place2 and place5 and place8 in ['O'] or place3 and place6 and place9 in ['O'] or place1 and place5 and place9 in ['O'] or place3 and place5 and place7 in ['O']:
		return 2
	else:
		return 0

#This was an attempt at starting the AI, It does not work as intended
	#Needs to be reworked
def First_move(place1,place2,place3,place4,place5,place6,place7,place8,place9):
	RandNum = random.randint(0,7)
	print('Random Numer = ',RandNum)
	if place1 in ['X']:
		if RandNum == 0:
			return 2
		elif RandNum == 1:
			return 3
		elif RandNum == 2:
			return 4
		elif RandNum == 3:
			return 5
		elif RandNum == 4:
			return 6
		elif RandNum == 5:
			return 7
		elif RandNum == 6:
			return 8
		elif RandNum == 7:
			return 9
		else:
			return 0
gameGUI()
while True:

#This works perfectly fine, it inputs a users go and inputs it into the gui
	if Gamemode in ['2','two']:
		turn = input("Where do you want to go player 1?")
		if turn in ['top left']:
			place1 = 'X'
		elif turn in ['top middle']:
			place2 = 'X'
		elif turn in ['top right']:
			place3 = 'X'
		elif turn in ['middle left']:
			place4 = 'X'
		elif turn in ['middle']:
			place5 = 'X'
		elif turn in ['middle right']:
			place6 = 'X'
		elif turn in ['bottom left']:
			place7 = 'X'
		elif turn in ['bottom middle']:
			place8 = 'X'
		elif turn in ['bottom right']:
			place9 = 'X'
		else:
			print("Wrong")
		gameGUI()
		#This doesn't work as the Winner() function doesn't work
		if Winner(0,'Player 1 WINS!!!!','PLayer 2 WINS!!!!')>0:
			if Winner(0,'Player 1 WINS!!!!','PLayer 2 WINS!!!!')==1:
				print('Player 1 Wins!!!!')
			elif Winner(0,'Player 1 WINS!!!!','PLayer 2 WINS!!!!')==2:
				print('Player 2 Wins!!!!')
			break
#This is the same as the X component, it works. but there may be a way to improve it.
		turn = input("Where do you want to go player 2?")
		if turn in ['top left']:
			place1 = 'O'
		elif turn in ['top middle']:
			place2 = 'O'
		elif turn in ['top right']:
			place3 = 'O'
		elif turn in ['middle left']:
			place4 = 'O'
		elif turn in ['middle']:
			place5 = 'O'
		elif turn in ['middle right']:
			place6 = 'O'
		elif turn in ['bottom left']:
			place7 = 'O'
		elif turn in ['bottom middle']:
			place8 = 'O'
		elif turn in ['bottom right']:
			place9 = 'O'
		else:
			print("Wrong")
		gameGUI()
		if Winner(0,'Player 1 WINS!!!!','PLayer 2 WINS!!!!')>0:
			if Winner(0,'Player 1 WINS!!!!','PLayer 2 WINS!!!!')==1:
				print('Player 1 Wins!!!!')
			elif Winner(0,'Player 1 WINS!!!!','PLayer 2 WINS!!!!')==2:
				print('Player 2 Wins!!!!')
			break


#This doesn't work, but I will keep it as a template and reminder.
	elif Gamemode in ['1','one']:


		turn = input('Where do you want to go?')
		if turn in ['top left']:
			place1 = 'X'
		elif turn in ['top middle']:
			place2 = 'X'
		elif turn in ['top right']:
			place3 = 'X'
		elif turn in ['middle left']:
			place4 = 'X'
		elif turn in ['middle']:
			place5 = 'X'
		elif turn in ['middle right']:
			place6 = 'X'
		elif turn in ['bottom left']:
			place7 = 'X'
		elif turn in ['bottom middle']:
			place8 = 'X'
		elif turn in ['bottom right']:
			place9 = 'X'
		else:
			print("Wrong")

		if First_move(place1,place2,place3,place4,place5,place6,place7,place8,place9) == 1:
			place1 = 'O'
		elif First_move(place1,place2,place3,place4,place5,place6,place7,place8,place9) == 2:
			place2 = 'O'
		elif First_move(place1,place2,place3,place4,place5,place6,place7,place8,place9) == 3:
			place3 = 'O'
		elif First_move(place1,place2,place3,place4,place5,place6,place7,place8,place9) == 4:
			place4 = 'O'
		elif First_move(place1,place2,place3,place4,place5,place6,place7,place8,place9) == 5:
			place5 = 'O'
		elif First_move(place1,place2,place3,place4,place5,place6,place7,place8,place9) == 6:
			place6 = 'O'
		elif First_move(place1,place2,place3,place4,place5,place6,place7,place8,place9) == 7:
			place7 = 'O'
		elif First_move(place1,place2,place3,place4,place5,place6,place7,place8,place9) == 8:
			place8 = 'O'
		elif First_move(place1,place2,place3,place4,place5,place6,place7,place8,place9) == 9:
			place9 = 'O'
		else:
			print('No')

		gameGUI()

		if Winner(0,'Player 1 WINS!!!!','PLayer 2 WINS!!!!')>0:
			if Winner(0,'Player 1 WINS!!!!','PLayer 2 WINS!!!!')==1:
				print('You win!!!!')
			elif Winner(0,'Player 1 WINS!!!!','PLayer 2 WINS!!!!')==2:
				print('The computer beat you!!!!')
			break






input("HEL")
