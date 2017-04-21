import sys
import pygame
import random

from pygame.locals import *


def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text,True, color)
    screen.blit(imgText, (x,y))

def draw_circle(x, y, radius, width = 0):
    pygame.draw.circle(screen, black, (x-4,int(y)-4), radius, width)
    pygame.draw.circle(screen, yellow, (x,int(y)), radius, width)

def draw_rect(x, y, )

pygame.init()
pygame.display.set_caption("Bomb Catching Game")

screen = pygame.display.set_mode((600,500))
font1 = pygame.font.Font(None, 24)
lives = 0
score = 0
black = 0,0,0
yellow = 255,255,0
while True:
    for event in pygame.event.get():
        if event == QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0,100,0))
    print_text(font1, 0, 0, "LIVES: " + str(lives))
    print_text(font1, 500, 0, "SCORE: " + str(score))

    draw_circle(250,300,20)

    pygame.display.update()
