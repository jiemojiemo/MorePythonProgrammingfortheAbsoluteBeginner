import pygame
import sys
import math

from pygame.locals import *

pygame.init()
pygame.display.set_caption("Drawing Arcs")

screen = pygame.display.set_mode((600,500))

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))

    color = 255,0,255
    position = 200,150,200,200
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    width = 8

    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    pygame.display.update()
