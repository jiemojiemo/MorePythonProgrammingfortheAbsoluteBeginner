import pygame
import random
import sys

from pygame.locals import *

pygame.init()
pygame.display.set_caption("Random Lines")

screen = pygame.display.set_mode((600,500))

start_points = []
end_points = []

for i in range(0,1000):
    x = random.randint(0,600);
    y = random.randint(0,500);
    start_points.append((x,y))
    x = random.randint(0,600);
    y = random.randint(0,500);
    end_points.append((x,y))

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

        screen.fill((0,80,0))

        color = 100,255,200
        width = 2;
        for i in range(0, 1000):
            pygame.draw.line(screen,color,start_points[i],end_points[i],width)

        pygame.display.update()
            
