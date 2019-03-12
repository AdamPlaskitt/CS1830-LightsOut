try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import pygame
from lib.util.vector import Vector


class Player:

    def __init__(self, x_pos, y_pos):

        self.pos = (x_pos, y_pos)
        self.max_health = 100
        self.health = self.max_health
        self.dead = False
        self.is_moving = False
        self.look_dir = Vector()
        self.mouse_pos = pygame.mouse.get_pos()
        self.img = simplegui._load_local_image("../texture/sprite_sheets/player/playersprite.jpg")
        self.height = self.img.get_height()
        self.width = self.img.get_width()
        self.frame_size = self.width / 3

    def draw(self, canvas):
        canvas.draw_image(self.img, (100, 100), (100, 100), (100, 100), (100, 100), 0)

    def update(self):
        self.update_mouse()
        self.update_sprite()

    def update_mouse(self):
        self.mouse_pos = pygame.mouse.get_pos()
        print(self.mouse_pos[1])
        #self.look_dir = Vector(self.mouse_pos[0], self.mouse_pos[1])

    def update_sprite(self):
        if self.is_moving:
            pass

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
