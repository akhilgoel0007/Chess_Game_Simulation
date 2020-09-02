from Functions.BasicFunc import *

# En-Passant Capture is Pending in this Code..
# Double Queen Promotion is Pending..

def MovePawn(ChessPiece, NewSquare, Action, AllPieces, Board):
	""" Makes The Pawn Move on the board."""

	if ChessPiece[:5] == 'White':
		for Pawn in AllPieces[ChessPiece]:
			if Action == 'Capture':
				if Pawn['CurrentSquare'][0] == NewSquare[0]:
					X_PawnSquare =  int(Pawn['CurrentSquare'][1])-1 # Integer Coordinate
					Y_PawnSquare = int(RowToNumber(Pawn['CurrentSquare'][0])) # Integer Coordinate

					# Right Piece Capture By Pawn..
					if Y_PawnSquare+1 <= 7:
						if Board[X_PawnSquare+1][Y_PawnSquare+1] == 'Black':
							if NewSquare[1] == (NumberToRow((str(Y_PawnSquare+1)))+str(X_PawnSquare+2)):
								Board[X_PawnSquare][Y_PawnSquare] = 'Free'
								Board[X_PawnSquare+1][Y_PawnSquare+1] = 'White'
								return Pawn['CurrentSquare'] 

					# Left Piece Capture By Pawn..
					if Y_PawnSquare-1 >= 0:
						if Board[X_PawnSquare+1][Y_PawnSquare-1] == 'Black':
							if NewSquare[1] == (NumberToRow((str(Y_PawnSquare-1)))+str(X_PawnSquare+2)):
								Board[X_PawnSquare][Y_PawnSquare] = 'Free'
								Board[X_PawnSquare+1][Y_PawnSquare-1] = 'White'
								return Pawn['CurrentSquare'] 

					# Remaining Pawn Capture by En-passant in this Code
			
			elif Action == 'Move':
				X_PawnSquare =  int(Pawn['CurrentSquare'][1])-1 # Integer Coordinate
				Y_PawnSquare = int(RowToNumber(Pawn['CurrentSquare'][0])) # Integer Coordinate
					
				if Board[X_PawnSquare+1][Y_PawnSquare] == 'Free':
					if NewSquare[0] == (NumberToRow(str(Y_PawnSquare))+str(X_PawnSquare+2)):
						Board[X_PawnSquare][Y_PawnSquare] = 'Free'
						Board[X_PawnSquare+1][Y_PawnSquare] = 'White'
						return Pawn['CurrentSquare']			
				
				if Pawn['CurrentSquare'] == Pawn['RealSquare']:
					if Board[X_PawnSquare+2][Y_PawnSquare] == 'Free':
						if NewSquare[0] == (NumberToRow(str(Y_PawnSquare))+str(X_PawnSquare+3)):
							Board[X_PawnSquare][Y_PawnSquare] = 'Free'
							Board[X_PawnSquare+2][Y_PawnSquare] = 'White'
							return Pawn['CurrentSquare']
		
		return None # If Both Pieces Don't Match..

	elif ChessPiece[:5] == 'Black':
		for Pawn in AllPieces[ChessPiece]:
			if Action == 'Capture':
				if Pawn['CurrentSquare'][0] == NewSquare[0]:
					X_PawnSquare =  int(Pawn['CurrentSquare'][1])-1 # Integer Coordinate
					Y_PawnSquare = int(RowToNumber(Pawn['CurrentSquare'][0])) # Integer Coordinate

					# Right Piece Capture By Pawn..
					if Y_PawnSquare+1 <= 7:
						if Board[X_PawnSquare-1][Y_PawnSquare+1] == 'White':
							if NewSquare[1] == (NumberToRow(str(Y_PawnSquare+1))+str(X_PawnSquare)):
								Board[X_PawnSquare][Y_PawnSquare] = 'Free'
								Board[X_PawnSquare-1][Y_PawnSquare+1] = 'Black'
								return Pawn['CurrentSquare']
				
					# Left Piece Capture By Pawn..
					if Y_PawnSquare-1 >= 0:
						if Board[X_PawnSquare-1][Y_PawnSquare-1] == 'White':
							if NewSquare[1] == (NumberToRow(str(Y_PawnSquare-1))+str(X_PawnSquare)):
								Board[X_PawnSquare][Y_PawnSquare] = 'Free'
								Board[X_PawnSquare-1][Y_PawnSquare-1] = 'Black'
								return Pawn['CurrentSquare']

					# Remaining Pawn Capture by En-passant in this Code
			
			elif Action == 'Move':
				X_PawnSquare =  int(Pawn['CurrentSquare'][1])-1 # Integer Coordinate
				Y_PawnSquare = int(RowToNumber(Pawn['CurrentSquare'][0])) # Integer Coordinate

				# Move One Step from any Square..
				if Board[X_PawnSquare-1][Y_PawnSquare] == 'Free':
					if NewSquare[0] == (NumberToRow(str(Y_PawnSquare))+str(X_PawnSquare)):
						Board[X_PawnSquare][Y_PawnSquare] = 'Free'
						Board[X_PawnSquare-1][Y_PawnSquare] = 'Black'
						return Pawn['CurrentSquare']
					
				# Move Two Steps is The Pawn is at the First Square..
				if Pawn['CurrentSquare'] == Pawn['RealSquare']:
					if Board[X_PawnSquare-2][Y_PawnSquare] == 'Free':
						if NewSquare[0] == (NumberToRow(str(Y_PawnSquare))+str(X_PawnSquare-1)):
							Board[X_PawnSquare][Y_PawnSquare] = 'Free'
							Board[X_PawnSquare-2][Y_PawnSquare] = 'Black'
							return Pawn['CurrentSquare']
		
		return None # If Both Pieces Don't Match..	