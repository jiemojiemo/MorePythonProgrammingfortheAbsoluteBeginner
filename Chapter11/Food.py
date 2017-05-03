import pygame
import MyLibrary
from MyLibrary import *

import random

class Food(MySprite):
    def __init__(self):
        MySprite.__init__(self)

        image = pygame.Surface((32,32)).convert_alpha()
        image.fill((255,255,255,0))
        pygame.draw.circle(image, (250,250,50), (16,16), 16, 0)
        self.set_image(image)
        MySprite.update(self, 0, 30)
        self.X = random.randint(0, 23) * 32
        self.Y = random.randint(0, 17) * 32
