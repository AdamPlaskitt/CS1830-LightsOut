try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import pygame
from lib.state_machine.states import States
from lib.game_functions.scoreboard.scores import Scores


class Leaderboard(States):
    def __init__(self, settings_arg):
        States.__init__(self)
        self.settings = settings_arg
        self.font = self.settings.get('font')
        self.next = 'menu'
        self.startPos = [self.settings.get('width')/50, self.settings.get('height')/2.5]
        self.backPos = [[10, 10], [10, 50], [50, 50], [50, 10]]
        self.arrowPos = [[20, 30], [30, 40], [30, 20]]
        self.arrowShaftPos = [[30, 30], [40, 30]]
        self.location, self.scores = Scores().get_scores()
        self.backX = 50
        self.backY = 50
        self.pos = None
        self.length = 10

    def set_up(self):
        if len(self.scores) < self.length:
            self.length = len(self.scores)
        for i in range(self.length):
            chars = len(str(self.scores[i][0]))
            for j in range(13-chars):
                self.scores[i][0] = str(self.scores[i][0]) + '-'

    def draw(self, canvas):
        self.pos = pygame.mouse.get_pos()
        canvas.draw_text("Leaderboard", (self.settings.get('width') / 7, self.settings.get('height') / 7),
                         self.settings.get('width') / 10, "White", self.font)
        canvas.draw_polygon(self.backPos, 4, "White")
        canvas.draw_polygon(self.arrowPos, 4, "White")
        canvas.draw_polygon(self.arrowShaftPos, 4, "White")
        canvas.draw_text(self.location, (self.settings.get('width') / 2.5, self.settings.get('height') / 4),
                         self.settings.get('width') / 15, "White", self.font)
        for i in range(self.length):
            canvas.draw_text(str(self.scores[i][0]), (self.settings.get('width') / 10, (self.settings.get('height') / 3)
                                                      + (i * 50)), self.settings.get('width') / 20, "White", self.font)
            canvas.draw_text(self.scores[i][1], (self.settings.get('width') / 2, (self.settings.get('height') / 3)
                                                 + (i * 50)), self.settings.get('width') / 20, "White", self.font)

    def click(self, pos):
        if pos[0] < self.backX and pos[1] < self.backY:
            self.done = True


if __name__ == '__main__':
    frame = simplegui.create_frame("LightsOut", 1000, 750)
    settings = {
        'width': 1000,
        'height': 750,
        'font': 'monospace',
        'fps': 60
    }
    test = Leaderboard(settings)
    test.set_up()
    frame.set_draw_handler(test.draw)
    frame.start()
