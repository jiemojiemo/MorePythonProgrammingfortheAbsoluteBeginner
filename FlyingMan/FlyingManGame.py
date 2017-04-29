import MyLibrary
from MyLibrary import *

import pygame
from pygame.locals import *

import sys

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
MAN_FALL_SPEED = 2
MAN_FLY_SPEEN = -10
BLOCK_MOVE_SPEEN = 2


def reset_velocity():
    global flyingman
    flyingman.velocity = Point(0,MAN_FLY_SPEEN)

def update_velocity():
    global flyingman
    if flyingman.velocity.y > MAN_FALL_SPEED:
        flyingman.velocity.y = MAN_FALL_SPEED
    else:
        flyingman.velocity.y += MAN_FALL_SPEED

def update_flyingman():
    global flyingman
    global game_over
    flyingman.Y += flyingman.velocity.y
    update_velocity()

    if flyingman.Y > WINDOW_HEIGHT or flyingman.Y < 0:
        game_over = True

def move_walls():
    out_of_screen = False
    for blocks in wall_group:
        blocks.X -= BLOCK_MOVE_SPEEN
        if blocks.X+blocks.frame_width < 0:
            wall_group.remove(blocks)
            out_of_screen = True

    return out_of_screen

def add_new_wall(i):
    n_above_blocks = random.randint(1,need_blocks-1)
    n_bellow_blocks = need_blocks - n_above_blocks
    for j in range(0,n_above_blocks):
        block = MySprite()
        block.set_image(block_image)
        block.position = WINDOW_WIDTH/3+i*wall_space, j*block.frame_height
        wall_group.add(block)

    for j in range(1,n_bellow_blocks+1):
        block = MySprite()
        block.set_image(block_image)
        block.position = WINDOW_WIDTH/3+i*wall_space, WINDOW_HEIGHT - j*block.frame_height
        wall_group.add(block)  
    
def update_walls():
    out_of_screen = move_walls()
    if out_of_screen:
        add_new_wall(4)

def collision_man_wall():
    global game_over
    hit_block = pygame.sprite.spritecollideany(flyingman, wall_group)
    if hit_block != None:
        if pygame.sprite.collide_rect_radio(0.5)(flyingman, hit_block):
            game_over = True
    
# init
pygame.init()
pygame.display.set_caption("Flying Man Game")
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.mouse.set_visible(False)

# create group
flyingman_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

# create flying man
flyingman = MySprite()
flyingman.load("flyingman.bmp", 50, 64, 8)
flyingman.first_frame = 1
flyingman.last_frame = 7
flyingman.position = WINDOW_WIDTH/7, WINDOW_HEIGHT/2
flyingman_group.add(flyingman)

# create blocks
block_image = pygame.image.load("block.bmp")
block_width, block_height = block_image.get_size()
total_blocks = WINDOW_HEIGHT // block_height
space_blocks = flyingman.frame_height//block_height + random.randint(5,8)
need_blocks = total_blocks - space_blocks

# create above blocks
wall_space = 400
n_walls = 5
for i in range(0,n_walls):
    add_new_wall(i)

timer = pygame.time.Clock()
game_over = False

while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                reset_velocity()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0,100,0))

    if not game_over:
        update_flyingman()
        update_walls()
        collision_man_wall()
        
    
    flyingman_group.update(ticks,50)
    wall_group.update(ticks, 50)

    flyingman_group.draw(screen)
    wall_group.draw(screen)

    pygame.display.update()
    
