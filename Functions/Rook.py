from Functions.BasicFunc import *
from Functions.Decode import IsDigit

def RookAllowedToMove(Constant, Start, End, RankOrRow, AllPieces):
	"""Checks Whether The Rook is Allowed to move or Not."""

	RookCanMove = True
	Position = ""
	for i in range(Start, End):
			
		if RankOrRow == "Rank":
			Position = Constant + str(i)
		elif RankOrRow == "Row":
			Position = NumberToRow(str(i)) + Constant
			
		for Piece in AllPieces: # e.g. 'WhiteRook' -> Piece
			for PieceNum in AllPieces[Piece]: # PieceNum -> WhiteRook: List 
				if PieceNum['CurrentSquare'] == Position and PieceNum['IsInGame']:
					return not RookCanMove
	return RookCanMove

def MoveRook(ChessPiece, NewSquare, Action, AllPieces, Board):
	"""Moves Rook On the Board.."""

	if len(NewSquare) == 2 and str(type(NewSquare)) == "<class 'list'>":
		for Rook in AllPieces[ChessPiece]:
			if IsDigit(NewSquare[0]):
				if Rook['CurrentSquare'][1] == NewSquare[0]:
					Board[int(Rook['CurrentSquare'][1])-1][int(RowToNumber(Rook['CurrentSquare'][0]))] = 'Free'
					Board[int(NewSquare[1][1])-1][int(RowToNumber(NewSquare[1][0]))] = ChessPiece[:5]
					return Rook['CurrentSquare']
			else:
				if Rook['CurrentSquare'][0] == NewSquare[0]:
					Board[int(Rook['CurrentSquare'][1])-1][int(RowToNumber(Rook['CurrentSquare'][0]))] = 'Free'
					Board[int(NewSquare[1][1])-1][int(RowToNumber(NewSquare[1][0]))] = ChessPiece[:5]
					return Rook['CurrentSquare']
		return None

	FirstRook = [False]
	SecondRook = [False]
	RookNumber = 1

	for Rook in AllPieces[ChessPiece]:
		if not Rook['IsInGame']:
			RookNumber = RookNumber + 1
			continue

		X_RookSquare =  int(Rook['CurrentSquare'][1])-1 # Integer Coordinate
		Y_RookSquare = int(RowToNumber(Rook['CurrentSquare'][0])) # Integer Coordinate
		AvailableSquares = []

		for x in range(0, 8):
			if x != X_RookSquare:
				AvailableSquares.append((NumberToRow(str(Y_RookSquare))+str(x+1)))

		for y in range(0, 8):
			if y != Y_RookSquare:
				AvailableSquares.append((NumberToRow(str(y))+str(X_RookSquare+1)))
				
		if Action == "Move":
			if NewSquare in AvailableSquares and RookNumber == 1:
				RookAllowed = False
				if Rook['CurrentSquare'][0] == NewSquare[0]:
					if int(NewSquare[1]) > int(Rook['CurrentSquare'][1]):
						RookAllowed = RookAllowedToMove(Rook['CurrentSquare'][0], int(Rook['CurrentSquare'][1]) + 1, int(NewSquare[1]) + 1, "Rank", AllPieces)
					else:
						RookAllowed = RookAllowedToMove(Rook['CurrentSquare'][0], int(NewSquare[1]), int(Rook['CurrentSquare'][1]), "Rank", AllPieces)

				elif Rook['CurrentSquare'][1] == NewSquare[1]:
					if int(RowToNumber(NewSquare[0])) > int(RowToNumber(Rook['CurrentSquare'][0])):
						RookAllowed = RookAllowedToMove(Rook['CurrentSquare'][1], int(RowToNumber(Rook['CurrentSquare'][0])) + 1, int(RowToNumber(NewSquare[0]))+1, "Row", AllPieces)
					else:
						RookAllowed = RookAllowedToMove(Rook['CurrentSquare'][1], int(RowToNumber(NewSquare[0])), int(RowToNumber(Rook['CurrentSquare'][0])), "Row", AllPieces)

				if RookAllowed:
					Board[X_RookSquare][Y_RookSquare] = 'Free'
					Board[int(NewSquare[1])-1][int(RowToNumber(NewSquare[0]))] = ChessPiece[:5]
					return Rook['CurrentSquare']

			elif NewSquare in AvailableSquares and RookNumber == 2:
				RookAllowed = False
				
				if Rook['CurrentSquare'][0] == NewSquare[0]:
					if int(NewSquare[1]) > int(Rook['CurrentSquare'][1]):
						RookAllowed = RookAllowedToMove(Rook['CurrentSquare'][0], int(Rook['CurrentSquare'][1]) + 1, int(NewSquare[1]) + 1, "Rank", AllPieces)
					else:
						RookAllowed = RookAllowedToMove(Rook['CurrentSquare'][0], int(NewSquare[1]), int(Rook['CurrentSquare'][1]), "Rank", AllPieces)

				elif Rook['CurrentSquare'][1] == NewSquare[1]:
					if int(RowToNumber(NewSquare[0])) > int(RowToNumber(Rook['CurrentSquare'][0])):
						RookAllowed = RookAllowedToMove(Rook['CurrentSquare'][1], int(RowToNumber(Rook['CurrentSquare'][0])) + 1, int(RowToNumber(NewSquare[0]))+1, "Row", AllPieces)
					else:
						RookAllowed = RookAllowedToMove(Rook['CurrentSquare'][1], int(RowToNumber(NewSquare[0])), int(RowToNumber(Rook['CurrentSquare'][0])), "Row", AllPieces)

				if RookAllowed:
					Board[X_RookSquare][Y_RookSquare] = 'Free'
					Board[int(NewSquare[1])-1][int(RowToNumber(NewSquare[0]))] = ChessPiece[:5]
					return Rook['CurrentSquare']
		
		elif Action == "Capture":
			if NewSquare in AvailableSquares and RookNumber == 1:
				Board[X_RookSquare][Y_RookSquare] = 'Free'
				Board[int(NewSquare[1])-1][int(RowToNumber(NewSquare[0]))] = ChessPiece[:5]
				return Rook['CurrentSquare']
				
			elif NewSquare in AvailableSquares and RookNumber == 2:
				Board[X_RookSquare][Y_RookSquare] = 'Free'
				Board[int(NewSquare[1])-1][int(RowToNumber(NewSquare[0]))] = ChessPiece[:5]
				return Rook['CurrentSquare']
			
		RookNumber = RookNumber + 1

	return None