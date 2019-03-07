import pygame
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

CANVASWIDTH = 1000
CANVASHEIGHT = 750


class Button:
    def __init__(self, canvas, pos, txt, colourTxt, colourBack):
        self.canvas = canvas
        self.pos = pos
        self.xRat = 1.045
        self.yRat = 6
        self.width = 10
        self.colourTxt = colourTxt
        self.colourBack = colourBack
        self.txt = txt
        self.point1 = pos
        self.point2 = [self.pos[0] + CANVASWIDTH/self.xRat, self.pos[1]]
        self.point3 = [self.pos[0] + CANVASWIDTH/self.xRat, self.pos[1] + CANVASHEIGHT/self.yRat]
        self.point4 = [self.pos[0], self.pos[1] + CANVASHEIGHT/self.yRat]

    def draw(self):
        self.canvas.draw_polygon([self.point1, self.point2, self.point3, self.point4], self.width, self.colourTxt,
                                 self.colourBack)
        self.canvas.draw_text(self.txt, [self.pos[0]*4, self.pos[1] + CANVASHEIGHT/self.yRat/2], 50, self.colourTxt,
                              'monospace')

class Leaderboard:
    def __init__(self):
        self.startPos = [CANVASWIDTH/50, CANVASHEIGHT/2.5]
        self.backPos = [[10, 10], [10, 50], [50, 50], [50, 10]]
        self.arrowPos = [[20, 30], [30, 40], [30, 20]]
        self.arrowShaftPos = [[30, 30], [40, 30]]

    def draw(self, canvas):
        self.canvas = canvas
        self.canvas.draw_text("Leaderboard", (CANVASWIDTH / 7, CANVASHEIGHT / 7), CANVASWIDTH / 9, "White", 'monospace')
        self.canvas.draw_polygon(self.backPos, 4, "White")
        self.canvas.draw_polygon(self.arrowPos, 4, "White")
        self.canvas.draw_polygon(self.arrowShaftPos, 4, "White")

if __name__ == '__main__':
    frame = simplegui.create_frame("LightsOut", CANVASWIDTH, CANVASHEIGHT)
    test = Leaderboard()
    frame.set_draw_handler(test.draw)
    frame.start()
