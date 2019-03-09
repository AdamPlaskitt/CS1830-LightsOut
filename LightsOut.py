#!/usr/bin/python
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import sys
from lib.state_machine.control import Control
from game_screens.menu.MenuWithLeaderBoardTest import Menu
from game_screens.leaderboard import Leaderboard


def main():
    settings = {
        'width': 1000,
        'height': 750,
        'fps': 60
    }

    app = Control()
    state_dict = {
        'menu': Menu(),
        'leaderboard': Leaderboard()
    }

    app.setup_states(state_dict, 'menu')

    screen = simplegui.create_frame("LightsOut", settings.get('width'), settings.get('height'))
    screen.set_draw_handler(app.main_game_loop)
    screen.set_mouseclick_handler(app.state.click)
    screen.start()
    sys.exit()


if __name__ == '__main__':
    main()
