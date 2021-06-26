from pygame import *
from random import choice

PLATFORM_WIDTH = 52
PLATFORM_HEIGHT = 52
PLATFORM_COLOR = "#FF6262"


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        name = choice(["/home/andreacat/pocketPyme/rpg-template-master/images/props_tree.png", "/home/andreacat/pocketPyme/rpg-template-master/images/props_tree_group.png"])
        self.image = image.load(name)
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())

##~/pocketPyme/rpg-template-master/
class Ground(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("/home/andreacat/pocketPyme/rpg-template-master/images/bg.png")
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())


class Stone(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("/home/andreacat/pocketPyme/rpg-template-master/images/props_big_stone.png")
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())


class Water(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("/home/andreacat/pocketPyme/rpg-template-master/images/water.png")
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())


class Coin(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("/home/andreacat/pocketPyme/rpg-template-master/images/ui_coin.png")
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())


class edi(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("/home/andreacat/pocketPyme/rpg-template-master/images/pngs/edificio1.png")
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())
