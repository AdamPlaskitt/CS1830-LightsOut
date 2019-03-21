import pygame
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import os

CANVASWIDTH = 1000
CANVASHEIGHT = 750

class GamePlay:

    def __init__(self):
        self.zoom = 2
        self.mapPos = [CANVASWIDTH/2,CANVASHEIGHT/2]
        self.mousePos = [0,0]

    def drawDark(self, canvas):
        canvas.draw_circle(self.mousePos, 250, 300, 'Black')
        canvas.draw_polygon([[0,0],[self.mousePos[0]-100, 0],[self.mousePos[0]-100, CANVASHEIGHT],[0,CANVASHEIGHT]], 1, 'Black', 'Black')
        canvas.draw_polygon([[CANVASWIDTH,0],[self.mousePos[0]+100, 0],[self.mousePos[0]+100, CANVASHEIGHT],[CANVASWIDTH,CANVASHEIGHT]], 1, 'Black', 'Black')
        canvas.draw_polygon([[0,0], [CANVASWIDTH,0], [CANVASWIDTH, self.mousePos[1]-100],[0, self.mousePos[1]-100]], 1, 'Black', 'Black')
        canvas.draw_polygon([[0,CANVASHEIGHT], [CANVASWIDTH,CANVASHEIGHT], [CANVASWIDTH, self.mousePos[1]+100],[0, self.mousePos[1]+100]], 1, 'Black', 'Black')
        canvas.draw_line([CANVASWIDTH/2,CANVASHEIGHT/2], self.mousePos, 1, 'Red')

    def drawMap(self, canvas):
        map = simplegui._load_local_image(os.path.join(os.path.dirname(__file__), "../gameMap.jpg"))
        canvas.draw_image(map, (map.get_width()/2,map.get_height()/2), (map.get_width(),map.get_height()), (self.mapPos[0],self.mapPos[1]), (CANVASWIDTH*self.zoom,CANVASHEIGHT*self.zoom))

    def draw(self, canvas):
        mousePosStart = pygame.mouse.get_pos()
        self.mousePos[0] = mousePosStart[0]-252
        self.mousePos[1] = mousePosStart[1]-27
        self.drawMap(canvas)
        self.drawDark(canvas)

if __name__ == '__main__':
    frame = simplegui.create_frame("LightsOut", CANVASWIDTH, CANVASHEIGHT)
    gamePlay = GamePlay()
    frame.set_draw_handler(gamePlay.draw)
    frame.start()
