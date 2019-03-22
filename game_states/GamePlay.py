import pygame
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import os
from lib.state_machine.states import States
from lib.map.map import Map

CANVASWIDTH = 1000
CANVASHEIGHT = 750


class GamePlay(States):
    def __init__(self, settings):
        States.__init__(self)
        self.mapPos = [CANVASWIDTH/2,CANVASHEIGHT/2]
        self.mousePos = [0,0]
        self.game = Map()

    def set_up(self):
        self.mapPos = [CANVASWIDTH / 2, CANVASHEIGHT / 2]
        self.mousePos = [0, 0]
        self.game = Map()

    def draw(self, canvas):
        self.game.draw(canvas)

    def update(self, canvas):
        if self.game.player.game_over:
            self.next = 'gameOver'
            self.done = True

    def key_listener(self, key):
        self.game.kbd.key_down(key)

    def key_up(self, key):
        self.game.kbd.key_up(key)




if __name__ == '__main__':
    settings = {
        'width': 1000,
        'height': 750,
        'font': 'monospace',
        'fps': 60
    }
    frame = simplegui.create_frame("LightsOut", CANVASWIDTH, CANVASHEIGHT)
    gamePlay = GamePlay(settings)
    frame.set_draw_handler(gamePlay.draw)
    frame.start()
