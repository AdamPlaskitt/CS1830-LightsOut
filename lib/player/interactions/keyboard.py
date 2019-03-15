try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Keyboard:
    def __init__(self):
        self.move = False
        self.one = False
        self.two = False
        self.three = False
        self.four = False
        self.five = False
        self.six = False
        self.seven = False
        self.eight = False
        self.nine = False

    def key_down(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.move = True
        if key == simplegui.KEY_MAP['left']:
            self.move = True
        if key == simplegui.KEY_MAP['up']:
            self.move = True
        if key == simplegui.KEY_MAP['down']:
            self.move = True
        if key == simplegui.KEY_MAP['1']:
            self.one = True
        if key == simplegui.KEY_MAP['2']:
            self.two = True
        if key == simplegui.KEY_MAP['3']:
            self.three = True
        if key == simplegui.KEY_MAP['4']:
            self.four = True
        if key == simplegui.KEY_MAP['5']:
            self.five = True
        if key == simplegui.KEY_MAP['6']:
            self.six = True
        if key == simplegui.KEY_MAP['7']:
            self.seven = True
        if key == simplegui.KEY_MAP['8']:
            self.eight = True
        if key == simplegui.KEY_MAP['9']:
            self.nine = True

    def key_up(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.move = False
        if key == simplegui.KEY_MAP['left']:
            self.move = False
        if key == simplegui.KEY_MAP['up']:
            self.move = False
        if key == simplegui.KEY_MAP['down']:
            self.move = False
        if key == simplegui.KEY_MAP['1']:
            self.one = False
        if key == simplegui.KEY_MAP['2']:
            self.two = False
        if key == simplegui.KEY_MAP['3']:
            self.three = False
        if key == simplegui.KEY_MAP['4']:
            self.four = False
        if key == simplegui.KEY_MAP['5']:
            self.five = False
        if key == simplegui.KEY_MAP['6']:
            self.six = False
        if key == simplegui.KEY_MAP['7']:
            self.seven = False
        if key == simplegui.KEY_MAP['8']:
            self.eight = False
        if key == simplegui.KEY_MAP['9']:
            self.nine = False
