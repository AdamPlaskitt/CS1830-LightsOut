try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import os
from lib.enemies.enemy import Enemy
from lib.util.spritesheet import SpriteSheet
from lib.util.vector import Vector
import random


class Shuffler(Enemy):
    def __init__(self, position, settings_args):
        Enemy.__init__(self, position, True, False, 0.1, 10, 30, 0)
        self.img = simplegui._load_local_image(os.path.join(os.path.dirname(__file__), "../../textures/sprite_sheets"
                                                                                       "/enemies"
                                                                                       "/ghosts.png"))
        self.zombie = SpriteSheet(self.img, 12, 8, 100, 100)
        self.frameWidth = (self.img.get_width() / 12)
        self.frameHeight = (self.img.get_height() / 8)
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        self.settings = settings_args
        self.target = Vector(self.settings.get('width')/2, self.settings.get('height')/2)
        self.aim = self.target.copy()
        self.pos = position
        self.row = None
        self.moving = 'up'
        self.column = 0
        self.path = None

    def draw(self, canvas):
        if self.visible:
            if self.moving == 'up':
                self.row = 3
            if self.moving == 'right':
                self.row = 2
            if self.moving == 'down':
                self.row = 0
            if self.moving == 'left':
                self.row = 1
            canvas.draw_image(self.img, (self.frameWidth * self.column + self.frameCentreX,
                                         self.frameHeight * self.row + self.frameCentreY),  # center_source
                              (self.frameWidth, self.frameHeight),  # width_height_source
                              self.pos.get_pos(),  # center_dest
                              (20, 20))
            canvas.draw_line(self.pos.copy().add(Vector(-10, -20)).get_pos(), self.pos.copy().add(Vector(-10 + self.health * (2/3), -20)).get_pos(), 3, 'Red')

    def update(self):
        self.path = self.aim.copy().subtract(self.pos).normalize() * 3
        self.column += 1
        if self.column > 2:
            self.column = 0
        self.moving = self.get_orientation()
        self.pos.add(self.path)

    def is_fleeing(self):
        return self.flee

    def get_orientation(self):
        if self.pos.get_pos()[0] >= self.frameCentreX and self.pos.get_pos()[1] > self.frameCentreY:
            if self.pos.get_pos()[0] >= self.pos.get_pos()[1]:
                return 'up'
            else:
                return 'right'
        elif self.pos.get_pos()[0] > self.frameCentreX and self.pos.get_pos()[1] <= self.frameCentreY:
            if self.pos.get_pos()[0] >= -self.pos.get_pos()[1]:
                return 'down'
            else:
                return 'right'
        elif self.pos.get_pos()[0] <= self.frameCentreX and self.pos.get_pos()[1] < self.frameCentreY:
            if self.pos.get_pos()[0] <= self.pos.get_pos()[1]:
                return 'left'
            else:
                return 'down'
        elif self.pos.get_pos()[0] < self.frameCentreX and self.pos.get_pos()[1] >= self.frameCentreY:
            if self.pos.get_pos()[0] <= -self.pos.get_pos()[1]:
                return 'left'
            else:
                return 'up'
        return self.moving

if __name__ == '__main__':
    settings = {
        'width': 1000,
        'height': 750,
        'font': 'monospace',
        'fps': 60
    }
    frame = simplegui.create_frame("LightsOut", 1000, 750)
    test = Shuffler(Vector(100, 310), settings)
    frame.set_draw_handler(test.draw)
    frame.start()
