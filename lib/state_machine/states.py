try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class States(object):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None
        self.settings = {}
        self.pos = None
        self.key_pressed = False
        self.key = None

    # Overridable methods
    def clean_up(self):
        pass

    def set_up(self):
        self.key_pressed = False
        self.key = None

    def draw(self, canvas):
        pass

    def click(self, pos):
        pass

    def key_reader(self):
        pass

    def update(self, canvas):
        self.draw(canvas)

    # Override to use for none rectangles
    def is_in_bounds(self, bounds, pos):
        # only works for rectangles
        bounds_x = []
        bounds_y = []
        for i in range(4):
            bounds_x.append(bounds[i][0])
            bounds_y.append(bounds[i][1])
        x_max = max(bounds_x[0], bounds_x[1], bounds_x[2], bounds_x[3])
        x_min = min(bounds_x[0], bounds_x[1], bounds_x[2], bounds_x[3])
        y_max = int(max(bounds_y[0], bounds_y[1], bounds_y[2], bounds_y[3]))
        y_min = int(min(bounds_y[0], bounds_y[1], bounds_y[2], bounds_y[3]))
        if x_min < pos[0] < x_max and y_min < pos[1] < y_max:
            return True
        return False

    # Don't override
    def key_listener(self, key):
        for label, value in simplegui.KEY_MAP.items():
            if value == key:
                self.key_pressed = True
                self.key = label.upper()
