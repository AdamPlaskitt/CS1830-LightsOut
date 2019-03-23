import sys
sys.argv.append('--no-controlpanel')
import pygame
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from lib.util.vector import Vector

CANVASWIDTH = 1000
CANVASHEIGHT = 750


class Torch:
    def __init__(self):
        self.zoom = 2
        self.mapPos = [CANVASWIDTH/2,CANVASHEIGHT/2]
        self.mousePos = [0,0]
        self.isSmaTorch = False
        self.isMedTorch = True
        self.isBigTorch = False
        self.radius = 1
        self.circleThick = 1
        self.lightRadius = 1
        self.damage = 1


    def draw(self, canvas):
        canvas.draw_circle(self.mousePos, self.radius, self.circleThick, 'Black')
        canvas.draw_polygon([[0,0],[self.mousePos[0] - self.lightRadius, 0],[self.mousePos[0] - self.lightRadius, CANVASHEIGHT],[0,CANVASHEIGHT]], 1, 'Black', 'Black')
        canvas.draw_polygon([[CANVASWIDTH,0],[self.mousePos[0] + self.lightRadius, 0],[self.mousePos[0] + self.lightRadius, CANVASHEIGHT],[CANVASWIDTH,CANVASHEIGHT]], 1, 'Black', 'Black')
        canvas.draw_polygon([[0,0], [CANVASWIDTH,0], [CANVASWIDTH, self.mousePos[1] - self.lightRadius],[0, self.mousePos[1] - self.lightRadius]], 1, 'Black', 'Black')
        canvas.draw_polygon([[0,CANVASHEIGHT], [CANVASWIDTH,CANVASHEIGHT], [CANVASWIDTH, self.mousePos[1] + self.lightRadius],[0, self.mousePos[1] + self.lightRadius]], 1, 'Black', 'Black')
        # canvas.draw_line([CANVASWIDTH/2,CANVASHEIGHT/2], self.mousePos, 1, 'Red')

    def createSmaTorch(self):
        self.radius = 150
        self.circleThick = 200
        self.lightRadius = 75
        self.damage = 3

    def useSmallTorch(self):
        self.isSmaTorch = True
        self.isMedTorch = False
        self.isBigTorch = False

    def createMedTorch(self):
        self.radius = 250
        self.circleThick = 300
        self.lightRadius = 100
        self.damage = 1.5

    def useMediumTorch(self):
        self.isSmaTorch = False
        self.isMedTorch = True
        self.isBigTorch = False

    def createBigTorch(self):
        self.radius = 400
        self.circleThick = 500
        self.lightRadius = 200
        self.damage = 0.1

    def useBigTorch(self):
        self.isSmaTorch = False
        self.isMedTorch = False
        self.isBigTorch = True

    def update(self):
        if Vector(self.mapPos[0], self.mapPos[1]).copy().subtract(Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])).length() >= self.lightRadius-20:
            self.mousePos = pygame.mouse.get_pos()
        if self.isSmaTorch:
            self.createSmaTorch()
        if self.isMedTorch:
            self.createMedTorch()
        if self.isBigTorch:
            self.createBigTorch()


if __name__ == '__main__':
    torch = Torch()

    def draw(canvas):
        torch.update()
        torch.draw(canvas)

    frame = simplegui.create_frame("LightsOut", CANVASWIDTH, CANVASHEIGHT)
    frame.set_canvas_background("Blue")
    frame.set_draw_handler(draw)
    frame.start()
