try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import pygame
from lib.state_machine.states import States
from lib.game_functions.scoreboard.scores import Scores

CANVASWIDTH = 1000
CANVASHEIGHT = 750


class Leaderboard(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'menus'
        self.startPos = [CANVASWIDTH/50, CANVASHEIGHT/2.5]
        self.backPos = [[10, 10], [10, 50], [50, 50], [50, 10]]
        self.arrowPos = [[20, 30], [30, 40], [30, 20]]
        self.arrowShaftPos = [[30, 30], [40, 30]]
        self.location, self.scores = Scores().get_scores()  # TODO implement threading to speed up load time
        self.backX = 50
        self.backY = 50
        self.pos = None
        self.length = 10
        if len(self.scores) < self.length:
            self.length = len(self.scores)
        for i in range(self.length):
            chars = len(str(self.scores[i][0]))
            for j in range(13-chars):
                self.scores[i][0] = str(self.scores[i][0]) + '-'

    def draw(self, canvas):
        self.pos = pygame.mouse.get_pos()
        canvas.draw_text("Leaderboard", (CANVASWIDTH / 7, CANVASHEIGHT / 7), CANVASWIDTH / 10, "White", 'monospace')
        canvas.draw_polygon(self.backPos, 4, "White")
        canvas.draw_polygon(self.arrowPos, 4, "White")
        canvas.draw_polygon(self.arrowShaftPos, 4, "White")
        canvas.draw_text(self.location, (CANVASWIDTH / 2.5, CANVASHEIGHT / 4), CANVASWIDTH / 15, "White", 'monospace')
        for i in range(self.length):
            canvas.draw_text(str(self.scores[i][0]), (CANVASWIDTH / 10, (CANVASHEIGHT / 3) + (i * 50)), CANVASWIDTH
                             / 20, "White", 'monospace')
            canvas.draw_text(self.scores[i][1], (CANVASWIDTH / 2, (CANVASHEIGHT / 3) + (i * 50)), CANVASWIDTH / 20,
                             "White", 'monospace')

    def click(self, pos):
        if pos[0] < self.backX and pos[1] < self.backY:
            self.done = True


if __name__ == '__main__':
    frame = simplegui.create_frame("LightsOut", CANVASWIDTH, CANVASHEIGHT)
    test = Leaderboard()
    frame.set_draw_handler(test.draw)
    frame.start()
