class Enemy(object):
    def __init__(self, position, visible, light, attack_str=10, speed=10, max_health=50, heal=1):
        # TODO update default values
        self.max_health = max_health
        self.health = self.max_health
        self.speed = speed
        self.attack_str = attack_str
        self.visible = visible
        self.light = light
        self.pos = position
        self.heal = heal
        self.dead = False
        self.flee = False

    # Can be overridden
    # is enemy in regen of torch
    def is_in_torch(self):
        # TODO conduct check against vector position of torch
        self.flee = True
        return self.light

    def update(self):
        pass

    def draw(self, canvas):
        pass

    # Don't override
    # is the enemy alive
    def is_alive(self):
        if self.health > 0 or not self.dead:
            return True
        return False

    # have the enemy take damage
    def take_damage(self, damage):
        self.health = self.health - damage
        if not self.is_alive():
            self.dead = False

    # is the enemy fleeing from the torch
    def is_fleeing(self):
        return self.flee

    def healing(self):
        if not self.is_fleeing() and self.is_alive():
            if self.health < self.max_health:
                self.health = self.health + self.heal
        if self.health > self.max_health:
            self.health = self.max_health
