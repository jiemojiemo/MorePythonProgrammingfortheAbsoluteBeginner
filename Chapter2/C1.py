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
    radius = 100
    width = 10
    
    screen.fill(blue)
    pygame.draw.ellipse(screen, color,(300,200,40,80), width)
    
    pygame.display.update()

