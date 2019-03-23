class Quit:
    def __init__(self, player, keyboard):
        self.kbd = keyboard
        self.player = player

    def update(self):
        if self.kbd.q:
            self.player.final_score = self.player.score
            self.player.game_over = True
