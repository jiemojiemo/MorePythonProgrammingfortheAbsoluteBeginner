import math
import pygame
import sys

from pygame.locals import *

pygame.init()
pygame.display.set_caption("The Pie Game - Press 1,2,3,4")

screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None, 60)

color = 200,80,60
width = 4
x = 300
y = 250
radius = 200
position = x-radius, y-radius, 2*radius, 2*radius

p1 = False
p2 = False
p3 = False
p4 = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                p1 = True
            elif event.key == pygame.K_2:
                p2 = True
            elif event.key == pygame.K_3:
                p3 = True
            elif event.key == pygame.K_4:
                p4 = True


        screen.fill((0,0,200))

        textImage1 = myfont.render("1", True, color);
        screen.blit(textImage1, (x+radius/2-20, y-radius/2))

        textImage2 = myfont.render("2", True, color);
        screen.blit(textImage2, (x-radius/2, y-radius/2))

        textImage3 = myfont.render("3", True, color);
        screen.blit(textImage3, (x-radius/2, y+radius/2-20))

        textImage4 = myfont.render("4", True, color);
        screen.blit(textImage4, (x+radius/2-20, y+radius/2-20))

        if p1:
            start_angle = math.radians(0)
            end_angle = math.radians(90)
            pygame.draw.arc(screen, color, position, start_angle,end_angle,width)
            pygame.draw.line(screen, color, (x,y), (x,y-radius), width)
            pygame.draw.line(screen, color, (x,y), (x+radius,y), width)
        if p2:
            start_angle = math.radians(90)
            end_angle = math.radians(180)
            pygame.draw.arc(screen, color, position, start_angle,end_angle,width)
            pygame.draw.line(screen, color, (x,y), (x,y-radius), width)
            pygame.draw.line(screen, color, (x,y), (x-radius,y), width)
        if p3:
            start_angle = math.radians(180)
            end_angle = math.radians(270)
            pygame.draw.arc(screen, color, position, start_angle,end_angle,width)
            pygame.draw.line(screen, color, (x,y), (x-radius,y), width)
            pygame.draw.line(screen, color, (x,y), (x,y+radius), width)
        if p4:
            start_angle = math.radians(270)
            end_angle = math.radians(360)
            pygame.draw.arc(screen, color, position, start_angle,end_angle,width)
            pygame.draw.line(screen, color, (x,y), (x,y+radius), width)
            pygame.draw.line(screen, color, (x,y), (x+radius,y), width)

        if p1 and p2 and p3 and p4:
            color = 0,255,0

        pygame.display.update()
    












        
