try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from lib.game_functions.scoreboard.scores import Scores

CANVASWIDTH = 1000
CANVASHEIGHT = 750


class Leaderboard:
    def __init__(self):
        self.startPos = [CANVASWIDTH/50, CANVASHEIGHT/2.5]
        self.backPos = [[10, 10], [10, 50], [50, 50], [50, 10]]
        self.arrowPos = [[20, 30], [30, 40], [30, 20]]
        self.arrowShaftPos = [[30, 30], [40, 30]]
        self.location, self.scores = Scores().get_scores()  # TODO implement threading to speed up load time
        self.length = 10
        if len(self.scores) < self.length:
            self.length = len(self.scores)
        for i in range(self.length):
            chars = len(str(self.scores[i][0]))
            for j in range(13-chars):
                self.scores[i][0] = str(self.scores[i][0]) + '-'

    def draw(self, canvas):
        self.canvas = canvas
        self.canvas.draw_text("Leaderboard", (CANVASWIDTH / 7, CANVASHEIGHT / 7), CANVASWIDTH / 10, "White", 'monospace')
        self.canvas.draw_polygon(self.backPos, 4, "White")
        self.canvas.draw_polygon(self.arrowPos, 4, "White")
        self.canvas.draw_polygon(self.arrowShaftPos, 4, "White")
        self.canvas.draw_text(self.location, (CANVASWIDTH / 2.5, CANVASHEIGHT / 4), CANVASWIDTH / 15, "White",
                              'monospace')
        for i in range(self.length):
            self.canvas.draw_text(str(self.scores[i][0]), (CANVASWIDTH / 10, (CANVASHEIGHT / 3) + (i * 50)), CANVASWIDTH / 20, "White",
                                  'monospace')
            self.canvas.draw_text(self.scores[i][1], (CANVASWIDTH / 2, (CANVASHEIGHT / 3) + (i * 50)), CANVASWIDTH / 20,
                                  "White", 'monospace')

if __name__ == '__main__':
    frame = simplegui.create_frame("LightsOut", CANVASWIDTH, CANVASHEIGHT)
    test = Leaderboard()
    frame.set_draw_handler(test.draw)
    frame.start()
