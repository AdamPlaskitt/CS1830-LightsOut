import sys
try:
    import simplegui
except ImportError:
    sys.argv.append('--no-controlpanel')
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import os
from game_states.Torch import Torch


class Inventory:

    def __init__(self, slots, size, canvas_width, canvas_height):
        self.torch = Torch()
        x = os.path.join(os.path.dirname(__file__), "../../textures/sprite_sheets/player/torch.png")
        self.torch_img = simplegui._load_local_image(x)
        y = os.path.join(os.path.dirname(__file__), "../../textures/sprite_sheets/player/torch_lock.png")
        self.torch_lock_img = simplegui._load_local_image(y)
        self.screen_width = canvas_width
        self.screen_height = canvas_height
        self.slots = slots
        self.size = size
        self.bars = math.floor(self.slots / 2)
        self.score = 0
        self.slot_1_selected = True
        self.slot_2_selected = False
        self.slot_3_selected = False
        self.slot_4_selected = False
        self.slot_5_selected = False
        self.slot_6_selected = False
        self.slot_7_selected = False
        self.slot_8_selected = False
        self.slot_9_selected = False
        self.highlighted = 1

    def draw(self, canvas):
        # TODO
        #self.torch.draw(canvas)
        if self.score >= 100:
            canvas.draw_image(self.torch_img, (256, 256), (512, 512),
                            (self.screen_width / 2 - self.size, self.screen_height - 10 - self.size / 2), (50, 50))
        else:
            canvas.draw_image(self.torch_lock_img, (256, 256), (512, 512),
                              (self.screen_width / 2 - self.size, self.screen_height - 10 - self.size / 2), (50, 50))
        canvas.draw_image(self.torch_img, (256, 256), (512, 512),
                          (self.screen_width / 2, self.screen_height - 10 - self.size / 2), (75, 75))
        if self.score >= 500:
            canvas.draw_image(self.torch_img, (256, 256), (512, 512),
                            (self.screen_width / 2 + self.size, self.screen_height - 10 - self.size / 2), (100, 100))
        else:
            canvas.draw_image(self.torch_lock_img, (256, 256), (512, 512),
                            (self.screen_width / 2 + self.size, self.screen_height - 10 - self.size / 2), (100, 100))
        canvas.draw_line(((self.screen_width / 2) - (self.size * self.slots / 2), self.screen_height - 10 - self.size),
                         ((self.screen_width / 2) + (self.size * self.slots / 2), self.screen_height - 10 - self.size),
                         5, 'White')
        canvas.draw_line(((self.screen_width / 2) - (self.size * self.slots / 2), self.screen_height - 10),
                         ((self.screen_width / 2) + (self.size * self.slots / 2), self.screen_height - 10), 5, 'White')
        for i in range(-self.slots + self.bars, self.slots - self.bars):
            canvas.draw_line(((self.screen_width / 2) + (self.size * i) + self.size / 2,
                              self.screen_height - 10 - self.size),
                             ((self.screen_width / 2) + (self.size * i) + self.size / 2, self.screen_height - 10),
                             5, 'White')
        canvas.draw_polyline([((self.screen_width / 2) + (self.size * (self.highlighted - self.slots / 2)),
                               self.screen_height - 10 - self.size),
                              ((self.screen_width / 2) + (self.size * (self.highlighted - (self.slots / 2 - 1))),
                               self.screen_height - 10 - self.size),
                              ((self.screen_width / 2) + (self.size * (self.highlighted - (self.slots / 2 - 1))),
                               self.screen_height - 10),
                              ((self.screen_width / 2) + (self.size * (self.highlighted - self.slots / 2)),
                               self.screen_height - 10),
                              ((self.screen_width / 2) + (self.size * (self.highlighted - self.slots / 2)),
                               self.screen_height - 10 - self.size)], 7, 'Blue')

    def update(self):
        self.torch.update()
        if self.slot_1_selected and self.score >= 100:
            self.highlighted = 0
            self.torch.useSmallTorch()
        if self.slot_2_selected:
            self.highlighted = 1
            self.torch.useMediumTorch()
        if self.slot_3_selected and self.score >= 500:
            self.highlighted = 2
            self.torch.useBigTorch()
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
