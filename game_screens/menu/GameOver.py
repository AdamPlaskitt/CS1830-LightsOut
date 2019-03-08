import pygame
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

CANVASWIDTH = 600
CANVASHEIGHT = 400
score = 100 #change to function
msg1 = "Game Over!"
msg2 = "Score: " + str(score)
msg3 = "Enter your name for the leaderboard:"
msg4 = "Submit"
msg5 = "Main Menu"
h1Size = 48
h2Size = 24
h3Size = 18
bp1 = (200, 12*(CANVASHEIGHT/18))
bp2 = (200, 14*(CANVASHEIGHT/18))
bp3 = (CANVASWIDTH-200, 14*(CANVASHEIGHT/18))
bp4 = (CANVASWIDTH-200, 12*(CANVASHEIGHT/18))
button1 = [bp1, bp2, bp3, bp4]
bp5 = (200, 15*(CANVASHEIGHT/18))
bp6 = (200, 17*(CANVASHEIGHT/18))
bp7 = (CANVASWIDTH-200, 17*(CANVASHEIGHT/18))
bp8 = (CANVASWIDTH-200, 15*(CANVASHEIGHT/18))
button2 = [bp5, bp6, bp7, bp8]

class Mouse:
    def __init__(self):
        self.pos = [0,0]

    def click(self, pos):
        self.pos = pos


# Handler for mouse click
# Handler to draw on canvas
def draw(canvas):
    pos = pygame.mouse.get_pos()
    canvas.draw_text(msg1, [(centreText(msg1, h1Size)), 2*(CANVASHEIGHT/9)], h1Size, "Red")
    canvas.draw_text(msg2, [(centreText(msg2, h2Size)), 3*(CANVASHEIGHT/9)], h2Size, "Red")
    canvas.draw_text(msg3, [(centreText(msg3, h2Size)), 4*(CANVASHEIGHT/9)], h2Size, "Red")
    canvas.draw_polygon(button1, 5, "White", "Black")
    canvas.draw_polygon(button2, 5, "White", "Black")
    canvas.draw_text(msg4, [centreText(msg4,h3Size), 13.25*(CANVASHEIGHT/18)], h3Size, "Red")
    canvas.draw_text(msg5, [centreText(msg5,h3Size), 16.25*(CANVASHEIGHT/18)], h3Size, "Red")
    print(pos)
def centreText(message, size):
    len = frame.get_canvas_textwidth(message, size)
    return ((CANVASWIDTH/2)-(len/2))
# Create a frame and assign callbacks to event handlers
m = Mouse()
frame = simplegui.create_frame("GameOver", CANVASWIDTH, CANVASHEIGHT)

frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
