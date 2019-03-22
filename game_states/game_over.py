import pygame
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from lib.state_machine.states import States
from lib.game_functions.scoreboard.scores import Scores


class Button:
    def __init__(self, canvas, pos, txt, colour_txt, colour_back, settings_arg, length):
        self.settings = settings_arg
        self.canvas = canvas
        self.pos = pos
        self.xRat = 1.045
        self.yRat = 6
        self.width = 4
        self.colourTxt = colour_txt
        self.colourBack = colour_back
        self.txt = txt
        self.point1 = pos
        self.point2 = [self.pos[0] + length, self.pos[1]]
        self.point3 = [self.pos[0] + length, self.pos[1] + 80]
        self.point4 = [self.pos[0], self.pos[1] + 80]
        self.length = length

    def draw(self):
        self.canvas.draw_polygon([self.point1, self.point2, self.point3, self.point4], self.width, self.colourTxt,
                                 self.colourBack)
        self.canvas.draw_text(self.txt, [self.pos[0] * 2, self.pos[1] + self.settings.get('height') / self.yRat / 2],
                              50, self.colourTxt, self.settings.get('font'))


class GameOver(States):
    def __init__(self, settings_arg):
        States.__init__(self)
        self.settings = settings_arg
        self.score = 0  # change to function
        self.msg = {'title': "Game Over!",
                    'score': "Score: {value} ",
                    'enter': "Enter your name for the leaderboard:",
                    'name': "",
                    'sub': "Submit",
                    'main': "Main Menu"
                    }
        self.h1Size = 48
        self.h2Size = 24
        self.h3Size = 18
        self.sub_button = None
        self.main_button = None
        self.pos = None
        self.button_submit = None
        self.button_main = None
        self.entered = False

    # Override
    def set_up(self):
        self.msg = {'title': "Game Over!",
                    'score': "Score: {value} ",
                    'enter': "Enter your name for the leaderboard:",
                    'name': "",
                    'sub': "Submit",
                    'main': "Main Menu"
                    }
        self.entered = False
        self.key_pressed = False
        self.key = None
        # the boundaries of the button
        bp1 = (200, 500)
        bp2 = (200, 580)
        bp3 = (self.settings.get('width') - 200, 500)
        bp4 = (self.settings.get('width') - 200, 580)
        self.button_submit = [bp1, bp2, bp3, bp4]

        bp5 = (200, 627)
        bp6 = (200, 627 + 80)
        bp7 = (self.settings.get('width') - 200, 627)
        bp8 = (self.settings.get('width') - 200, 627 + 80)

        self.button_main = [bp5, bp6, bp7, bp8]
        value = self.score  # get value
        self.msg.update({'score': self.msg.get('score').format(value=value)})

    # Override
    def click(self, pos):
        self.pos = pos
        if self.is_in_bounds(self.button_submit, self.pos) and not self.entered:
            Scores().add_score(self.score, self.msg.get('name'))
            self.entered = True
        if self.is_in_bounds(self.button_main, self.pos):
            self.next = 'menu'
            self.done = True

    def key_reader(self):
        if self.key_pressed:
            self.key_pressed = False
            self.msg.update({'name': '{name}{add}'.format(name=self.msg.get('name'), add=self.key)})

    # Handler for mouse click
    # Handler to draw on canvas
    # Override
    def draw(self, canvas):
        self.pos = pygame.mouse.get_pos()
        canvas.draw_text(self.msg.get('title'),
                         [self.settings.get('width') / 2 - 120, 2 * (self.settings.get('height') / 9)], self.h1Size,
                         "Red")
        canvas.draw_text(self.msg.get('score'),
                         [self.settings.get('width') / 2 - 50, 3 * (self.settings.get('height') / 9)], self.h2Size,
                         "White")
        canvas.draw_text(self.msg.get('enter'),
                         [self.settings.get('width') / 2 - 175, 4 * (self.settings.get('height') / 9)], self.h2Size,
                         "White")
        canvas.draw_text(self.msg.get('name'),
                         [self.settings.get('width') / 2 - 175, 5 * (self.settings.get('height') / 9)], self.h3Size,
                         "White")
        self.sub_button = Button(canvas, [200, self.settings.get('height') - self.settings.get('height') / 3],
                                 self.msg.get('sub'), 'White', 'Black', self.settings, self.settings.get('width') - 400)
        self.main_button = Button(canvas, [200, self.settings.get('height') - self.settings.get('height') / 6],
                                  self.msg.get('main'), 'White', 'Black', self.settings,
                                  self.settings.get('width') - 400)
        if self.is_in_bounds(self.button_submit, self.pos) and not self.entered:
            self.sub_button = Button(canvas, [200, self.settings.get('height') - self.settings.get('height') / 3],
                                     self.msg.get('sub'), 'Black', 'White', self.settings,
                                     self.settings.get('width') - 400)
        if self.is_in_bounds(self.button_main, self.pos):
            self.main_button = Button(canvas, [200, self.settings.get('height') - self.settings.get('height') / 6],
                                      self.msg.get('main'), 'Black', 'White', self.settings,
                                      self.settings.get('width') - 400)
        self.sub_button.draw()
        self.main_button.draw()


if __name__ == '__main__':
    frame = simplegui.create_frame("LightsOut", 1000, 750)
    settings = {
        'width': 1000,
        'height': 750,
        'font': 'monospace',
        'fps': 60
    }
    test = GameOver(settings)
    test.set_up()
    frame.set_draw_handler(test.draw)
    frame.set_mouseclick_handler(test.click)
    frame.set_keydown_handler(test.key_listener)
    frame.start()
