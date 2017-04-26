import itertools
import sys
import time
import random
import math
import pygame

from pygame.locals import *
from MyLibrary import *

def calc_velocity(direction, vel=1.0):
    velocity = Point(0,0)
    if direction == 0: #north
        velocity.y = -vel
    elif direction == 2: #east
        velocity.x = vel
    elif direction == 4: #south
        velocity.y = vel
    elif direction == 6: # west
        velocity.x = -vel
    return velocity

def be_bound():
    if player.X < 0:
        player.X = 0
    elif player.X > 700:
        player.X = 700
    if player.Y < 0:
        player.Y = 0
    elif player.Y > 500:
        player.Y = 500

def move_player():
    player.X += player.velocity.x
    player.Y += player.velocity.y

def reverse_direction(sprite):
    if sprite.direction == 0:
        sprite.direction = 4
    elif sprite.direction == 2:
        sprite.direction = 6
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2

def draw_energy_bar():
    pygame.draw.rect(screen, (50,150,50), Rect(300,570,player_health*2,25))
    pygame.draw.rect(screen, (100,200,100), Rect(300,570,200,25), 2)

def update_player():
    player.first_frame = player.direction * player.colums
    player.last_frame = player.first_frame + player.colums - 1
    if player.frame < player.first_frame:
        player.frame = player.first_frame
        pass
    if not player_moving:
        #stop animating when player is not pressing a key
        player.frame = player.first_frame = player.last_frame
    else:
        #move player in direction
        player.velocity = calc_velocity(player.direction, 1.5)
        player.velocity.x *= 1.5
        player.velocity.y *= 1.5

    #manually move the player
    if player_moving:
        move_player()
        be_bound()
    player_group.update(ticks, 50)

def add_health():
    global health_group
    health = MySprite()
    health.load("health.png", 32, 32, 1)
    health.position = random.randint(0,700),random.randint(0,500)
    health_group.add(health)

def add_zombie_to_group():
    global zombie_group
    zombie = MySprite()
    zombie.load("zombie walk.png", 96, 96, 8)
    zombie.position = random.randint(0,700), random.randint(0,500)
    zombie.direction = random.randint(0,3) * 2
    zombie_group.add(zombie)


def update_zombie():
    global start_time
    now_time = time.clock()
    seconds = now_time - start_time
    if seconds > 10.0:
        add_zombie_to_group()
        start_time = now_time
    #manually iterate through all the zombies
    for z in zombie_group:
        #set the zombie's animation range
        z.first_frame = z.direction * z.colums
        z.last_frame = z.first_frame + z.colums - 1
        if z.frame < z.first_frame:
            z.frame = z.first_frame

        z.velocity = calc_velocity(z.direction)
        #keep the zombie on the screen
        z.X += z.velocity.x
        z.Y += z.velocity.y
        if z.X < 0 or z.X > 700 or z.Y < 0 or z.Y > 500:
            reverse_direction(z)

    zombie_group.update(ticks, 50)

def check_collistion_with_zombie():
    #check for collistion with zombies
    attacker = None
    attacker = pygame.sprite.spritecollideany(player, zombie_group)
    global player_health
    if attacker != None:
        #we got a hit, now do a more precise check
        if pygame.sprite.collide_rect_ratio(0.5)(player, attacker):
            player_health -= 10
            if attacker.X < player.X:
                attacker.X -= 10
            elif attacker.X > player.X:
                attacker.X += 10
        else:
            attacker = None

def update_health():
    health_group.update(ticks, 50)
    #check for collistion with health
    global player_health
    healther = None
    healther = pygame.sprite.spritecollideany(player, health_group)
    if healther != None:
        if pygame.sprite.collide_rect_ratio(0.5)(player, healther):
            player_health += 10
            if player_health > 100 : player_health = 100
            healther.X = random.randint(0,700)
            healther.Y = random.randint(0,500)

#main program begins
pygame.init()
pygame.display.set_caption("Zombie Mob Game")
screen = pygame.display.set_mode((800,600))
font = pygame.font.Font(None, 36)
timer = pygame.time.Clock()

#create sprite groups
player_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
health_group = pygame.sprite.Group()

#create player sprite
player = MySprite()
player.load("farmer walk.png", 96, 96, 8)
player.position = 80,80
player.direction = 4
player_group.add(player)

#create health sprite
for n in range(0,3):
    add_health()


player_moving = False
game_over = False
player_health = 100
start_time = time.clock()

#create zombie sprite
zombie_image = pygame.image.load("zombie walk.png").convert_alpha()
for n in range(0, 10):
    add_zombie_to_group()

while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()


    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    elif keys[K_UP] or keys[K_w]:
        player.direction = 0
        player_moving = True
    elif keys[K_RIGHT] or keys[K_d]:
        player.direction = 2
        player_moving = True
    elif keys[K_DOWN] or keys[K_s]:
        player.direction = 4
        player_moving = True
    elif keys[K_LEFT] or keys[K_a]:
        player.direction = 6
        player_moving = True
    else:
        player_moving = False

    if not game_over:
        update_player()
        update_zombie()
        check_collistion_with_zombie()
        update_health()

    if player_health <= 0:
        game_over = True

    screen.fill((50,50,100))

    player_group.draw(screen)
    zombie_group.draw(screen)
    health_group.draw(screen)

    #draw energy bar
    draw_energy_bar()

    if game_over:
        print_text(font, 300, 100, "G A M E  O V E R")

    pygame.display.update()
