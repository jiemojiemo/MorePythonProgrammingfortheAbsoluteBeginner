import sys
import random
import math
from datetime import datetime, date, time

import pygame
from pygame.locals import *

def wrap_angle(angle):
    return abs(angle % 360)

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

def draw_circle():
    pygame.draw.circle(screen, white, (pos_x, pos_y), radius, 6)

def draw_hour_hand():
    hourAngle = wrap_angle( hour*(360/12) - 90 )
    hourAngle = math.radians(hourAngle)
    hour_x = math.cos(hourAngle)*(radius - 80)
    hour_y = math.sin(hourAngle)*(radius - 80)
    target = (pos_x + hour_x, pos_y + hour_y)

    pygame.draw.line(screen, pink, (pos_x, pos_y), target, 25)

def draw_minute_hand():
    minAngle = wrap_angle( minute*(360/12) - 90 )
    minAngle = math.radians(minAngle)
    min_x = math.cos(minAngle)*(radius - 60)
    min_y = math.sin(minAngle)*(radius - 60)
    target = (pos_x + min_x, pos_y + min_y)

    pygame.draw.line(screen, orange, (pos_x, pos_y), target, 12)
def draw_second_hand():
    secAngle = wrap_angle( second*(360/12) - 90 )
    secAngle = math.radians(secAngle)
    sec_x = math.cos(secAngle)*(radius - 40)
    sec_y = math.sin(secAngle)*(radius - 40)
    target = (pos_x + sec_x, pos_y + sec_y)

    pygame.draw.line(screen, yellow, (pos_x, pos_y), target, 6)
def draw_hands():
    draw_hour_hand()
    draw_minute_hand()
    draw_second_hand()

# draw the clock numbers 1-12
def draw_numbers():
    for n in range(1,13):
        angle = math.radians( n*(360/12) - 90 )
        x = math.cos(angle)*(radius - 20) - 10
        y = math.sin(angle)*(radius - 20) - 10
        print_text(font, pos_x+x, pos_y+y, str(n))

def draw_clock():
    draw_circle()
    draw_numbers()
    draw_hands()
    #draw hands of clock

# init
pygame.init()
pygame.display.set_caption("Analog Clock")

screen = pygame.display.set_mode((600,500))
screen.fill((0,100,0))
font = pygame.font.Font(None, 36)

pos_x = 300
pos_y = 250
radius = 250
angle = 360

# color
white = 255,255,255
pink = 255,100,100
orange = 220,180,0
yellow = 255,255,0

# time
hour = 0
minute = 0
second = 0

# repeating loop
while True:
    for event in pygame.event.get():
        if event == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    screen.fill((0,0,100))

    today = datetime.today()
    hour = today.hour % 12
    minute = today.minute
    second = today.second

    draw_clock()
    print_text(font, 0, 0, str(hour)+":"+str(minute)+":"+str(second))
    pygame.display.update()
