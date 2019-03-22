import sys
sys.argv.append('--no-controlpanel')
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math, random
from lib.util.vector import Vector
from lib.player.Player import Player

CANVASHEIGHT = 750
CANVASWIDTH = 1000
MIN_RAD = 1
img = simplegui.load_image(
    'https://raw.githubusercontent.com/Bill-Ferny/CS1830-LightsOut/master/textures/backgrounds/maps/gameMap.jpg')
imgCentre = Vector(307, 307)
mapZoom = 2
screenPos = Vector(307, 307)

player = Player(CANVASWIDTH/2, CANVASHEIGHT/2, 3)


class Obstacle:
    def __init__(self, x1, y1, x2, y2):
        self.startPos = imgCentre.copy().add(Vector(x1, y1).multiply(mapZoom))
        self.endPos = imgCentre.copy().add(Vector(x2, y2).multiply(mapZoom))
        self.vel = Vector()
        self.colour = 'Blue'

    def draw(self, canvas):
        canvas.draw_line(self.startPos.get_pos(), self.endPos.get_pos(), 1, self.colour)

    def update(self):
        self.startPos.add(self.vel)
        self.endPos.add(self.vel)
        self.vel.multiply(0.85)


class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['up']:
            self.up = True
        if key == simplegui.KEY_MAP['down']:
            self.down = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
        if key == simplegui.KEY_MAP['down']:
            self.down = False


class Interaction:
    def __init__(self, obstacle, keyboard, tMap):
        self.obstacle = obstacle
        self.keyboard = keyboard
        self.tMap = tMap

    def update(self):

        if self.keyboard.left:
            self.obstacle.vel.add(Vector(0.1, 0))
            # self.tMap.vel.add(Vector(0.1, 0))
        if self.keyboard.right:
            self.obstacle.vel.add(Vector(-0.1, 0))
            # self.tMap.vel.add(Vector(-0.1, 0))
        if self.keyboard.down:
            self.obstacle.vel.add(Vector(0, -0.1))
            # self.tMap.vel.add(Vector(0, -0.1))
        if self.keyboard.up:
            self.obstacle.vel.add(Vector(0, 0.1))
            # self.tMap.vel.add(Vector(0, 0.1))


class MapInteraction:
    def __init__(self, keyboard, tMap):
        # self.obstacle = obstacle
        self.keyboard = keyboard
        self.tMap = tMap

    def update(self):
        if self.keyboard.left:
            self.tMap.vel.add(Vector(0.1, 0))
        if self.keyboard.right:
            self.tMap.vel.add(Vector(-0.1, 0))
        if self.keyboard.down:
            self.tMap.vel.add(Vector(0, -0.1))
        if self.keyboard.up:
            self.tMap.vel.add(Vector(0, 0.1))


class tMap:
    def __init__(self, zoom):
        self.vel = Vector()
        self.source = img
        self.centreSource = Vector(307, 307)
        self.dimSource = Vector(614, 614)
        self.moveP = Vector(307, 307)
        self.imgZoom = Vector(614 * zoom, 614 * zoom)
        self.startPos = Vector(0, 0)
        self.endPos = Vector(0, 0)

    def draw(self, canvas):
        canvas.draw_image(img, self.centreSource.get_pos(), self.dimSource.get_pos(), self.moveP.get_pos(), self.imgZoom.get_pos())

    def update(self):
        self.moveP.add(self.vel)
        self.vel.multiply(0.85)
        screenPos = self.moveP

    def collide_check(walls):

        if walls.startPos.x <= player.pos.x <= walls.endPos.x and walls.startPos.y <= player.pos.y <= walls.endPos.y:
            print("collide with wall (" + + ", " + y1 + ")" + "(" + x2 + ", " + y2 + ")")
            return True
        else:
            return False


class Map:
    def __init__(self):
        self.kbd = Keyboard()
        self.Map = []
        # Room1 walls
        self.Map.append(Obstacle(-105, -32, -6, -32))
        self.Map.append(Obstacle(32, -32, 97, -32))
        self.Map.append(Obstacle(97, -32, 97, 7))
        self.Map.append(Obstacle(97, 41, 97, 93))
        self.Map.append(Obstacle(97, 93, 93, 93))
        self.Map.append(Obstacle(54, 93, -104, 93))
        self.Map.append(Obstacle(-104, 93, -104, 33))
        self.Map.append(Obstacle(-104, 12, -104, -32))
        # Room2 walls
        self.Map.append(Obstacle(54, 137, -140, 137))
        self.Map.append(Obstacle(92, 137, 130, 137))
        self.Map.append(Obstacle(-140, 137, -140, 300))
        self.Map.append(Obstacle(-140, 300, 130, 300))
        self.Map.append(Obstacle(130, 137, 130, 300))
        # Bridge1 walls
        self.Map.append(Obstacle(54, 93, 54, 137))
        self.Map.append(Obstacle(93, 93, 93, 137))
        # Water feature walls
        self.Map.append(Obstacle(-45, 175, 54, 175))
        self.Map.append(Obstacle(-45, 268, 54, 268))
        self.Map.append(Obstacle(-45, 175, -45, 268))
        self.Map.append(Obstacle(54, 175, 54, 268))
        # Room3 walls
        self.Map.append(Obstacle(-6, -73, -151, -73))
        self.Map.append(Obstacle(32, -73, 59, -73))
        self.Map.append(Obstacle(-151, -73, -151, -237))
        self.Map.append(Obstacle(-151, -237, 59, -237))
        self.Map.append(Obstacle(59, -237, 59, -178))
        self.Map.append(Obstacle(59, -158, 59, -73))
        # Bridge2 walls
        self.Map.append(Obstacle(-6, -73, -6, -32))
        self.Map.append(Obstacle(32, -73, 32, -32))
        # Bridge5 walls
        self.Map.append(Obstacle(59, -178, 99, -178))
        self.Map.append(Obstacle(59, -158, 99, -158))
        # Room4 walls
        self.Map.append(Obstacle(99, -178, 99, -226))
        self.Map.append(Obstacle(99, -158, 99, -80))
        self.Map.append(Obstacle(99, -80, 252, -80))
        self.Map.append(Obstacle(252, -80, 252, -226))
        self.Map.append(Obstacle(252, -226, 99, -226))
        # Room5 walls
        self.Map.append(Obstacle(161, 7, 161, -45))
        self.Map.append(Obstacle(161, 41, 161, 177))
        self.Map.append(Obstacle(161, 177, 286, 177))
        self.Map.append(Obstacle(286, 177, 286, -45))
        self.Map.append(Obstacle(161, -45, 286, -45))
        # Bridge3 walls
        self.Map.append(Obstacle(97, 7, 161, 7))
        self.Map.append(Obstacle(97, 41, 161, 41))
        # Bridge4 walls
        self.Map.append(Obstacle(-104, 12, -144, 12))
        self.Map.append(Obstacle(-104, 33, -144, 33))
        # Room6 walls
        self.Map.append(Obstacle(-144, 12, -144, 1))
        self.Map.append(Obstacle(-144, 33, -144, 70))
        self.Map.append(Obstacle(-144, 1, -182, 1))
        self.Map.append(Obstacle(-144, 70, -169, 70))
        self.Map.append(Obstacle(-169, 70, -169, 231))
        self.Map.append(Obstacle(-182, 1, -182, -41))
        self.Map.append(Obstacle(-169, 231, -296, 231))
        self.Map.append(Obstacle(-296, 231, -296, -41))
        self.Map.append(Obstacle(-296, -41, -230, -41))
        self.Map.append(Obstacle(-182, -41, -198, -41))
        # Bridge6 walls
        self.Map.append(Obstacle(-198, -41, -198, -95))
        self.Map.append(Obstacle(-230, -41, -230, -95))
        self.Map.append(Obstacle(-198, -95, -230, -95))
        # Add map to list
        self.Map.append(tMap(mapZoom))
        self.Interactions = []
        self.tmap = tMap(mapZoom)
        for map in self.Map:
            self.Interactions.append(MapInteraction(self.kbd, map))
        for obstacle in self.Map:
            self.Interactions.append(Interaction(obstacle, self.kbd, map))


    #####################################################################################
    def collide_check(self, wall, tMap, keyboard):
        if (((int(wall.startPos.x) == int(wall.endPos.x)) and ((CANVASWIDTH/2) - 7 < int(wall.startPos.x) < (CANVASWIDTH/2) + 7) and (
                int(wall.endPos.y) < CANVASHEIGHT/2 < int(wall.startPos.y) or int(wall.startPos.y) < CANVASHEIGHT/2 < int(wall.endPos.y)))):
            for wall in self.Map:
                if keyboard.left:
                    wall.vel.add(Vector(-1, 0))
                    tMap.vel.add(Vector(-1, 0))
                if keyboard.right:
                    wall.vel.add(Vector(1, 0))
                    tMap.vel.add(Vector(1, 0))
                if keyboard.down:
                    wall.vel.add(Vector(0, 1))
                    tMap.vel.add(Vector(0, 1))
                if keyboard.up:
                    wall.vel.add(Vector(0, -1))
                    tMap.vel.add(Vector(0, -1))
                #print("Collision handled")
            return True
        elif (((int(wall.startPos.y) == int(wall.endPos.y)) and ((CANVASHEIGHT/2) - 7 < int(wall.startPos.y) < (CANVASHEIGHT/2) + 7) and (
                int(wall.endPos.x) < CANVASWIDTH/2 < int(wall.startPos.x) or int(wall.startPos.x) < CANVASWIDTH/2 < int(wall.endPos.x)))):
            for wall in self.Map:
                if keyboard.left:
                    wall.vel.add(Vector(-1, 0))
                    tMap.vel.add(Vector(-1, 0))
                if keyboard.right:
                    wall.vel.add(Vector(1, 0))
                    tMap.vel.add(Vector(1, 0))
                if keyboard.down:
                    wall.vel.add(Vector(0, 1))
                    tMap.vel.add(Vector(0, 1))
                if keyboard.up:
                    wall.vel.add(Vector(0, -1))
                    tMap.vel.add(Vector(0, -1))
                #print("Collision handled")
            return True
        # print("False")
        return False

    ###################################################################################
    def draw(self, canvas):
        for inter in self.Interactions:
            inter.update()
        for map in self.Map:
            map.update()
            map.draw(canvas)
        for obstacle in self.Map:
            obstacle.update()
            obstacle.draw(canvas)
            self.collide_check(obstacle, self.tmap, self.kbd)
            # print(int(obstacle.startPos.x), int(obstacle.endPos.x), int(player.pos.x))
        player.update()
        player.draw(canvas)

if __name__ == '__main__':
    # Create a frame and assign callbacks to event handlers
    frame = simplegui.create_frame("Game", CANVASWIDTH, CANVASHEIGHT)
    test = Map()
    frame.set_draw_handler(test.draw)
    frame.set_keydown_handler(test.kbd.keyDown)
    frame.set_keyup_handler(test.kbd.keyUp)
    frame.start()

