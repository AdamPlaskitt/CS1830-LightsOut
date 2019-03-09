import pygame
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from lib.state_machine.states import States


class GameOver(States):
    def __init__(self, settings):
        States.__init__(self)
        self.settings = settings
        self.score = None  # change to function
        self.msg = {'title': "Game Over!",
                    'score': "Score: {value} ",
                    'enter': "Enter your name for the leaderboard:",
                    'sub': "Submit",
                    'main': "Main Menu"
                    }
        self.h1Size = 48
        self.h2Size = 24
        self.h3Size = 18
        self.button1 = None
        self.button2 = None
        self.pos = None

    def set_up(self):
        bp1 = (200, 12*(self.settings.get('height')/18))
        bp2 = (200, 14*(self.settings.get('height')/18))
        bp3 = (self.settings.get('width')-200, 14*(self.settings.get('height')/18))
        bp4 = (self.settings.get('width')-200, 12*(self.settings.get('height')/18))
        self.button1 = [bp1, bp2, bp3, bp4]
        bp5 = (200, 15*(self.settings.get('height')/18))
        bp6 = (200, 17*(self.settings.get('height')/18))
        bp7 = (self.settings.get('width')-200, 17*(self.settings.get('height')/18))
        bp8 = (self.settings.get('width')-200, 15*(self.settings.get('height')/18))
        self.button2 = [bp5, bp6, bp7, bp8]

        print(self.msg)
        value = '---'  # get value
        self.msg.update({'score': self.msg.get('score').format(value=value)})
        print(self.msg)

    def click(self, pos):
        self.pos = pos

    # Handler for mouse click
    # Handler to draw on canvas
    def draw(self, canvas):
        pos = pygame.mouse.get_pos()
        canvas.draw_text(self.msg.get('title'), [(self.centre_text(self.msg.get('title'), self.h1Size)), 2 * (self.settings.get('height') / 9)], self.h1Size, "Red")
        canvas.draw_text(self.msg.get('score'), [(self.centre_text(self.msg.get('score'), self.h2Size)), 3 * (self.settings.get('height') / 9)], self.h2Size, "White")
        canvas.draw_text(self.msg.get('enter'), [(self.centre_text(self.msg.get('enter'), self.h2Size)), 4 * (self.settings.get('height') / 9)], self.h2Size, "White")
        canvas.draw_polygon(self.button1, 5, "White", "Black")
        canvas.draw_polygon(self.button2, 5, "White", "Black")
        canvas.draw_text(self.msg.get('sub'), [self.centre_text(self.msg.get('sub'), self.h3Size), 13.25 * (self.settings.get('height') / 18)], self.h3Size, "White")
        canvas.draw_text(self.msg.get('main'), [self.centre_text(self.msg.get('main'), self.h3Size), 16.25 * (self.settings.get('height') / 18)], self.h3Size, "White")

    def centre_text(self, message, size):
        len = frame.get_canvas_textwidth(message, size)
        return (self.settings.get('width')/2)-(len/2)


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
    frame.start()
