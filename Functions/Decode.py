import re as Regx

def CopyDictionary(Dictionary):
	CopiedDictionary = {}
	for UniquePiece in Dictionary: # PieceName
		EachPieceList = []
		for Piece in Dictionary[UniquePiece]: # Associated List, Piece is Dictionary
			Attributes = {}
			for PieceAttribute in Piece: # Keys in Piece
				if PieceAttribute != 'Label':
					Attributes[PieceAttribute] = Piece[PieceAttribute]
			EachPieceList.append(Attributes)
		CopiedDictionary[UniquePiece] = EachPieceList
	return CopiedDictionary

def IsDigit(Check):
	Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	IsNumber = True

	for Character in Check:
		if Character not in Digits:
			return not IsNumber
	return IsNumber

def RefineGameFile(OpenedGame):
	
	"""
		A) File Can Have Entries Other Than Chess Lines But Those Lines Should Start From '#'
		B) File Can Have Blank Lines
		C) Moves Should Start From Number 
			All of the below specified Formats can be used to Enter Moves in .txt File.
			-> For Example: 1. e4 e5
						 	1) e4 e5 or 1] e4 e5 or 1} e4 e5
						 	1 e4 e5
						 	1: e4 e5
						 	1> e4 e5
	"""

	RemoveCharacters = ['.', ')', '}', ']', ':', '>']
	Game = {}

	WhiteMoves = []
	BlackMoves = []

	if OpenedGame == None:
		return [False]
	else:
		for Move in OpenedGame:
			if Move == '\n': # Ignore Empty Lines
				continue
			else:
				for i in range(0, len(Move)):
					if Move[i] in RemoveCharacters:
						Move = Move[:i] + Move[(i+1):]
						break
				Move = Move.split()
				
				if IsDigit(Move[0]):
					if len(Move) == 2:
						WhiteMoves.append((int(Move[0]), Move[1]))
					elif len(Move) == 3:
						WhiteMoves.append((int(Move[0]), Move[1]))
						BlackMoves.append((int(Move[0]), Move[2]))
				else:
					continue
		
		Game['WhiteMoves'] = WhiteMoves 
		Game['BlackMoves'] = BlackMoves
		Game['NumberOfMoves'] = len(WhiteMoves) + len(BlackMoves)

		return Game

def GetMinorPiece(Side, Starting, MinorPieceDic):
	if Side == '1':
		ChessPieces = ['White' + MinorPieceDic[Starting]]
	elif Side == '2': 
		ChessPieces = ['Black' + MinorPieceDic[Starting]]

	return ChessPieces

def DecodeMove(ChessMove, Side):
	MinorPiece = {
		'K': 'King',
		'B': 'Bishop',
		'N': 'Knight',
		'R': 'Rook',
		'Q': 'Queen'
	}

	Symbols = {
			"!": "Good Move",
			"!!": "Brilliant Move",
			"!?": "Interesting Move",
			"?!": "Dubious Move",
			"?": "A Weak Move",
			"??": "Blunder",
			"+-": "White has a Decisive Advantage",
			"=": "Equal",
			"-+": "Black has a Decisive Advantage",
			"+": "Check",
			"#": "CheckMate",
			"(W+)": "White has Clear Advantage",
			"(W-)": "White has Slight Advantage",
			"(B+)": "Black has Clear Advantage",
			"(B-)": "Black has Slight Advantage",
			"<B>": "Black Won",
			"<W>": "White Won",
			"X": "Resigned",
			"C": "Continued",
			"S": "Stopped",
			"D": "Draw"
		}

	MiscCharacters = ['!', '?', '-', '+', '=', '#', '(', '<']
	
	Compliment = ""
	for i in range(0,len(ChessMove)):
		if ChessMove[i] in MiscCharacters:
			if ChessMove[i] == '=' and i != len(ChessMove)-1: # c6=Q
				continue
			if ChessMove[i] == '-' and ChessMove[i+1] == 'O':
				continue
				
			Compliment = Symbols[ChessMove[i:]]
			ChessMove = ChessMove[:i]
			break

	GameEnded = Regx.compile(r'[XCSD]')

	if GameEnded.search(ChessMove) != None:
		return [None, None, None, Symbols[ChessMove]]
	

	PawnMove = Regx.compile(r'^[abcdefgh]\d$') # b6
	PawnCapture = Regx.compile(r'^[abcdefgh]x[abcdefgh]\d$') # cxb6

	MinorPieceMove1 = Regx.compile(r'^[BKNRQ][abcdefgh]\d$') # Nd2
	MinorPieceMove2 = Regx.compile(r'^[BKNRQ][abcdefgh][abcdefgh]\d$') # Ned2
	MinorPieceMove3 = Regx.compile(r'^[BKNRQ]\d[abcdefgh]\d$') # N7d2

	MinorPieceCapture1 = Regx.compile(r'^[BKNRQ]x[abcdefgh]\d$') # Nxd2
	MinorPieceCapture2 = Regx.compile(r'^[BKNRQ][abcdefgh]x[abcdefgh]\d$') #Nbxd2
	MinorPieceCapture3 = Regx.compile(r'^[BKNRQ]\dx[abcdefgh]\d$') # N7xd2

	ShortCastling = Regx.compile(r'^O-O$')
	LongCastling = Regx.compile(r'^O-O-O$')

	QueenPromotion = Regx.compile(r'^[abcdefgh]\d=Q$') # c6=Q

	Pieces = None
	Action = None
	MovedSquare = None

	if PawnMove.search(ChessMove) != None: # b6
		Action = "Move"
		MovedSquare = [ChessMove]
		
		if Side == '1':
			Pieces = ['WhitePawn']
		elif Side == '2': 
			Pieces = ['BlackPawn']

	elif PawnCapture.search(ChessMove) != None: # cxb6
		Action = "Capture"
		MovedSquare = [ChessMove[0], ChessMove[2:]]
		
		if Side == '1':
			Pieces = ['WhitePawn']
		elif Side == '2': 
			Pieces = ['BlackPawn']

	elif MinorPieceMove1.search(ChessMove) != None: # Nd2
		Action = 'Move'
		MovedSquare = [ChessMove[1:]]
		Pieces = GetMinorPiece(Side, ChessMove[0], MinorPiece)

	elif MinorPieceMove2.search(ChessMove) != None: # Ned2
		Action = 'Move'
		MovedSquare = [ChessMove[1], ChessMove[2:]]
		Pieces = GetMinorPiece(Side, ChessMove[0], MinorPiece)
	
	elif MinorPieceMove3.search(ChessMove) != None: # N7d2
		Action = 'Move'
		MovedSquare = [ChessMove[1], ChessMove[2:]]
		Pieces = GetMinorPiece(Side, ChessMove[0], MinorPiece)
	
	elif MinorPieceCapture1.search(ChessMove) != None: # Nxd2
		Action = 'Capture'
		MovedSquare = [ChessMove[2:]]
		Pieces = GetMinorPiece(Side, ChessMove[0], MinorPiece)
	
	elif MinorPieceCapture2.search(ChessMove) != None: # Nbxd2
		Action = 'Capture'
		MovedSquare = [ChessMove[1], ChessMove[3:]]
		Pieces = GetMinorPiece(Side, ChessMove[0], MinorPiece)

	elif MinorPieceCapture3.search(ChessMove) != None: # N7xd2
		Action = 'Capture'
		MovedSquare = [ChessMove[1], ChessMove[3:]]
		Pieces = GetMinorPiece(Side, ChessMove[0], MinorPiece)
	
	elif QueenPromotion.search(ChessMove) != None:
		Action = "Promoted"
		MovedSquare = [ChessMove[:2]]
		Pieces = GetMinorPiece(Side, ChessMove[3], MinorPiece)
	
	elif ShortCastling.search(ChessMove) != None:
		Action = "Short-Castled"
		MovedSquare = ['e1', 'h1']
		
		if Side == '1':
			Pieces = ['WhiteKing', 'WhiteRook']
		elif Side == '2': 
			Pieces = ['BlackKing', 'BlackRook']

	elif LongCastling.search(ChessMove) != None:
		Action = "Long-Castled"
		MovedSquare = ['e1', 'a1']

		if Side == '1':
			Pieces = ['WhiteKing', 'WhiteRook']
		elif Side == '2': 
			Pieces = ['BlackKing', 'BlackRook']

	
	return [Pieces, Action, MovedSquare, Compliment]