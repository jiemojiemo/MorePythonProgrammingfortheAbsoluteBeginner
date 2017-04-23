import sys
import math
import pygame
from pygame.locals import *

class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x
    def setx(self, x):
        self.__x = x
    x = property(getx, setx)

    def gety(self):
        return self.__y
    def sety(self, y):
        self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
        ",Y:" + "{:.0f}".format(self.__y) + "}"

def print_text(font, x, y, text, color=(255,255,255)):
    img_text = font.render(text, True, color)
    screen.blit(img_text, (x,y))

def wrap_angle(angle):
    return angle % 360

# init
pygame.init()
pygame.display.set_caption("Orbit Demo")
screen = pygame.display.set_mode((800,600))
font = pygame.font.Font(None, 24)

# load bitmaps
space = pygame.image.load("space.png").convert_alpha()
planet = pygame.image.load("planet2.png").convert_alpha()

ship = pygame.image.load("freelance.png").convert_alpha()
width,height = ship.get_size()
ship = pygame.transform.smoothscale(ship, (width//2,height//2))

radius = 250
angle = 0.0
pos = Point(0,0)
old_pos = Point(0,0)
vel_r = 0.1


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_1]:
        vel_r += 0.05
    if keys[K_2]:
        vel_r -= 0.05


    #draw background
    screen.blit(space,(0,0))

    #draw planet
    width,height = planet.get_size()
    screen.blit(planet, (400-width/2,300-width/2))

    #move the ship
    angle = wrap_angle(angle - vel_r)
    pos.x = math.cos(math.radians(angle))*radius
    pos.y = math.sin(math.radians(angle))*radius
    #rotate the ship
    delta_x = (pos.x - old_pos.x)
    delta_y = (pos.y - old_pos.y)
    rangle = math.atan2(delta_y, delta_x)
    rangled = wrap_angle(-math.degrees(rangle))
    scratch_ship = pygame.transform.rotate(ship, rangled)
    #draw the ship
    width, height = scratch_ship.get_size()
    x = 400+pos.x-width//2
    y = 300+pos.y-height//2
    screen.blit(scratch_ship, (x,y))

    print_text(font, 0, 0, "Orbit: " + "{:.0f}".format(angle))
    print_text(font, 0, 20, "Rotation: " + "{:.2f}".format(rangle))
    print_text(font, 0, 40, "Position: " + str(pos))
    print_text(font, 0, 60, "Old Pos: " + str(old_pos))

    pygame.display.update()
    old_pos.x = pos.x
    old_pos.y = pos.y
