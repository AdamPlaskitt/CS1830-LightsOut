class ChangeSlot:
    def __init__(self, inventory, keyboard):
        self.inventory = inventory
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.one:
            self.inventory.slot_1_selected = True
        else:
            self.inventory.slot_1_selected = False
        if self.keyboard.two:
            self.inventory.slot_2_selected = True
        else:
            self.inventory.slot_2_selected = False
        if self.keyboard.three:
            self.inventory.slot_3_selected = True
        else:
            self.inventory.slot_3_selected = False
        if self.keyboard.four:
            self.inventory.slot_4_selected = True
        else:
            self.inventory.slot_4_selected = False
        if self.keyboard.five:
            self.inventory.slot_5_selected = True
        else:
            self.inventory.slot_5_selected = False
        if self.keyboard.six:
            self.inventory.slot_6_selected = True
        else:
            self.inventory.slot_6_selected = False
        if self.keyboard.seven:
            self.inventory.slot_7_selected = True
        else:
            self.inventory.slot_7_selected = False
        if self.keyboard.eight:
            self.inventory.slot_8_selected = True
        else:
            self.inventory.slot_8_selected = False
        if self.keyboard.nine:
            self.inventory.slot_9_selected = True
        else:
            self.inventory.slot_9_selected = False