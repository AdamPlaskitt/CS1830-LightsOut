try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


class SpriteSheet:
    def __init__(self, img, columns, rows, X, Y):
        """
        :param img: img
        :param columns: amount of columns
        :param rows: amount of rows
        :param X: pos
        :param Y: pos
        """
        self.end = False
        self.img = img
        self.columns = columns
        self.rows = rows
        self.frameIndex = [0, 0]
        self.frameWidth = (img.get_width() / columns)
        self.frameHeight = (img.get_height() / rows)
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        self.X = X
        self.Y = Y

    def draw(self, canvas, frame_index):
        canvas.draw_image(self.img, (self.frameWidth * frame_index[0] + self.frameCentreX,
                                     self.frameHeight * frame_index[1] + self.frameCentreY),  # center_source
                          (self.frameWidth, self.frameHeight),  # width_height_source
                          (self.X, self.Y),  # center_dest
                          (100, 100))

    def next_frame(self, offset):
        if not (self.frameIndex[1] == self.rows - 1 and self.frameIndex[0] == offset - 1):
            self.end = False
            if self.frameIndex[0] < (self.columns - 1):
                self.frameIndex[0] += 1
            else:
                self.frameIndex[0] = 0
                if self.frameIndex[1] < self.rows - 1:
                    self.frameIndex[1] += 1
                else:
                    self.frameIndex[1] = 0
                    self.end = True
        else:
            self.frameIndex[1] = 0
            self.frameIndex[0] = offset
        if self.frameIndex[1] == self.rows - 1 and self.frameIndex[0] == offset - 2:
            self.end = True

    def previous_frame(self, offset):
        if not (self.frameIndex[1] == self.rows - 1 and self.frameIndex[0] > offset):
            self.end = False
            if self.frameIndex[0] > 0:
                self.frameIndex[0] -= 1
            else:
                self.frameIndex[0] = (self.columns - 1)
                if self.frameIndex[1] > 0:
                    self.frameIndex[1] -= 1
                else:
                    self.frameIndex[1] = self.rows - 1

        else:
            self.frameIndex[1] = self.rows - 1
            self.frameIndex[0] = offset - 1

        if self.frameIndex[1] == 0 and self.frameIndex[0] == 0:
            self.end = True

    def done(self):
        return self.end
