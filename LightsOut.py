#!/usr/bin/python
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import sys
from lib.state_machine.control import Control
from game_states.menu import Menu
from game_states.leaderboard import Leaderboard
from game_states.game_over import GameOver


# main function to be run
def main():
    """settings:
    game settings to be used by control.State
    state_dict:
    dictionary of the states and the call code
    create screen assigning handlers from app to screen
    """
    settings = {
        'width': 1000,
        'height': 750,
        'font': 'monospace',
        'fps': 60
    }

    app = Control()
    state_dict = {
        # passing settings into the states
        'menu': Menu(settings),
        'leaderboard': Leaderboard(settings),
        'gameOver':  GameOver(settings)
    }

    app.setup_states(state_dict, 'menu')

    screen = simplegui.create_frame("LightsOut", settings.get('width'), settings.get('height'))
    screen.set_draw_handler(app.main_game_loop)
    screen.set_mouseclick_handler(app.event_loop)
    screen.set_keydown_handler(app.key_board_loop)

    # start the game screen
    screen.start()
    sys.exit()


if __name__ == '__main__':
    main()
