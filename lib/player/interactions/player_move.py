class PlayerMove:
    def __init__(self, sprite, keyboard):
        self.player = sprite
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.move:
            self.player.is_moving = True
        elif not self.keyboard.move:
            self.player.is_moving = False
