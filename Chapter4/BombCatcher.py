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

def draw_rect(x, y, width, height, line_width=0):
    # line_width = 0 for solid rectangle
    pygame.draw.rect(screen, black, (x-4, y-4, width, height), line_width)
    pygame.draw.rect(screen, red, (x, y, width, height), line_width)

# init
pygame.init()
pygame.display.set_caption("Bomb Catching Game")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((600,500))
font1 = pygame.font.Font(None, 24)

lives = 3
score = 0
gameOver = False

# colors
black = 0,0,0
yellow = 255,255,0
red = 255,0,0

# mouse position
mouse_x = 0
mouse_y = 0
# mouse relative movement
move_x = 0
move_y = 0

# bomb position: x is random value in range(0, 500), 500 is window width
bomb_x = random.randint(0,500)
bomb_y = -50

pos_x = 300
pos_y = 460

# velocity of bomb
vel_y = 0.7





while True:
    for event in pygame.event.get():
        if event == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            move_x, move_y = event.rel
        elif event.type == MOUSEBUTTONUP:
            if gameOver:
                gameOver = False
                lives = 3
                score = 0

    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0,100,0))
    print_text(font1, 0, 0, "LIVES: " + str(lives))
    print_text(font1, 500, 0, "SCORE: " + str(score))

    if gameOver:
        print_text(font1, 100, 200, "<CLICK TO PLAY>")
    else:
        bomb_y += vel_y
        # out of the window, failed to catch the bomb
        if bomb_y > 500:
            bomb_x = random.randint(0, 500)
            bomb_y = -50
            lives -= 1
            if lives == 0:
                gameOver = True
        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 120:
                score += 10
                bomb_x = random.randint(0,500)
                bomb_y = -50


    draw_circle(bomb_x, bomb_y, 30)

    # set basket position
    pos_x = mouse_x
    if pos_x < 0:
        pos_x = 0
    elif pos_x > 500:
        pos_x = 500
    draw_rect(pos_x, pos_y, 120, 40)

    pygame.display.update()
