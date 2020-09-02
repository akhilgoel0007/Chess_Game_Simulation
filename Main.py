import os as OperatingSystem
from tkinter import *
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
from tkinter import simpledialog as SimpleDialog
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk

# The Below Class is Imported from Storage Folder..
from Storage.ChangeSettings import *

# The Below Decode Module is Imported from Functions Folder..
from Functions.Decode import *
from Functions.Pawn import MovePawn
from Functions.Rook import MoveRook
from Functions.Bishop import MoveBishop
from Functions.Knight import MoveKnight
from Functions.KingAndQueen import MoveKingAndQueen

class MakeFolder(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.geometry("600x600+400+100")
		self.title("Add New Folder")
		self.resizable(False, False)

class Log(object):
	def __init__(self):
		self.__LogFile__ = []
		self.__SizeOfLog__ = 0
		self.__CurrentEntryNumber__ = 0 
		self.__Compliment__ = []

	def PushLog(self, LogEntry, Compliment):
		self.__LogFile__.append(LogEntry)
		self.__Compliment__.append(Compliment) # Saved Compliment

		self.__IncrementSize__()

	def GetLogEntry(self, LogEntryNumber):
		return self.__LogFile__[LogEntryNumber]

	def __IncrementSize__(self):
		self.__SizeOfLog__ += 1

	def NextMove(self):
		if self.__CurrentEntryNumber__ != (self.__SizeOfLog__-1):
			self.__CurrentEntryNumber__ += 1
			return self.__MakeMove__(self.__CurrentEntryNumber__)
		else:
			return "NotValid"

	def PreviousMove(self):
		if self.__CurrentEntryNumber__ != 0:
			self.__CurrentEntryNumber__ -= 1
			return self.__MakeMove__(self.__CurrentEntryNumber__)
		else:
			return "NotValid"

	def __MakeMove__(self, Index):
		CurrentDictionary = self.__LogFile__[Index]
		if CurrentDictionary is not None:
			for ChessPiece in CurrentDictionary:
				for i in range(0, len(CurrentDictionary[ChessPiece])):
					if CurrentDictionary[ChessPiece][i]['IsInGame']:
						self.__PieceCharacteristics__[ChessPiece][i]['Label'].configure(bg = self.__BoardSquares__[CurrentDictionary[ChessPiece][i]['CurrentSquare']]['Color'])
						self.__PieceCharacteristics__[ChessPiece][i]['Label'].grid(row=self.__BoardSquares__[CurrentDictionary[ChessPiece][i]['CurrentSquare']]['X'], column=self.__BoardSquares__[CurrentDictionary[ChessPiece][i]['CurrentSquare']]['Y'])
					else:
						self.__PieceCharacteristics__[ChessPiece][i]['Label'].grid_forget()

		if self.__Compliment__[Index] == "" or self.__Compliment__[Index] == None:
			return None
		else:
			return self.__Compliment__[Index]

	def EmptyLogFile(self):
		self.__LogFile__ = []
		self.__SizeOfLog__ = 0
		self.__CurrentEntryNumber__ = 0 
		self.__Compliment__ = []

	def SetBoardSquares(self, BoardSquares):
		self.__BoardSquares__ = BoardSquares
	
	def SetPieceAttributes(self, PieceAttributes):
		self.__PieceCharacteristics__ = PieceAttributes

	def GetCurrentLog(self):
		return self.__LogFile__[self.__CurrentEntryNumber__]

class ChessMenu:
	def __init__(self, App):
		self.__Application__ = App
		self.__Master__ = App.GetMaster()
		self.__MainMenu__ = Menu(self.__Master__)
		self.__Master__.configure(menu=self.__MainMenu__)
		self.CreateMenu()

	def CreateMenu(self):
		self.__CreateFileMenu__()
		self.__CreateEditMenu__()
		self.__CreateOptionsMenu__()

	def __CreateFileMenu__(self):
		FileMenu = Menu(self.__MainMenu__)
		self.__MainMenu__.add_cascade(label="File", menu=FileMenu)
		FileMenu.add_command(label="Add New Game", command=self.__Application__.AddNewGame) 
		FileMenu.add_command(label="Open Game", command=self.__Application__.OpenStoredGame)

	def __CreateEditMenu__(self):
		EditMenu = Menu(self.__MainMenu__)
		self.__MainMenu__.add_cascade(label="Edit", menu=EditMenu)
		
		EditMenu.add_command(label="Make New Folder", command=self.__MakeNewFolder__)

	def __CreateOptionsMenu__(self):
		OptionsMenu = Menu(self.__MainMenu__)
		self.__MainMenu__.add_cascade(label="Options", menu=OptionsMenu)
		
		# Make Color Option of Options Menu
		self.__MakeColorOption__(OptionsMenu) 

		
	def __MakeColorOption__(self, OptionsMenu):
		""" Making Color Option """

		BoardColors = Menu(OptionsMenu)
		OptionsMenu.add_cascade(label="Board Colors", menu=BoardColors)

		BoardColors.add_command(label="Change Color 1", command=self.__Application__.ChangeBoardColor1)
		BoardColors.add_command(label="Change Color 2", command=self.__Application__.ChangeBoardColor2)

	def __MakeNewFolder__(self):
		# NameOfFolder = SimpleDialog.askstring("New Folder", "Please Enter The Name Of Folder")
		# if NameOfFolder != None:
		Folder = MakeFolder()

class MakePieces:
	def __SetParameters__(self, Master, Pieces, PieceSpecs, Color1, Color2, TopFrame):
		self.__Master__ = Master
		self.__Pieces__ = Pieces
		self.__PieceSpecs__ = PieceSpecs
		self.__Color1__ = Color1
		self.__Color2__ = Color2
		self.__TopFrame__ = TopFrame

	def __SetPieces__(self):
		RowsWithPieces = [0, 1, 6, 7]
		Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		self.__PieceCharacteristics__ = {}
		self.__VirtualBoardTracker__ = []

		for i in range(0, 8):	
			
			Row = []
			for Square in range(0, 8):
				Row.append('Free')
			
			self.__VirtualBoardTracker__.append(Row)

		for x in RowsWithPieces:
			for y in range(0, 8):
				PieceAttributes = {}
				
				# The Block on which Our Piece is Placed
				PieceAttributes['CurrentSquare'] = Alphabets[y] + str((8-x))
				PieceAttributes['RealSquare'] = Alphabets[y] + str((8-x)) # Rook at 'a1' -> 'a1'
				PieceAttributes['IsInGame'] = True
				PieceAttributes['X'] = x
				PieceAttributes['Y'] = y
				
				CurrentPiece = ""
				
				if x == 0: # H row
					self.__VirtualBoardTracker__[(7-x)][y] = 'Black'

					if y == 0 or y == 7:

						BlockColor = self.__Color1__
						if y == 7:
							BlockColor = self.__Color2__
						
						ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['BlackRook'], font=self.__PieceSpecs__, bg=BlockColor)
						ChessPiece.grid(row=x, column=y)

						CurrentPiece = 'BlackRook'
						PieceAttributes['Label'] = ChessPiece 
						
					elif y == 1 or y == 6:
						BlockColor = self.__Color2__
						if y == 6:
							BlockColor = self.__Color1__

						ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['BlackKnight'], font=self.__PieceSpecs__, bg=BlockColor)
						ChessPiece.grid(row=x, column=y)	

						CurrentPiece = 'BlackKnight'
						PieceAttributes['Label'] = ChessPiece 

					elif y == 2 or y == 5:
						BlockColor = self.__Color1__
						if y == 5:
							BlockColor = self.__Color2__
					
						ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['BlackBishop'], font=self.__PieceSpecs__, bg=BlockColor)
						ChessPiece.grid(row=x, column=y)

						CurrentPiece = 'BlackBishop'
						PieceAttributes['Label'] = ChessPiece 
					
					elif y == 3:
						BlockColor = self.__Color2__
					
						ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['BlackQueen'], font=self.__PieceSpecs__, bg=BlockColor)
						ChessPiece.grid(row=x, column=y)

						CurrentPiece = 'BlackQueen'
						PieceAttributes['Label'] = ChessPiece 
					
					elif y == 4:
						BlockColor = self.__Color1__
					
						ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['BlackKing'], font=self.__PieceSpecs__, bg=BlockColor)
						ChessPiece.grid(row=x, column=y)

						CurrentPiece = 'BlackKing'
						PieceAttributes['Label'] = ChessPiece 
				
				elif x == 1: # G Row
					self.__VirtualBoardTracker__[(7-x)][y] = 'Black'

					BlockColor = self.__Color2__
					if y%2 != 0:
						BlockColor = self.__Color1__
					
					ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['BlackPawn'], font=self.__PieceSpecs__, bg=BlockColor)
					ChessPiece.grid(row=x, column=y)

					CurrentPiece = 'BlackPawn'
					PieceAttributes['Label'] = ChessPiece 
				
				elif x == 6: # B Row
					self.__VirtualBoardTracker__[(7-x)][y] = 'White'

					BlockColor = self.__Color1__
					if y%2 != 0:
						BlockColor = self.__Color2__
					
					ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['WhitePawn'], font=self.__PieceSpecs__, bg=BlockColor)
					ChessPiece.grid(row=x, column=y)

					CurrentPiece = 'WhitePawn'
					PieceAttributes['Label'] = ChessPiece 

				elif x == 7: # A Row
					self.__VirtualBoardTracker__[(7-x)][y] = 'White'

					if y == 0 or y == 7:
						BlockColor = self.__Color2__
						if y == 7:
							BlockColor = self.__Color1__

						ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['WhiteRook'], font=self.__PieceSpecs__, bg=BlockColor)
						ChessPiece.grid(row=x, column=y)
						
						CurrentPiece = 'WhiteRook'
						PieceAttributes['Label'] = ChessPiece 
					
					elif y == 1 or y == 6:
						BlockColor = self.__Color1__
					
						if y == 6:
							BlockColor = self.__Color2__
						
						ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['WhiteKnight'], font=self.__PieceSpecs__, bg=BlockColor)
						ChessPiece.grid(row=x, column=y)

						CurrentPiece = 'WhiteKnight'
						PieceAttributes['Label'] = ChessPiece 
					
					elif y == 2 or y == 5:
						BlockColor = self.__Color2__
					
						if y == 5:
							BlockColor = self.__Color1__
						
						ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['WhiteBishop'], font=self.__PieceSpecs__, bg=BlockColor)
						ChessPiece.grid(row=x, column=y)
						
						CurrentPiece = 'WhiteBishop'
						PieceAttributes['Label'] = ChessPiece 
					
					elif y == 3:
						BlockColor = self.__Color1__
						
						ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['WhiteQueen'], font=self.__PieceSpecs__, bg=BlockColor)
						ChessPiece.grid(row=x, column=y)

						CurrentPiece = 'WhiteQueen'
						PieceAttributes['Label'] = ChessPiece 
					
					elif y == 4:
						BlockColor = self.__Color2__
						
						ChessPiece = Label(self.__TopFrame__, text=self.__Pieces__['WhiteKing'], font=self.__PieceSpecs__, bg=BlockColor)
						ChessPiece.grid(row=x, column=y)

						CurrentPiece = 'WhiteKing'
						PieceAttributes['Label'] = ChessPiece

				if CurrentPiece not in self.__PieceCharacteristics__.keys():
					self.__PieceCharacteristics__[CurrentPiece] = []
				self.__PieceCharacteristics__[CurrentPiece].append(PieceAttributes)
	
	def ReInitiatePieces(self, BoardSquares, Log):
		"""Function Changes the Color of All The Pieces When Board Colors Are Changed."""

		PieceAttributes = Log.GetCurrentLog()

		for ChessPiece in self.__PieceCharacteristics__:
			for i in range(0, len(self.__PieceCharacteristics__[ChessPiece])):
				self.__PieceCharacteristics__[ChessPiece][i]['Label'].configure(bg = BoardSquares[PieceAttributes[ChessPiece][i]['CurrentSquare']]['Color'])

	def Initiate(self, Master, Log, Pieces, PieceSpecs, Color1, Color2, TopFrame):
		"""Function Is Called Once When The Application is Started To Put Pieces in Place"""
		
		self.__SetParameters__(Master, Pieces, PieceSpecs, Color1, Color2, TopFrame)
		self.__SetPieces__()
		Log.PushLog(CopyDictionary(self.__PieceCharacteristics__), "")
	
	def DestroyPieces(self):
		"""Function is Called When We have To Open New Game on Top of earler one."""

		Master = self.__TopFrame__
		for ChessPiece in self.__PieceCharacteristics__:
			for Piece in self.__PieceCharacteristics__[ChessPiece]:
				Piece['Label'].destroy()

	def MovePiece(self, ChessPiece, NewSquare, BoardSquares, Log, Action, Compliment):
		StorMove = False

		if len(ChessPiece) == 1:
			# No Castling
			ChessPiece = ChessPiece[0]
		
		else:
			#Castling
			if Action == "Short-Castled":
				if ChessPiece[0][:5] == 'White':
					StoreMove = self.__ChangePosition__(ChessPiece[0], 'g1', BoardSquares, 'e1', "Move") # WhiteKing
					StoreMove = self.__ChangePosition__(ChessPiece[1], 'f1', BoardSquares, 'h1', "Move") # WhiteRook

				elif ChessPiece[0][:5] == 'Black':
					StoreMove = self.__ChangePosition__(ChessPiece[0], 'g8', BoardSquares, 'e8', "Move") # BlackKing
					StoreMove = self.__ChangePosition__(ChessPiece[1], 'f8', BoardSquares, 'h8', "Move") # BlackRook

			elif Action == "Long-Castled":
				if ChessPiece[0][:5] == 'White':
					StoreMove = self.__ChangePosition__(ChessPiece[0], 'c1', BoardSquares, 'e1', "Move") # WhiteKing
					StoreMove = self.__ChangePosition__(ChessPiece[1], 'd1', BoardSquares, 'a1', "Move") # WhiteRook

				elif ChessPiece[0][:5] == 'Black':
					StoreMove = self.__ChangePosition__(ChessPiece[0], 'c8', BoardSquares, 'e8', "Move") # BlackKing
					StoreMove = self.__ChangePosition__(ChessPiece[1], 'd8', BoardSquares, 'a8', "Move") # BlackRook
			
			if StoreMove:
				Log.PushLog(CopyDictionary(self.__PieceCharacteristics__), Compliment)
				return True
			else:
				return False

		if ChessPiece[5:] == 'King' or ChessPiece[5:] == 'Queen':
			if len(NewSquare) == 1:	
				StoreMove = self.__ChangePosition__(ChessPiece, NewSquare[0], BoardSquares, MoveKingAndQueen(ChessPiece, NewSquare[0], self.__PieceCharacteristics__, self.__VirtualBoardTracker__), Action)
		
		elif ChessPiece[5:] == 'Knight':
			if len(NewSquare) == 1:	
				StoreMove = self.__ChangePosition__(ChessPiece, NewSquare[0], BoardSquares, MoveKnight(ChessPiece, NewSquare[0], self.__PieceCharacteristics__, self.__VirtualBoardTracker__), Action)
			elif len(NewSquare) == 2:
				StoreMove = self.__ChangePosition__(ChessPiece, NewSquare[1], BoardSquares, MoveKnight(ChessPiece, NewSquare, self.__PieceCharacteristics__, self.__VirtualBoardTracker__), Action)
		
		elif ChessPiece[5:] == 'Bishop':
			if len(NewSquare) == 1:		
				StoreMove = self.__ChangePosition__(ChessPiece, NewSquare[0], BoardSquares, MoveBishop(ChessPiece, NewSquare[0], self.__PieceCharacteristics__, self.__VirtualBoardTracker__), Action)
		
		elif ChessPiece[5:] == 'Rook':
			if len(NewSquare) == 1:
				StoreMove = self.__ChangePosition__(ChessPiece, NewSquare[0], BoardSquares, MoveRook(ChessPiece, NewSquare[0], Action, self.__PieceCharacteristics__, self.__VirtualBoardTracker__), Action)
			elif len(NewSquare) == 2:
				StoreMove = self.__ChangePosition__(ChessPiece, NewSquare[1], BoardSquares, MoveRook(ChessPiece, NewSquare, Action, self.__PieceCharacteristics__, self.__VirtualBoardTracker__), Action)

		elif ChessPiece[5:] == 'Pawn':
			if len(NewSquare) == 1:
				StoreMove = self.__ChangePosition__(ChessPiece, NewSquare[0], BoardSquares, MovePawn(ChessPiece, NewSquare, Action, self.__PieceCharacteristics__, self.__VirtualBoardTracker__), Action)
			else:
				StoreMove = self.__ChangePosition__(ChessPiece, NewSquare[1], BoardSquares, MovePawn(ChessPiece, NewSquare, Action, self.__PieceCharacteristics__, self.__VirtualBoardTracker__), Action)


		# In Log File I need NewSquare, BoardSquares
		if StoreMove:
			Log.PushLog(CopyDictionary(self.__PieceCharacteristics__), Compliment)
			return True
		else:
			return False
			
	def __ChangePosition__(self, ChessPiece, NewSquare, BoardSquares, Address, Action):
		"""Changes Position Of The Choosen Piece.."""
		if Address == None:
			MoveError = "{CP} cannot {A} to {NS}.\n Please reload the game after recifying the fault in game.".format(CP=ChessPiece, A=Action, NS=NewSquare)
			MessageBox.showerror("Error: ", MoveError)
			return False

		if Action == "Capture":
			for Piece in self.__PieceCharacteristics__: # e.g. 'WhiteRook' -> Piece
				for PieceNum in self.__PieceCharacteristics__[Piece]: # PieceNum -> WhiteRook: List 
					if PieceNum['CurrentSquare'] == NewSquare:
						PieceNum['IsInGame'] = False

		for Piece in self.__PieceCharacteristics__[ChessPiece]:
			if Piece['CurrentSquare'] == Address:
				Piece['CurrentSquare'] = NewSquare

		return True

	def GetPieceAttributes(self):
		return self.__PieceCharacteristics__

class MakeBoard:
	"""Make The Chess Board On the Main Screen."""

	def __SetParameters__(self, Master, SquareHeight, SquareWidth, Color1, Color2):
		self.__Master__ = Master
		self.__SquareHeight__ = SquareHeight
		self.__SquareWidth__ = SquareWidth
		self.__Color1__ = Color1
		self.__Color2__ = Color2
		
		self.__LabelFrame__ = LabelFrame(self.__Master__, text="Chess Board", bg='white', height=self.__SquareHeight__*9.7, width=self.__SquareWidth__*8+65,labelanchor=N, bd=10,padx=10, pady=5)
		self.__LabelFrame__.place(x=10, y=5)

		self.__TopFrame__ = Frame(self.__LabelFrame__, highlightbackground="#aa5555", highlightcolor="green", highlightthickness=10, height=self.__SquareHeight__*8, width=self.__SquareWidth__*8)
		self.__TopFrame__.place(x=0, y=0)

	def __MakeBoard__(self):
		self.__BoardSquares__ = {}
		Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

		for x in range(0, 8):
			for y in range(0, 8):
				SquareIdentity = Alphabets[y] + str((8-x))
				SquareAttributes = {}
				
				SquareAttributes['X'] = x
				SquareAttributes['Y'] = y

				if x%2 == 0:
					if y%2 == 0:
						BlockColor = self.__Color1__
						
						BlockFrame = Frame(self.__TopFrame__, height = self.__SquareHeight__, width = self.__SquareWidth__, bg=BlockColor)
						BlockFrame.grid(row=x, column=y)

						SquareAttributes['ColorNumber'] = '1'
						SquareAttributes['Color'] = BlockColor
						SquareAttributes['Frame'] = BlockFrame

					else:
						BlockColor = self.__Color2__
						
						BlockFrame = Frame(self.__TopFrame__, height = self.__SquareHeight__, width = self.__SquareWidth__, bg=BlockColor)
						BlockFrame.grid(row=x, column=y)

						SquareAttributes['ColorNumber'] = '2'
						SquareAttributes['Color'] = BlockColor
						SquareAttributes['Frame'] = BlockFrame
				else:
					if y%2 == 0:
						BlockColor = self.__Color2__
						
						BlockFrame = Frame(self.__TopFrame__, height = self.__SquareHeight__, width = self.__SquareWidth__, bg=BlockColor)
						BlockFrame.grid(row=x, column=y)

						SquareAttributes['ColorNumber'] = '2'
						SquareAttributes['Color'] = BlockColor
						SquareAttributes['Frame'] = BlockFrame

					else:
						BlockColor = self.__Color1__
						
						BlockFrame = Frame(self.__TopFrame__, height = self.__SquareHeight__, width = self.__SquareWidth__, bg=BlockColor)
						BlockFrame.grid(row=x, column=y)

						SquareAttributes['ColorNumber'] = '1'
						SquareAttributes['Color'] = BlockColor
						SquareAttributes['Frame'] = BlockFrame

				self.__BoardSquares__[SquareIdentity] = SquareAttributes

	def Initiate(self, Master, SquareHeight, SquareWidth, Color1, Color2):
		"""Function Is Called Once When The Application is Started To Make ChessBoard"""

		self.__SetParameters__(Master, SquareHeight, SquareWidth, Color1, Color2)
		self.__MakeBoard__()

	def ReInitiateBoard(self, Color1, Color2):
		"""Function Changes the Color of All The Pieces When Board Colors Are Changed"""

		for Square in self.__BoardSquares__:
			SquareAttributes = self.__BoardSquares__[Square]

			if SquareAttributes['ColorNumber'] == '1':
				SquareAttributes['Color'] = Color1
			elif SquareAttributes['ColorNumber'] == '2':
				SquareAttributes['Color'] = Color2

			SquareAttributes['Frame'].configure(bg=SquareAttributes['Color'])

	def GetBoardSquares(self):
		"""Function Returns The Dictionary Which has all the attributes of the BlockSquares"""

		return self.__BoardSquares__
	
	def GetTopFrame(self):
		return self.__TopFrame__

	def GetLabelFrame(self):
		return self.__LabelFrame__	

class DriverClass(MakeBoard, MakePieces):
	
	def __init__(self, Master):
		self.__Master__ = Master
		self.__Pieces__ = {
			'WhiteRook': u'\u2656',
			'WhiteKnight': u'\u2658',
			'WhiteBishop': u'\u2657',
			'WhiteKing': u'\u2654',
			'WhiteQueen': u'\u2655',
			'WhitePawn': u'\u2659',
			'BlackRook': u'\u265C',
			'BlackKnight': u'\u265E',
			'BlackBishop': u'\u265D',
			'BlackKing': u'\u265A',
			'BlackQueen': u'\u265B',
			'BlackPawn': u'\u265F'	
		}

		self.__PieceSpecs__ = "arial 38"
		self.__SquareWidth__ = 64
		self.__SquareHeight__ = 64
		
	def InitiateSequence(self, Log) :
		self.__Board__ = MakeBoard()
		self.__ChessPieces__ = MakePieces()
		self.__SetColors__()

		self.__Board__.Initiate(self.__Master__, self.__SquareHeight__, self.__SquareWidth__, self.__Color1__, self.__Color2__)
		self.__ChessPieces__.Initiate(self.__Master__, Log, self.__Pieces__, self.__PieceSpecs__, self.__Color1__, self.__Color2__, self.__Board__.GetTopFrame())

	def ReInitiate(self, Log):
		self.__SetColors__()
		self.__Board__.ReInitiateBoard(self.__Color1__, self.__Color2__)
		self.__ChessPieces__.ReInitiatePieces(self.GetBoardSquares(), Log)
	
	def __GetBlockColors__(self):
		return Change().GetColorsFromDataBase()

	def __SetColors__(self):
		BlockColors = self.__GetBlockColors__()
		self.__Color1__ = BlockColors[0]
		self.__Color2__ = BlockColors[1]

	def GetSymbols(self):
		return self.__Symbols__

	def MakeMove(self, ChessPiece, Square, Log, Action, Compliment):
		return self.__ChessPieces__.MovePiece(ChessPiece, Square, self.__Board__.GetBoardSquares(), Log, Action, Compliment)

	def GetBoardSquares(self):
		return self.__Board__.GetBoardSquares()

	def GetPieceAttributes(self):
		return self.__ChessPieces__.GetPieceAttributes()
	
	def GetLabelFrame(self):
		return self.__Board__.GetLabelFrame()

	def NewGame(self, Log):
		self.__ChessPieces__.DestroyPieces()
		self.__ChessPieces__.Initiate(self.__Master__, Log, self.__Pieces__, self.__PieceSpecs__, self.__Color1__, self.__Color2__, self.__Board__.GetTopFrame())


class Widgets:
	""" Make Widgets of the Main Application."""

	def __init__(self, App):
		self.__Application__ = App
		self.__Master__ = App.GetMaster()
		self.__LabelFrame__ = App.GetLabelFrame()
		self.__Compliment__ = ""
		self.MakeWidgets()

	def MakeWidgets(self):
		# Pervious Move Button
		self.__Master__.bind('<Left>', self.PreviousMoveFromLogFile)
		self.__PreviousImage__ = Image.open(self.__GetImagePath__() + "\\Images\\Previous.png")
		self.__PreviousImage__ = ImageTk.PhotoImage(self.__ResizeImage__(self.__PreviousImage__, [45, 30]))
		self.__Perviousbutton__ = Button(self.__LabelFrame__, image=self.__PreviousImage__, width="45", height="30", command=self.PreviousMoveFromLogFile)
		self.__Perviousbutton__.place(x=208.5, y=545)

		# Next Move Button
		self.__Master__.bind('<Right>', self.NextMoveFromLogFile)
		self.__NextImage__ = Image.open(self.__GetImagePath__() + "\\Images\\Next.png")
		self.__NextImage__ = ImageTk.PhotoImage(self.__ResizeImage__(self.__NextImage__, [45, 30]))
		self.__Nextbutton__ = Button(self.__LabelFrame__, image=self.__NextImage__, width="45", height="30", command=self.NextMoveFromLogFile)
		self.__Nextbutton__.place(x=272.5, y=545)

		# Compliment Box
		self.__ComplimentLabelFrame__ = LabelFrame(self.__Master__, text="Compliment", bg='white', height= 58, width= 500, bd=3, padx=5, pady=2)
		self.__ComplimentLabelFrame__.place(x=605, y= 15)
	
	def NextMoveFromLogFile(self, event=""):
		"""Used To Get the Next Move From The File."""

		self.__DisplayCompliment__(self.__Application__.NextLogFileMove())

	def PreviousMoveFromLogFile(self, event=""):
		""" Used To Get the Pervious Move From The File."""

		self.__DisplayCompliment__(self.__Application__.PreviousLogFileMove())

	def __GetImagePath__(self):
		""" Returns the Path of the Image. """

		return OperatingSystem.getcwd()

	def __ResizeImage__(self, CurrentImage, MaxSize):
		""" Used To resize the Image of Button """

		WidthRatio = CurrentImage.size[0]/MaxSize[0]
		HeightRatio = CurrentImage.size[1]/MaxSize[1]
		Ratio = max(WidthRatio, HeightRatio)
		NewSize = (int(CurrentImage.size[0]/Ratio), int(CurrentImage.size[1]/Ratio))
		CurrentImage = CurrentImage.resize(NewSize, Image.ANTIALIAS)
		return CurrentImage

	def __DisplayCompliment__(self, Compliment):
		""" Displayes Comment in Compliment Box. """

		if str(type(self.__Compliment__)) == "<class 'tkinter.Label'>" and Compliment is not "Ended":
			self.__Compliment__.destroy()

		if Compliment != None and Compliment is not "Ended":
			self.__Compliment__ = Label(self.__ComplimentLabelFrame__, bg='white', text=Compliment, font= ("Helvetica", 16))
			self.__Compliment__.place(relx = 0, rely = 0)

class Application(object):
	""" Main Application """
	
	def __init__(self):
		"""Constructor Called Only for One Time in the starting of the Application.."""

		self.__Root__ = Tk()
		self.__Root__.configure(background='white')
		self.__ApplicationWindow__ = DriverClass(self.__Root__)
		self.__Geometery__ ='1000x700+100+50'
		self.__IsFirstGame__ = True
		
		self.__Logs__ = Log()
		self.__ApplicationWindow__.InitiateSequence(self.__Logs__)
		self.__Logs__.SetBoardSquares(self.__ApplicationWindow__.GetBoardSquares())
		self.__Logs__.SetPieceAttributes(self.__ApplicationWindow__.GetPieceAttributes())

	def __ReInitiate__(self):
		"""This Function is Called when a New File is Opened on the Top of Earlier File.."""

		self.__Logs__.EmptyLogFile()
		self.__ApplicationWindow__.NewGame(self.__Logs__)
		self.__Logs__.SetBoardSquares(self.__ApplicationWindow__.GetBoardSquares())
		self.__Logs__.SetPieceAttributes(self.__ApplicationWindow__.GetPieceAttributes())

	def InitiateRootProperties(self):
		self.__Root__.title("Chess Game Reviser")
		self.__Root__.geometry("{0}x{1}+0+0".format(self.__Root__.winfo_screenwidth()-3, self.__Root__.winfo_screenheight()-3))
		self.__Root__.bind('<Escape>', self.__Geometery__)
		self.__Root__.resizable(True, True)
		self.__Root__.mainloop()

	#================== The Functions Below are Used to Change Color of Board =========================#

	def __GetNewColor__(self, ColorNumber):
		"""Gets The  New Color of the Board.."""

		NewColor = ColorChooser.askcolor(title="Select New Color")
		NewColor = NewColor[1]

		if NewColor == None:
			if ColorNumber == 1:
				return "white" # Get Default Color1
			elif ColorNumber == 2:
				return "skyblue" # GetDefault Color2
		else:
			return NewColor

	def __ChangeColor__(self, Color, ColorNumber):
		"""Changes The Color of the Board.."""

		if Change().UpdateColor(Color, ColorNumber):
			self.__ApplicationWindow__.ReInitiate(self.__Logs__)

	def ChangeBoardColor1(self):
		"""Changes the Color 1 of the board.."""

		NewColor1 = self.__GetNewColor__(1)
		if NewColor1 != "white":
			self.__ChangeColor__(NewColor1, 1)

	def ChangeBoardColor2(self):
		"""Changes the Color 2 of the board.."""

		NewColor2 = self.__GetNewColor__(2)
		if NewColor2 != "skyblue":
			self.__ChangeColor__(NewColor2, 2)

	#==================================================================================================#
	#================= The Function Below is Used to Get the Main Root Window =========================#

	def GetMaster(self):
		return self.__Root__

	#==================================================================================================#
	#===================== The Functions Below are Used in the File Menu ==============================#	
	
	def OpenStoredGame(self):
		"""This is Called When The Open File Button is pressed."""

		OpenedGame = FileDialog.askopenfile(initialdir="c:\\Codes\\Projects\\Chess_Game_Simulation\\Games", title="Select Game File", filetypes=(("Text Files", ".txt"), ("All Files", "*.*")))
		if OpenedGame != None:
			
			if self.__IsFirstGame__:
				self.__IsFirstGame__ = False
			else:
				self.__ReInitiate__()
				
			Game = RefineGameFile(OpenedGame)
			WhiteMove = 0
			BlackMove = 0

			for i in range(0, Game['NumberOfMoves']):
				if i%2 == 0:
					if self.MakeMove(Game['WhiteMoves'][WhiteMove][1], '1'):
						WhiteMove += 1
					else:
						self.__Logs__.EmptyLogFile()
						break
				else:
					if self.MakeMove(Game['BlackMoves'][BlackMove][1], '2'):
						BlackMove += 1
					else:
						self.__Logs__.EmptyLogFile()
						break

	def MakeMove(self, Move, Side):
		"""Gets The Information For Each Move In the .txt File Using Decode Function. """

		StoreMove = DecodeMove(Move, Side)
		print("StoreMove: {S}".format(S=StoreMove))
		
		Piece = StoreMove[0]
		Action = StoreMove[1]
		Square = StoreMove[2]
		Compliment = StoreMove[3]
		
		if Piece != None and Square != None:
			if len(Piece) != 0 and len(Square) != 0:
				return self.__ApplicationWindow__.MakeMove(Piece, Square, self.__Logs__, Action, Compliment)
		elif Piece is None and Square is None:
			self.__Logs__.PushLog(None, Compliment)
			return True

	def NextLogFileMove(self):
		"""This Function is Called When Next Move Button is Pressed."""

		Move = self.__Logs__.NextMove()
		
		if Move is "NotValid":
			return "Ended"
		else:
			return Move
	
	def PreviousLogFileMove(self):
		"""This Function is Called When Previous Move Button is Pressed."""

		Move = self.__Logs__.PreviousMove()

		if Move is "NotValid":
			return None
		else:
			return Move
	
	def AddNewGame(self):
		""" Still to add Functionality. """
		pass

	def __ShowLogs__(self):
		""" Shows the Stored Log File in The Log Class."""

		self.__Logs__.PrintLogs()
	
	def GetLabelFrame(self):
		"""Returns the Label Frame of the Main Window.."""

		return self.__ApplicationWindow__.GetLabelFrame()
	#==================================================================================================#

def Main():

	MainApplication = Application()
	
	ApplicationMenu = ChessMenu(MainApplication)
	ApplicationWidgets = Widgets(MainApplication)

	MainApplication.InitiateRootProperties()

Main()