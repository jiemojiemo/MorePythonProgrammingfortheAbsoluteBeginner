import sys
import random
import math

import pygame
from pygame.locals import *

# init
pygame.init()
pygame.display.set_caption("Circle Demo")

screen = pygame.display.set_mode((600,500))
screen.fill((0,100,0))

pos_x = 300
pos_y = 250
radius = 200
angle = 360

# repeating loop
while True:
    for event in pygame.event.get():
        if event == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    angle += 1
    if angle >= 360:
        angle = 0

    color = [random.randint(0,255) for _ in range(3)]
    x = math.cos( math.radians(angle) )*radius
    y = math.sin( math.radians(angle) )*radius

    pos = ( int(pos_x + x), int(pos_y + y) )
    pygame.draw.circle(screen, color, pos, 10, 0)

    pygame.display.update()
