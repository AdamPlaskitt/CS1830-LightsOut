from game_states.MapMoving import Interactions, Map, player, kbd
from pygame import mouse

from game_states.MapMoving import CANVASWIDTH
from game_states.MapMoving import CANVASHEIGHT

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

def draw(canvas):
    for inter in Interactions:
        inter.update()
    for obstacle in Map:
        obstacle.update()
        obstacle.draw(canvas)
    player.update()
    player.draw(canvas)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Game", CANVASWIDTH, CANVASHEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.key_down)
frame.set_keyup_handler(kbd.key_up)
frame.set_mousedrag_handler(mouse.drag)
frame.start()