from tkinter import messagebox
import sqlite3
import os

class Change(object):
	def __init__(self):
		self.__Connection__ = sqlite3.connect(self.__GetPath__())
		self.__Cursor__ = self.__Connection__.cursor()
		
	def UpdateColor(self, Color, ColorNumber):
		Updated = False

		try:
			Query = "update 'Colors' set BlockColor = \'" + str(Color) + "\' where ColorNumber = "+ str(ColorNumber) +""
			self.__Cursor__.execute(Query)
			self.__Connection__.commit()
			# messagebox.showinfo("Success", "Color Updated.")
			Updated = True
			self.__Connection__.close()

		except Exception as e:
			Data = str(e).split()
			Data = Data[0]
			if Data == 'UNIQUE':
				messagebox.showinfo("Constraint", "Both the colors of the board Cannot be same.")
			else:
				messagebox.showerror("Error: ", str(e))
	
		return Updated 

	def GetColorsFromDataBase(self):
		BlockColors = self.__Cursor__.execute('Select * From Colors').fetchall()
		return [BlockColors[0][1], BlockColors[1][1]]
		self.__Connection__.close()

	def __GetPath__(self):
		return os.getcwd() + "\\Storage\\Settings.db"
		