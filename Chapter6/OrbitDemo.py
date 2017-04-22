import sys

import pygame
from pygame.locals import *

# init
pygame.init()
pygame.display.set_caption("Orbit Demo")
screen = pygame.display.set_mode((800,600))

# load bitmaps
space = pygame.image.load("space.bmp").convert_alpha()
planet = pygame.image.load("planet2.bmp").convert_alpha()

ship = pygame.image.load("freelance.bmp").convert_alpha()
width,height = ship.get_size()
ship = pygame.transform.scale(ship, (width//2,height//2))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    width,height = planet.get_size()
    screen.blit(space,(0,0))
    screen.blit(planet, (400-width/2,300-width/2))
    screen.blit(ship, (50,50))

    pygame.display.update()
