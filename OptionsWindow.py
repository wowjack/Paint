from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

def interizer(list):
    newlist = []
    for item in list:
        newlist.append(int(item))
    return newlist

class Options:
    def __init__(self, brush, canvas):
        self.brush = brush
        self.canvas = canvas
        self.root = Tk()
        self.root.title("Paint Options")
        self.root.geometry("400x200")
        self.contents = ttk.Frame(self.root, borderwidth=20)
        self.drawColorButton = ttk.Button(self.contents, text="Draw Color", command=self.chooseBrushColor)
        self.backColorButton = ttk.Button(self.contents, text="Background Color", command=self.chooseBackColor)
        self.contents.grid(column=0,row=0)
        self.drawColorButton.grid(column=0,row=0)
        self.backColorButton.grid(column=1,row=0)

    def update(self):
        self.root.update()

    def chooseBrushColor(self):
        color = colorchooser.askcolor()[0]
        self.brush.changeColor(color)
        self.brush.positions.clear()

    def chooseBackColor(self):
        color = colorchooser.askcolor()[0]
        self.canvas.background = color
        self.canvas.clear()
