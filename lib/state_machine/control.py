try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Control:
    def __init__(self):
        self.done = False
        self.state_dict = None
        self.state_name = None
        self.state = None

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state = self.state_dict[self.state_name]
        self.state.set_up()
        self.state.previous = previous

    def update(self, canvas):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(canvas)

    def event_loop(self):
        pass
        # click handler?

    def main_game_loop(self, canvas):
        self.event_loop()
        self.update(canvas)
        self.state.draw(canvas)
