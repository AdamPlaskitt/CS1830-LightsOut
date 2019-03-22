try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# The control class (and its dependencies in State) is a modified version of the control class from the tutorial at
# https://python-forum.io/Thread-PyGame-Creating-a-state-machine?fbclid=IwAR2cWol3wi134xyNpRQOh0Bpf_q6i7sYRxjyH5IW
# -qMyEAZlxWYDim7B488
class Control:
    def __init__(self):
        self.done = False
        self.state_dict = None
        self.state_name = None
        self.state = None

    # set up the start state for when Control is first run
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
        self.state.set_up()

    # change state
    def flip_state(self):
        self.state.clean_up()
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state = self.state_dict[self.state_name]
        self.state.set_up()
        self.state.previous = previous

    # check if a state is done or quit
    def update(self, canvas):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(canvas)

    # key_handler
    def key_board_loop(self, key):
        self.state.key_listener(key)
        self.state.key_reader()

    def key_up(self, key):
        self.state.key_up(key)

    # click handler
    def event_loop(self, pos):
        self.state.click(pos)

    # draw handler, checks for updates then draws.
    def main_game_loop(self, canvas):
        self.update(canvas)
        self.state.draw(canvas)
