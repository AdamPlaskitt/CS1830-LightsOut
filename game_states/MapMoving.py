from game_states.user303_0QT2noFSwD_0 import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

CANVASHEIGHT = 614
CANVASWIDTH = 614
MIN_RAD = 1
img = simplegui.load_image('https://raw.githubusercontent.com/Bill-Ferny/CS1830-LightsOut/master/gameMap.jpg')
imgCentre = Vector(307, 307)
mapZoom = 2


class Player:
    def __init__(self):
        self.pos = Vector(CANVASWIDTH / 2, CANVASHEIGHT / 2)
        self.vel = Vector()
        self.radius = 10
        self.colour = 'Green'

    def draw(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.radius, 1, self.colour, self.colour)

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)


player = Player()


class Obstacle:
    def __init__(self, x1, y1, x2, y2):
        self.startPos = imgCentre.copy().add(Vector(x1, y1).multiply(mapZoom))
        self.endPos = imgCentre.copy().add(Vector(x2, y2).multiply(mapZoom))
        self.vel = Vector()
        self.colour = 'Blue'

    def draw(self, canvas):
        canvas.draw_line(self.startPos.getP(), self.endPos.getP(), 7, self.colour)

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
    def __init__(self, obstacle, keyboard):
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
            # self.obstacle.vel.add(Vector(0.1, 0))
            self.tMap.vel.add(Vector(0.1, 0))
        if self.keyboard.right:
            # self.obstacle.vel.add(Vector(-0.1, 0))
            self.tMap.vel.add(Vector(-0.1, 0))
        if self.keyboard.down:
            # self.obstacle.vel.add(Vector(0, -0.1))
            self.tMap.vel.add(Vector(0, -0.1))
        if self.keyboard.up:
            # self.obstacle.vel.add(Vector(0, 0.1))
            self.tMap.vel.add(Vector(0, 0.1))


class tMap:
    def __init__(self, zoom):
        self.vel = Vector()
        self.source = img
        self.centreSource = Vector(307, 307)
        self.dimSource = Vector(614, 614)
        self.moveP = Vector(307, 307)
        self.imgZoom = Vector(614 * zoom, 614 * zoom)

    def draw(self, canvas):
        canvas.draw_image(img, self.centreSource.getP(), self.dimSource.getP(), self.moveP.getP(), self.imgZoom.getP())

    def update(self):
        self.moveP.add(self.vel)
        self.vel.multiply(0.85)

    def collide_check(walls):

        for x1, y1, x2, y2 in Obstacle.:
            if Obstacle.startPos.x <= player.pos.x <= Obstacle.endPos.x and Obstacle.startPos.y <= player.pos.y <= Obstacle.endPos.y:
                print("collide with wall (" +  + ", " + y1 + ")" + "(" + x2 + ", " + y2 + ")")
                return True
        return False


kbd = Keyboard()

Map = []
# Add map to list
Map.append(tMap(mapZoom))
# Room1 walls
Map.append(Obstacle(-105, -32, -6, -32))
Map.append(Obstacle(32, -32, 97, -32))
Map.append(Obstacle(97, -32, 97, 7))
Map.append(Obstacle(97, 41, 97, 93))
Map.append(Obstacle(97, 93, 93, 93))
Map.append(Obstacle(54, 93, -104, 93))
Map.append(Obstacle(-104, 93, -104, 33))
Map.append(Obstacle(-104, 12, -104, -32))
# Room2 walls
Map.append(Obstacle(54, 137, -140, 137))
Map.append(Obstacle(92, 137, 130, 137))
Map.append(Obstacle(-140, 137, -140, 300))
Map.append(Obstacle(-140, 300, 130, 300))
Map.append(Obstacle(130, 137, 130, 300))
# Bridge1 walls
Map.append(Obstacle(54, 93, 54, 137))
Map.append(Obstacle(93, 93, 93, 137))
# Water feature walls
Map.append(Obstacle(-45, 175, 54, 175))
Map.append(Obstacle(-45, 268, 54, 268))
Map.append(Obstacle(-45, 175, -45, 268))
Map.append(Obstacle(54, 175, 54, 268))
# Room3 walls
Map.append(Obstacle(-6, -73, -151, -73))
Map.append(Obstacle(32, -73, 59, -73))
Map.append(Obstacle(-151, -73, -151, -237))
Map.append(Obstacle(-151, -237, 59, -237))
Map.append(Obstacle(59, -237, 59, -178))
Map.append(Obstacle(59, -158, 59, -73))
# Bridge2 walls
Map.append(Obstacle(-6, -73, -6, -32))
Map.append(Obstacle(32, -73, 32, -32))
# Bridge5 walls
Map.append(Obstacle(59, -178, 99, -178))
Map.append(Obstacle(59, -158, 99, -158))
# Room4 walls
Map.append(Obstacle(99, -178, 99, -226))
Map.append(Obstacle(99, -158, 99, -80))
Map.append(Obstacle(99, -80, 252, -80))
Map.append(Obstacle(252, -80, 252, -226))
Map.append(Obstacle(252, -226, 99, -226))
# Room5 walls
Map.append(Obstacle(161, 7, 161, -45))
Map.append(Obstacle(161, 41, 161, 177))
Map.append(Obstacle(161, 177, 286, 177))
Map.append(Obstacle(286, 177, 286, -45))
Map.append(Obstacle(161, -45, 286, -45))
# Bridge3 walls
Map.append(Obstacle(97, 7, 161, 7))
Map.append(Obstacle(97, 41, 161, 41))
# Bridge4 walls
Map.append(Obstacle(-104, 12, -144, 12))
Map.append(Obstacle(-104, 33, -144, 33))
# Room6 walls
Map.append(Obstacle(-144, 12, -144, 1))
Map.append(Obstacle(-144, 33, -144, 70))
Map.append(Obstacle(-144, 1, -182, 1))
Map.append(Obstacle(-144, 70, -169, 70))
Map.append(Obstacle(-169, 70, -169, 231))
Map.append(Obstacle(-182, 1, -182, -41))
Map.append(Obstacle(-169, 231, -296, 231))
Map.append(Obstacle(-296, 231, -296, -41))
Map.append(Obstacle(-296, -41, -230, -41))
Map.append(Obstacle(-182, -41, -198, -41))
# Bridge6 walls
Map.append(Obstacle(-198, -41, -198, -95))
Map.append(Obstacle(-230, -41, -230, -95))
Map.append(Obstacle(-198, -95, -230, -95))
Interactions = []
map = tMap(mapZoom)
for map in Map:
    Interactions.append(MapInteraction(kbd, map))
for obstacle in Map:
    Interactions.append(Interaction(obstacle, kbd))


def collide_check(Obstacle):
   for x1, y1, x2, y2 in Obstacle:
        if x1<= player.pos.x <= x2 and y1 <= player.pos.y <= y2:
            print("collide with wall (" + x1 + ", "+ y1+")" + "(" + x2 + ", "+ y2+")")
            return True
   return False


def draw(canvas):
    for inter in Interactions:
        inter.update()
    for map in Map:
        map.collide_check(Obstacle)
        map.update()
        map.draw(canvas)
    for obstacle in Map:
        obstacle.update()
        obstacle.draw(canvas)
    player.update()
    player.draw(canvas)


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Game", CANVASWIDTH, CANVASHEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()

