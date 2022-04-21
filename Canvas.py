from pygame import *
from Colors import *
from OptionsWindow import *
import sys, OptionsWindow

init()

class Canvas:
    def __init__(self, background):
        self.background = background
        self.window = display.set_mode((800,800))
        display.set_caption("Paint")
        self.clock = time.Clock()
        self.brush = PaintBrush(self)
        self.options = Options(self.brush,self)
        self.window.fill(self.background)
        key.set_repeat(50, 25)

    def update(self):
        self.clock.tick(200)
        self.options.update()
        self.brush.draw()
        display.update()
        self.doEvents()

    def doEvents(self):
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:
                    self.clear()
                if e.key == K_UP:
                    self.brush.changeSize(1)
                if e.key == K_DOWN and self.brush.size > 1:
                    self.brush.changeSize(-1)

    def clear(self):
        self.window.fill(self.background)
        self.brush.positions.clear()


class PaintBrush:
    def __init__(self, canvas):
        self.canvas = canvas
        self.color = white
        self.positions = []
        self.size = 1

    def draw(self):
        if mouse.get_pressed()[0] == 1:
            self.positions.append(mouse.get_pos())
            if len(self.positions) > 2:
                draw.lines(self.canvas.window, self.color, False, self.positions, self.size)
        if len(event.get(eventtype=MOUSEBUTTONUP)) > 0:
            self.positions.clear()

    def changeSize(self, amount):
        self.size += amount

    def changeColor(self, color):
        self.color = color


c = Canvas(black)
while True:
    c.update()
