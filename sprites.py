# File created by: Diego Avila

import pygame as pg

from pygame.sprite import Sprite

from settings import *

vec = pg.math.Vector2

# create a player

class Player(Sprite):
    def _init_(self):
        Sprite._init_(self)
        self.image = pg.Surface