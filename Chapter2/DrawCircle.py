import pygame
import sys
from pygame.locals import *


pygame.init()
pygame.display.set_caption("Drawing Circle")
screen = pygame.display.set_mode((600,500))



while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
            
    blue = 0,0,255
    color = 255,255,0
    position = 300, 250
    radius = 100
    width = 10
    
    screen.fill(blue)
    pygame.draw.circle(screen, color, position, radius, width)
    
    pygame.display.update()

