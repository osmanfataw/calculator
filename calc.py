from tkinter import*
import math
import parser
import tkinter.messagebox


root = Tk()
root.title("Osman calculator")
root.resizable(width = False, height=False)
root.geometry("400x400+460+40")
MainFrame = Frame(root, bd=20, pady=2,relief=RIDGE).grid()
calc = Frame(MainFrame, bd=20, pady=2, relief=RIDGE).grid()


root.mainloop()