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
        self.score = 100 #change to function
        self.msg1 = "Game Over!"
        self.msg2 = "Score: " + str(self.score)
        self.msg3 = "Enter your name for the leaderboard:"
        self.msg4 = "Submit"
        self.msg5 = "Main Menu"
        self.h1Size = 48
        self.h2Size = 24
        self.h3Size = 18
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

    def click(self, pos):
        self.pos = pos

    # Handler for mouse click
    # Handler to draw on canvas
    def draw(self, canvas):
        pos = pygame.mouse.get_pos()
        canvas.draw_text(self.msg1, [(self.centreText(self.msg1, self.h1Size)), 2*(self.settings.get('height')/9)], self.h1Size, "Red")
        canvas.draw_text(self.msg2, [(self.centreText(self.msg2, self.h2Size)), 3*(self.settings.get('height')/9)], self.h2Size, "Red")
        canvas.draw_text(self.msg3, [(self.centreText(self.msg3, self.h2Size)), 4*(self.settings.get('height')/9)], self.h2Size, "Red")
        canvas.draw_polygon(self.button1, 5, "White", "Black")
        canvas.draw_polygon(self.button2, 5, "White", "Black")
        canvas.draw_text(self.msg4, [self.centreText(self.msg4,self.h3Size), 13.25*(self.settings.get('height')/18)], self.h3Size, "Red")
        canvas.draw_text(self.msg5, [self.centreText(self.msg5,self.h3Size), 16.25*(self.settings.get('height')/18)], self.h3Size, "Red")
        print(pos)

    def centreText(self, message, size):
        len = frame.get_canvas_textwidth(message, size)
        return ((self.settings.get('width')/2)-(len/2))

'''
# Create a frame and assign callbacks to event handlers
m = Mouse()
frame = simplegui.create_frame("GameOver", CANVASWIDTH, CANVASHEIGHT)

frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
'''


if __name__ == '__main__':
    frame = simplegui.create_frame("LightsOut", 1000, 750)
    settings = {
        'width': 1000,
        'height': 750,
        'font': 'monospace',
        'fps': 60
    }
    test = GameOver(settings)
    frame.set_draw_handler(test.draw)
    frame.start()
