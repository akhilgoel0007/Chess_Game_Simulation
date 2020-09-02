from Functions.BasicFunc import *
from Functions.Decode import IsDigit

def MoveKnight(ChessPiece, NewSquare, AllPieces, Board):
	""" Makes The Knight Move On The Board. """

	if len(NewSquare) == 2 and str(type(NewSquare)) == "<class 'list'>":
		for Knight in AllPieces[ChessPiece]:
			if IsDigit(NewSquare[0]):
				if Knight['CurrentSquare'][1] == NewSquare[0]:
					Board[int(Knight['CurrentSquare'][1])-1][int(RowToNumber(Knight['CurrentSquare'][0]))] = 'Free'
					Board[int(NewSquare[1][1])-1][int(RowToNumber(NewSquare[1][0]))] = ChessPiece[:5]

					return Knight['CurrentSquare']
			else:
				if Knight['CurrentSquare'][0] == NewSquare[0]:
					Board[int(Knight['CurrentSquare'][1])-1][int(RowToNumber(Knight['CurrentSquare'][0]))] = 'Free'
					Board[int(NewSquare[1][1])-1][int(RowToNumber(NewSquare[1][0]))] = ChessPiece[:5]

					return Knight['CurrentSquare']
		
		# If Both Knights Don't Match..
		return None

	for Knight in AllPieces[ChessPiece]:
		if not Knight['IsInGame']:
			continue

		X_KnightSquare =  int(Knight['CurrentSquare'][1])-1 # Integer Coordinate
		Y_KnightSquare = int(RowToNumber(Knight['CurrentSquare'][0])) # Integer Coordinate

		# Check Up Movement
		if X_KnightSquare+2 <= 7: 

			# Below Right
			if Y_KnightSquare+1 <= 7:
				if NewSquare == (NumberToRow(str(Y_KnightSquare+1))+str(X_KnightSquare+3)):
					if Board[X_KnightSquare+2][Y_KnightSquare+1] is not ChessPiece[:5]:
						Board[X_KnightSquare][Y_KnightSquare] = 'Free'
						Board[X_KnightSquare+2][Y_KnightSquare+1] = ChessPiece[:5]	
						return Knight['CurrentSquare']

			# Below Left
			if Y_KnightSquare-1 >= 0:  
				if NewSquare == (NumberToRow(str(Y_KnightSquare-1))+str(X_KnightSquare+3)):
					if Board[X_KnightSquare+2][Y_KnightSquare-1] is not ChessPiece[:5]:
						Board[X_KnightSquare][Y_KnightSquare] = 'Free'
						Board[X_KnightSquare+2][Y_KnightSquare-1] = ChessPiece[:5]
						return Knight['CurrentSquare']
		
		# Check Below Movement
		if X_KnightSquare-2 >= 0:

			# Below Right
			if Y_KnightSquare+1 <= 7:
				if NewSquare == (NumberToRow(str(Y_KnightSquare+1))+str(X_KnightSquare-1)):
					if Board[X_KnightSquare-2][Y_KnightSquare+1] is not ChessPiece[:5]:
						Board[X_KnightSquare][Y_KnightSquare] = 'Free'
						Board[X_KnightSquare-2][Y_KnightSquare+1] = ChessPiece[:5]
						return Knight['CurrentSquare']
		
			# Below Left
			if Y_KnightSquare-1 >= 0:  
				if NewSquare == (NumberToRow(str(Y_KnightSquare-1))+str(X_KnightSquare-1)):
					if Board[X_KnightSquare-2][Y_KnightSquare-1] is not ChessPiece[:5]:
						Board[X_KnightSquare][Y_KnightSquare] = 'Free'
						Board[X_KnightSquare-2][Y_KnightSquare-1] = ChessPiece[:5]
						return Knight['CurrentSquare']
			
		# Check Right Movement
		if Y_KnightSquare+2 <= 7: 
			
			# Right Up
			if X_KnightSquare+1 <= 7:
				if NewSquare == (NumberToRow(str(Y_KnightSquare+2))+str(X_KnightSquare+2)):
					if Board[X_KnightSquare+1][Y_KnightSquare+2] is not ChessPiece[:5]:
						Board[X_KnightSquare][Y_KnightSquare] = 'Free'
						Board[X_KnightSquare+1][Y_KnightSquare+2] = ChessPiece[:5]
						return Knight['CurrentSquare']
			
			# Right Below
			if X_KnightSquare-1 >= 0:  
				if NewSquare == (NumberToRow(str(Y_KnightSquare+2))+str(X_KnightSquare)):
					if Board[X_KnightSquare-1][Y_KnightSquare+2] is not ChessPiece[:5]:
						Board[X_KnightSquare][Y_KnightSquare] = 'Free'
						Board[X_KnightSquare-1][Y_KnightSquare+2] = ChessPiece[:5]
						return Knight['CurrentSquare']
			
		# Check Left Movement
		if Y_KnightSquare-2 >= 0: 

			#Left Up
			if X_KnightSquare+1 <= 7:
				if NewSquare == (NumberToRow(str(Y_KnightSquare-2)) + str(X_KnightSquare+2)):
					if Board[X_KnightSquare+1][Y_KnightSquare-2] is not ChessPiece[:5]:
						Board[X_KnightSquare][Y_KnightSquare] = 'Free'
						Board[X_KnightSquare+1][Y_KnightSquare-2] = ChessPiece[:5]
						return Knight['CurrentSquare']
			
			# Left Below
			if X_KnightSquare-1 >= 0:  
				if NewSquare == (NumberToRow(str(Y_KnightSquare-2))+str(X_KnightSquare)):
					if Board[X_KnightSquare-1][Y_KnightSquare-2] is not ChessPiece[:5]:
						Board[X_KnightSquare][Y_KnightSquare] = 'Free'
						Board[X_KnightSquare-1][Y_KnightSquare-2] = ChessPiece[:5]
						return Knight['CurrentSquare']

	# If Both Knights Don't Match..
	return None