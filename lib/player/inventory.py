import sys
try:
    import simplegui
except ImportError:
    sys.argv.append('--no-controlpanel')
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

CANVASHEIGHT = 500
CANVASWIDTH = 500


class Inventory:

    def __init__(self, slots, size):
        self.slots = slots
        self.size = size
        self.bars = math.floor(self.slots / 2)
        self.slot_1_selected = True
        self.slot_2_selected = False
        self.slot_3_selected = False
        self.slot_4_selected = False
        self.slot_5_selected = False
        self.slot_6_selected = False
        self.slot_7_selected = False
        self.slot_8_selected = False
        self.slot_9_selected = False
        self.highlighted = 0

    def draw(self, canvas):
        canvas.draw_line(((CANVASWIDTH / 2) - (self.size * self.slots / 2), CANVASHEIGHT - 10 - self.size),
                         ((CANVASWIDTH / 2) + (self.size * self.slots / 2), CANVASHEIGHT - 10 - self.size), 5, 'White')
        canvas.draw_line(((CANVASWIDTH / 2) - (self.size * self.slots / 2), CANVASHEIGHT - 10),
                         ((CANVASWIDTH / 2) + (self.size * self.slots / 2), CANVASHEIGHT - 10), 5, 'White')
        for i in range(-self.slots + self.bars, self.slots - self.bars):
            canvas.draw_line(((CANVASWIDTH / 2) + (self.size * i) + self.size / 2, CANVASHEIGHT - 10 - self.size),
                             ((CANVASWIDTH / 2) + (self.size * i) + self.size / 2, CANVASHEIGHT - 10), 5, 'White')
        canvas.draw_polyline([((CANVASWIDTH / 2) + (self.size * (self.highlighted - self.slots / 2)),
                               CANVASHEIGHT - 10 - self.size),
                              ((CANVASWIDTH / 2) + (self.size * (self.highlighted - (self.slots / 2 - 1))),
                               CANVASHEIGHT - 10 - self.size),
                              ((CANVASWIDTH / 2) + (self.size * (self.highlighted - (self.slots / 2 - 1))),
                               CANVASHEIGHT - 10),
                              ((CANVASWIDTH / 2) + (self.size * (self.highlighted - self.slots / 2)),
                               CANVASHEIGHT - 10),
                              ((CANVASWIDTH / 2) + (self.size * (self.highlighted - self.slots / 2)),
                               CANVASHEIGHT - 10 - self.size)], 7, 'Blue')

    def update(self):
        if self.slot_1_selected:
            self.highlighted = 0
        if self.slot_2_selected:
            self.highlighted = 1
        if self.slot_3_selected:
            self.highlighted = 2
        if self.slot_4_selected:
            self.highlighted = 3
        if self.slot_5_selected:
            self.highlighted = 4
        if self.slot_6_selected:
            self.highlighted = 5
        if self.slot_7_selected:
            self.highlighted = 6
        if self.slot_8_selected:
            self.highlighted = 7
        if self.slot_9_selected:
            self.highlighted = 8
        if self.highlighted >= self.slots:
            self.highlighted = self.slots - 1
