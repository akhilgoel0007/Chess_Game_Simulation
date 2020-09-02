from Functions.BasicFunc import *

def ValidateKingMove(PieceColor, CurrentSquare, DestinationSquare, Board):
	""" This Function Checks if the King Move is Valid or not.."""

	X_KingSquare =  int(CurrentSquare[1])-1 # Integer Coordinate
	Y_KingSquare = int(RowToNumber(CurrentSquare[0])) # Integer Coordinate

	for Y in range(Y_KingSquare-1, Y_KingSquare+2):
		for X in range(X_KingSquare-1, X_KingSquare+2):
			if Y >= 0 and Y <= 7 and X >= 0 and X <= 7:
				if DestinationSquare == (NumberToRow(Y) + str(X+1)):
					if Board[X][Y] is not PieceColor:
						Board[X_KingSquare][Y_KingSquare] = 'Free'
						Board[X][Y] = PieceColor
						return CurrentSquare

	# If No Square is Available For King..
	return None

def ValidateQueenMove(PieceColor, CurrentSquare, DestinationSquare, Board):
	""" This Function Checks if the Queen Move is Valid or not.."""

	X_QueenSquare = int(CurrentSquare[1])-1 # Integer Coordinate
	Y_QueenSquare = int(RowToNumber(CurrentSquare[0])) # Integer Coordinate

	# Check Left And Right
	for X in range(0, 8):
		if DestinationSquare == (NumberToRow(Y_QueenSquare) + str(X+1)):
			if Board[X][Y_QueenSquare] is not PieceColor:
				Board[X_QueenSquare][Y_QueenSquare] = 'Free'
				Board[X][Y_QueenSquare] = PieceColor
				return CurrentSquare

	# Check Up and Down
	for Y in range(0, 8):
		if DestinationSquare == (NumberToRow(Y) + str(X_QueenSquare+1)):
			if Board[X_QueenSquare][Y] is not PieceColor:
				Board[X_QueenSquare][Y_QueenSquare] = 'Free'
				Board[X_QueenSquare][Y] = PieceColor
				return CurrentSquare

	# Diagonal Up Right..
	for i in range(1, 8):
		if X_QueenSquare+i <= 7 and Y_QueenSquare+i <= 7:
			if DestinationSquare == (NumberToRow(str(Y_QueenSquare+i))+str(X_QueenSquare+i+1)):
				if Board[X_QueenSquare+i][Y_QueenSquare+i] is not PieceColor:
					Board[X_QueenSquare][Y_QueenSquare] = 'Free'
					Board[X_QueenSquare+i][Y_QueenSquare+i] = PieceColor
					return CurrentSquare
		else:
			break

	# Diagonal Up Left..		
	for i in range(1, 8):
		if X_QueenSquare+i <= 7 and Y_QueenSquare-i >= 0:
			if DestinationSquare == (NumberToRow(str(Y_QueenSquare-i))+str(X_QueenSquare+i+1)):
				if Board[X_QueenSquare+i][Y_QueenSquare-i] is not PieceColor:
					Board[X_QueenSquare][Y_QueenSquare] = 'Free'
					Board[X_QueenSquare+i][Y_QueenSquare-i] = PieceColor
					return CurrentSquare
		else:
			break
	
	# Diagonal Down Right..
	for i in range(1, 8):
		if X_QueenSquare-i >= 0 and Y_QueenSquare+i <= 7:
			if DestinationSquare == (NumberToRow(str(Y_QueenSquare+i))+str(X_QueenSquare-i+1)):
				if Board[X_QueenSquare-i][Y_QueenSquare+i] is not PieceColor:
					Board[X_QueenSquare][Y_QueenSquare] = 'Free'
					Board[X_QueenSquare-i][Y_QueenSquare+i] = PieceColor
					return CurrentSquare		
		else:
			break

	# Diagonal Down Left..
	for i in range(1, 8): 
		if X_QueenSquare-i >= 0 and Y_QueenSquare-i >= 0:
			if DestinationSquare == (NumberToRow(str(Y_QueenSquare-i))+str(X_QueenSquare-i+1)):
				if Board[X_QueenSquare-i][Y_QueenSquare-i] is not PieceColor:
					Board[X_QueenSquare][Y_QueenSquare] = 'Free'
					Board[X_QueenSquare-i][Y_QueenSquare-i] = PieceColor
					return CurrentSquare
		else:
			break

	# If Queen Can't go to that Square..
	return None 

def MoveKingAndQueen(ChessPiece, NewSquare, AllPieces, Board):
	""" Makes The King and Queen Move on the Board.. """
	
	if ChessPiece[5:] == 'King':
		return ValidateKingMove(ChessPiece[:5], AllPieces[ChessPiece][0]['CurrentSquare'], NewSquare, Board)

	elif ChessPiece[5:] == 'Queen':
		return ValidateQueenMove(ChessPiece[:5], AllPieces[ChessPiece][0]['CurrentSquare'], NewSquare, Board)