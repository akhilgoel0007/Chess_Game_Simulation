def RowToNumber(Row):
	Transform = {
		'a': '0',
		'b': '1',
		'c': '2',
		'd': '3',
		'e': '4',
		'f': '5',
		'g': '6',
		'h': '7' 
		}

	return Transform[Row]

# To be Rmoved
def Print(Board):
	print()
	for Row in Board:
		print(Row)
	print()

def NumberToRow(Number):

	Transform = {
		'0': 'a',
		'1': 'b',
		'2': 'c',
		'3': 'd',
		'4': 'e',
		'5': 'f',
		'6': 'g',
		'7': 'h',
		0: 'a',
		1: 'b',
		2: 'c',
		3: 'd',
		4: 'e',
		5: 'f',
		6: 'g',
		7: 'h',
		}
		
	return Transform[Number]

def UpdateVirtualBoard(ChessPieceColor, Board, Address, CurrentSquare):
	X_CurrentSquare = int(CurrentSquare[1])-1 # Integer Coordinate
	Y_CurrentSquare = int(RowToNumber(CurrentSquare[0])) # Integer Coordinate

	X_AddressSquare = int(Address[1])-1 # Integer Coordinate
	Y_AddressSquare = int(RowToNumber(Address[0])) # Integer Coordinate

	Board[X_AddressSquare][Y_AddressSquare][0] = 'Free'
	Board[X_AddressSquare][Y_AddressSquare][1] = False

	Board[X_CurrentSquare][Y_CurrentSquare][0] = ChessPieceColor
	Board[X_CurrentSquare][Y_CurrentSquare][1] = True