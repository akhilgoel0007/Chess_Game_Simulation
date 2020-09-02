from Functions.BasicFunc import *

def MoveBishop(ChessPiece, NewSquare, AllPieces, Board):
	""" Both Bishop's Cannot Collide at one Position, Both are of Different Colors.."""

	for Bishop in AllPieces[ChessPiece]:
		X_BishopSquare =  int(Bishop['CurrentSquare'][1])-1 # Integer Coordinate
		Y_BishopSquare = int(RowToNumber(Bishop['CurrentSquare'][0])) # Integer Coordinate

		# Diagonal Up Right..
		for i in range(1, 8):
			if X_BishopSquare+i <= 7 and Y_BishopSquare+i <= 7:
				if NewSquare == (NumberToRow(str(Y_BishopSquare+i))+str(X_BishopSquare+i+1)):
					if Board[X_BishopSquare+i][Y_BishopSquare+i] is not ChessPiece[:5]:
						Board[X_BishopSquare][Y_BishopSquare] = 'Free'
						Board[X_BishopSquare+i][Y_BishopSquare+i] = ChessPiece[:5]
						return Bishop['CurrentSquare']
			else:
				break

		# Diagonal Up Left..
		for i in range(1, 8): 
			if X_BishopSquare+i <= 7 and Y_BishopSquare-i >= 0:
				if NewSquare == (NumberToRow(str(Y_BishopSquare-i))+str(X_BishopSquare+i+1)):
					if Board[X_BishopSquare+i][Y_BishopSquare-i] is not ChessPiece[:5]:
						Board[X_BishopSquare][Y_BishopSquare] = 'Free'
						Board[X_BishopSquare+i][Y_BishopSquare-i] = ChessPiece[:5]
						return Bishop['CurrentSquare']
			else:
				break

		# Diagonal Down Right..
		for i in range(1, 8): 
			if X_BishopSquare-i >= 0 and Y_BishopSquare+i <= 7:
				if NewSquare == (NumberToRow(str(Y_BishopSquare+i))+str(X_BishopSquare-i+1)):
					if Board[X_BishopSquare-i][Y_BishopSquare+i] is not ChessPiece[:5]:
						Board[X_BishopSquare][Y_BishopSquare] = 'Free'
						Board[X_BishopSquare-i][Y_BishopSquare+i] = ChessPiece[:5]
						return Bishop['CurrentSquare']
			else:
				break
		
		# Diagonal Down Left..
		for i in range(1, 8):
			if X_BishopSquare-i >= 0 and Y_BishopSquare-i >= 0:
				if NewSquare == (NumberToRow(str(Y_BishopSquare-i))+str(X_BishopSquare-i+1)):
					if Board[X_BishopSquare-i][Y_BishopSquare-i] is not ChessPiece[:5]:
						Board[X_BishopSquare][Y_BishopSquare] = 'Free'
						Board[X_BishopSquare-i][Y_BishopSquare-i] = ChessPiece[:5]
						return Bishop['CurrentSquare']
			else:
				break

	# If Both Bishops Don't Match..
	return None