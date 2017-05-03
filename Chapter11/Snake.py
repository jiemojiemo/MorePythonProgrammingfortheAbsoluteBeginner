import MyLibrary
from MyLibrary import *

import pygame

class SnakeSegment(MySprite):
    def __init__(self, color=(20,200,20)):
        MySprite.__init__(self)

        image = pygame.Surface((32,32)).convert_alpha()
        image.fill((255,255,255,0))
        pygame.draw.circle(image, color, (16,16), 16, 0)
        self.set_image(image)
        MySprite.update(self, 0, 30)

class Snake():
    def __init__(self):
        self.velocity = Point(-1, 0)
        self.old_time = 0
        # create snake head
        head = SnakeSegment((50,250,50))
        head.X = 12*32
        head.Y = 9*32
        # create a list for segments
        self.segments = list()
        self.segments.append(head)
        # add some segments
        self.add_segment()
        self.add_segment()

    def add_segment(self):

        '''
        self.move_segments()
        last = len(self.segments) - 1
        segment = SnakeSegment()
        pos = Point(self.segments[last].X, self.segments[last].Y)
        segment.X = pos.x
        segment.Y = pos.y
        self.segments.append(segment)
        '''

        last = len(self.segments) - 1
        segment = SnakeSegment()
        start = Point(0,0)


        if self.velocity.x < 0: #  left
            start.x = 32
        elif self.velocity.x > 0: #  right
            start.x = -32

        if self.velocity.y < 0: #  up
            start.y = 32
        elif self.velocity.y > 0: #  down
            start.y = -32

        segment.X = self.segments[last].X + start.x
        segment.Y = self.segments[last].Y + start.y

        self.segments.append(segment)

    def move_segments(self):
        # auto move body segments
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].X = self.segments[i-1].X
            self.segments[i].Y = self.segments[i-1].Y
        # move snake head
        self.segments[0].X += self.velocity.x * 32
        self.segments[0].Y += self.velocity.y * 32


    def update(self, ticks, rate=400):
        if ticks > self.old_time + rate:
            self.old_time = ticks
            self.move_segments()

    def draw(self, surface):
        for segment in self.segments:
            surface.blit(segment.image, (segment.X, segment.Y))
