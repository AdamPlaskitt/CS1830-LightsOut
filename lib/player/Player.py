import sys
try:
    import simplegui
except ImportError:
    sys.argv.append('--no-controlpanel')
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import pygame
from lib.util.vector import Vector
import os
import math

class Player:

    def __init__(self, x_pos, y_pos):

        self.x = x_pos
        self.y = y_pos
        self.pos = (x_pos, y_pos)
        self.max_health = 100
        self.health = self.max_health
        self.dead = False
        self.is_moving = False
        self.mouse_pos = pygame.mouse.get_pos()
        x = os.path.join(os.path.dirname(__file__), "../../textures/sprite_sheets/player/playersprite.jpg")
        self.img = simplegui._load_local_image(x)
        self.height = 180
        self.width = 411
        self.frame_width = self.width / 3
        self.frame_centre = self.frame_width / 2
        self.frame_index = 0
        self.frame_up = True
        self.clock = 0
        self.rot = 0
        self.speed = 5  # amount of frames per sprite update

    def draw(self, canvas):
        canvas.draw_image(self.img, (self.frame_width * self.frame_index + self.frame_centre, self.height / 2),
                          (self.frame_width, self.height), self.pos, (100, 100), self.rot)
        canvas.draw_line(self.pos, self.mouse_pos, 2, 'Red')

    def update(self):
        self.update_rot()
        self.clock += 1
        if self.clock % self.speed == 0:
            self.update_sprite()

    def update_rot(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.mouse_pos[0] > self.x and self.mouse_pos[1] > self.y:
            self.rot = -(math.pi + math.asin(
                (self.mouse_pos[0] - self.x) / math.sqrt(math.pow(self.mouse_pos[0] - self. x, 2) +
                                                         math.pow(self.mouse_pos[1] - self.y, 2))))
        if self.mouse_pos[0] > self.x and self.mouse_pos[1] < self.y:
            self.rot = math.asin(
                (self.mouse_pos[0] - self.x) / math.sqrt(math.pow(self.mouse_pos[0] - self. x, 2) +
                                                         math.pow(self.mouse_pos[1] - self.y, 2)))
        if self.mouse_pos[0] < self.x and self.mouse_pos[1] < self.y:
            self.rot = math.asin(
                (self.mouse_pos[0] - self.x) / math.sqrt(math.pow(self.mouse_pos[0] - self. x, 2) +
                                                         math.pow(self.mouse_pos[1] - self.y, 2)))
        if self.mouse_pos[0] < self.x and self.mouse_pos[1] > self.y:
            self.rot = -(math.pi + math.asin(
                (self.mouse_pos[0] - self.x) / math.sqrt(math.pow(self.mouse_pos[0] - self. x, 2) +
                                                         math.pow(self.mouse_pos[1] - self.y, 2))))


    def update_sprite(self):
        if self.is_moving:
            if self.frame_up:
                self.frame_index += 1
                if self.frame_index == 3:
                    self.frame_up = False
            if not self.frame_up:
                self.frame_index -= 1
                if self.frame_index == 0:
                    self.frame_up = True

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead = True


class Keyboard:
    def __init__(self):
        self.move = False

    def key_down(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.move = True
        if key == simplegui.KEY_MAP['left']:
            self.move = True
        if key == simplegui.KEY_MAP['up']:
            self.move = True
        if key == simplegui.KEY_MAP['down']:
            self.move = True

    def key_up(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.move = False
        if key == simplegui.KEY_MAP['left']:
            self.move = False
        if key == simplegui.KEY_MAP['up']:
            self.move = False
        if key == simplegui.KEY_MAP['down']:
            self.move = False


class PlayerMove:
    def __init__(self, sprite, keyboard):
        self.player = sprite
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.move:
            self.player.is_moving = True
        elif not self.keyboard.move:
            self.player.is_moving = False


if __name__ == '__main__':
    CANVASWIDTH = 500
    CANVASHEIGHT = 500
    player = Player(CANVASWIDTH / 2, CANVASHEIGHT / 2)
    kbd = Keyboard()
    inter = PlayerMove(player, kbd)

    def draw(canvas):
        inter.update()
        player.update()
        player.draw(canvas)

    frame = simplegui.create_frame("Game", CANVASWIDTH, CANVASHEIGHT)
    frame.set_draw_handler(draw)
    frame.set_keydown_handler(kbd.key_down)
    frame.set_keyup_handler(kbd.key_up)
    frame.start()
