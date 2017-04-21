import sys
import pygame
import random
import time
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

# main program begins
pygame.init()
pygame.display.set_caption("Keyboard Demo")

screen = pygame.display.set_mode((600,500))
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 200)

white = 255,255,255
yellow = 255,255,0

key_flag = False # key down or not
correct_answer = 97 # 'a'
score = 0 # score will increase by 1 if you get correct answer
game_over = True
seconds = 11
clock_start = 0
current = 0
speed = 0

# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            key_flag = True
        elif event.type ==  KEYUP:
            key_flag = False

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        if keys[K_RETURN]:
            if game_over:
                game_over = False
                score = 0
                seconds = 11
                clock_start = time.clock()

        current = time.clock() - clock_start
        speed = score * 6
        if current > seconds:
            game_over = True
        elif current <= 10:
            if keys[correct_answer]:
                correct_answer = random.randint(97,122)
                score += 1


    screen.fill((0,100,0))

    print_text(font1, 0, 0, "Let's see how fast you can type!")
    print_text(font1, 0, 20, "Try to keep up for 10 seconds...")

    if key_flag:
        print_text(font1, 500, 0, "<key>")

    if game_over:
        print_text(font1, 0, 160, "Press Enter to start...")
    if not game_over:
        print_text(font1, 0, 80, "Time: " + str(int(seconds - current)))

    print_text(font1, 0, 100, "Speed: " + str(speed) + " letters/min")

    print_text(font2, 0, 240, chr(correct_answer-32))

    pygame.display.update()
