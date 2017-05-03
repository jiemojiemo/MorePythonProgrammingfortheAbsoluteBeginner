import pygame
from pygame.locals import *

import Snake
from Snake import *

import Food
from Food import *

import sys

def game_init():
    global screen, font, timer, backbuffer, snake
    global food_group

    pygame.init()
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((24*32, 18*32))
    font = pygame.font.Font(None, 30)
    timer = pygame.time.Clock()

    # create a drawing surface
    backbuffer = pygame.Surface((screen.get_rect().width, screen.get_rect().height))

    # create snake
    snake = Snake()

    # create food
    food_group = pygame.sprite.Group()
    food = Food()
    food_group.add(food)

# main program begins
game_init()
game_over = False
last_time = 0

V_UP = Point(0,-1)
V_DOWN = Point(0,1)
V_LEFT = Point(-1,0)
V_RIGHT = Point(1,0)

while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    #event section
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()
    elif keys[K_UP] or keys[K_w]:
        if snake.velocity.ne(V_DOWN):
            snake.velocity = V_UP
    elif keys[K_DOWN] or keys[K_s]:
        if snake.velocity.ne(V_UP):
            snake.velocity = V_DOWN
    elif keys[K_LEFT] or keys[K_a]:
        if snake.velocity.ne(V_RIGHT):
            snake.velocity = V_LEFT
    elif keys[K_RIGHT] or keys[K_d]:
        if snake.velocity.ne(V_LEFT):
            snake.velocity = V_RIGHT

    if not game_over:
        snake.update(ticks)
        food_group.update(ticks)

        # try to pick up food
        hit_list = pygame.sprite.groupcollide(snake.segments, food_group, False, True)
        if len(hit_list) > 0:
            food_group.add(Food())
            snake.add_segment()

    # see if head collides with body
    for i in range(1, len(snake.segments)):
        if pygame.sprite.collide_rect(snake.segments[0],\
            snake.segments[i]):
            game_over = True

    # check screen boundary
    x = snake.segments[0].X // 32
    y = snake.segments[0].Y // 32
    if x < 0 or x > 24 or y < 0 or y > 17:
        game_over = True

    backbuffer.fill((20,50,20))
    snake.draw(backbuffer)
    food_group.draw(backbuffer)

    screen.blit(backbuffer, (0,0))

    if not game_over:
        print_text(font, 0, 0, "Length " + str(len(snake.segments)))
        print_text(font, 0, 20, "Position " + str(snake.segments[0].X//32) + \
        "," + str(snake.segments[0].Y//32))
    else:
        print_text(font, 0, 0, "GAME OVER")

    pygame.display.update()
