class States(object):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

    # Overridable methods
    def clean_up(self):
        pass

    def set_up(self):
        pass

    def draw(self, canvas):
        pass

    def click(self, pos):
        pass

    def update(self, canvas):
        self.draw(canvas)
