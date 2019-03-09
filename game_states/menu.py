import pygame
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from lib.state_machine.states import States


CANVASWIDTH = 1000
CANVASHEIGHT = 750


class Button:
    def __init__(self, canvas, pos, txt, colour_txt, colour_back):
        self.canvas = canvas
        self.pos = pos
        self.xRat = 1.045
        self.yRat = 6
        self.width = 10
        self.colourTxt = colour_txt
        self.colourBack = colour_back
        self.txt = txt
        self.point1 = pos
        self.point2 = [self.pos[0] + CANVASWIDTH/self.xRat, self.pos[1]]
        self.point3 = [self.pos[0] + CANVASWIDTH/self.xRat, self.pos[1] + CANVASHEIGHT/self.yRat]
        self.point4 = [self.pos[0], self.pos[1] + CANVASHEIGHT/self.yRat]

    def draw(self):
        self.canvas.draw_polygon([self.point1, self.point2, self.point3, self.point4], self.width, self.colourTxt,
                                 self.colourBack)
        self.canvas.draw_text(self.txt, [self.pos[0]*4, self.pos[1] + CANVASHEIGHT/self.yRat/2], 50, self.colourTxt,
                              'monospace')


class Menu(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'leaderboard'  # TODO, change to enum
        self.startPos = [CANVASWIDTH / 50, CANVASHEIGHT / 2.5]
        self.helpPos = [CANVASWIDTH / 50, CANVASHEIGHT / 1.67]
        self.exitPos = [CANVASWIDTH / 50, CANVASHEIGHT / 1.25]
        self.backPos = [[10, 10], [10, 50], [50, 50], [50, 10]]
        self.arrowPos = [[20, 30], [30, 40], [30, 20]]
        self.arrowShaftPos = [[30, 30], [40, 30]]
        self.backX = 50
        self.backY = 50
        self.isStart = False
        self.isHelp = False
        self.isLeader = False
        self.isMenu = True
        self.isExit = False
        self.pos = None

    def drag(self, pos):
        self.pos = pos

    def click(self, pos):
        self.pos = pos

        if self.isMenu and self.startButton.point1[1] < self.pos[1] < self.startButton.point4[1]:
            self.isStart = True
            self.isHelp = False
            self.isLeader = False
            self.isMenu = False

        if self.isMenu and self.helpButton.point1[1] < self.pos[1] < self.helpButton.point4[1]:
            self.isStart = False
            self.isHelp = True
            self.isLeader = False
            self.isMenu = False

        if self.isMenu and self.leaderButton.point1[1] < self.pos[1] < self.leaderButton.point4[1]:
            self.next = 'leaderboard'
            self.done = True

        if self.isMenu and self.pos[0] < self.backX and self.pos[1] < self.backY:
            self.isExit = True

        if (self.isStart or self.isHelp or self.isLeader) and self.pos[0] < self.backX and self.pos[1] < self.backY:
            self.isStart = False
            self.isHelp = False
            self.isLeader = False
            self.isMenu = True

    def draw(self, canvas):
        self.pos = pygame.mouse.get_pos()
        self.startButton = Button(canvas, self.startPos, "Start", 'White', 'Black')
        self.helpButton = Button(canvas, self.helpPos, "Help", 'White', 'Black')
        self.leaderButton = Button(canvas, self.exitPos, "LeaderBoard", 'White', 'Black')
        if self.startButton.point1[1] < self.pos[1] < self.startButton.point4[1] * 1.1:
            self.startButton.colourBack = 'White'
            self.helpButton.colourBack = 'Black'
            self.leaderButton.colourBack = 'Black'
            self.startButton.colourTxt = 'Black'
            self.helpButton.colourTxt = 'White'
            self.leaderButton.colourTxt = 'White'
        elif self.helpButton.point1[1] < self.pos[1] < self.helpButton.point4[1] * 1.1:
            self.startButton.colourBack = 'Black'
            self.helpButton.colourBack = 'White'
            self.leaderButton.colourBack = 'Black'
            self.startButton.colourTxt = 'White'
            self.helpButton.colourTxt = 'Black'
            self.leaderButton.colourTxt = 'White'
        elif self.leaderButton.point1[1] < self.pos[1] < self.leaderButton.point4[1] * 1.1:
            self.startButton.colourBack = 'Black'
            self.helpButton.colourBack = 'Black'
            self.leaderButton.colourBack = 'White'
            self.startButton.colourTxt = 'White'
            self.helpButton.colourTxt = 'White'
            self.leaderButton.colourTxt = 'Black'
        else:
            self.startButton.colourBack = 'Black'
            self.helpButton.colourBack = 'Black'
            self.leaderButton.colourBack = 'Black'
            self.startButton.colourTxt = 'White'
            self.helpButton.colourTxt = 'White'
            self.leaderButton.colourTxt = 'White'

        if self.isMenu:
            canvas.draw_text("LightsOut",(CANVASWIDTH/7, CANVASHEIGHT/4), CANVASWIDTH/7.5, "White", 'monospace')
            self.startButton.draw()
            self.helpButton.draw()
            self.leaderButton.draw()
            canvas.draw_polygon(self.backPos, 4, "Red")
            canvas.draw_line(self.backPos[0], self.backPos[2], 2, 'Red')
            canvas.draw_line(self.backPos[1], self.backPos[3], 2, 'Red')

        if self.isStart:
            canvas.draw_polygon(self.backPos, 4, "White")
            canvas.draw_polygon(self.arrowPos, 4, "White")
            canvas.draw_polygon(self.arrowShaftPos, 4, "White")

        if self.isHelp:
            canvas.draw_polygon(self.backPos, 4, "White")
            canvas.draw_polygon(self.arrowPos, 4, "White")
            canvas.draw_polygon(self.arrowShaftPos, 4, "White")

        if self.isLeader:
            self.next = 'leaderboard'
            self.done = True

        if self.isExit:
            exit()
