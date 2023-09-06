from tkinter import *
from fractions import Fraction

frame = Tk()

width = frame.winfo_screenwidth()
height = frame.winfo_screenheight()

aspRatio = Fraction(width, height)

frame.title("Hackergame")
frame.geometry("1080x0+0+0")
frame.mainloop()