import pygame
from paddle import Paddle
from ball import Ball
from game import Game

w, h = 640, 400

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Breakout")

clock = pygame.time.Clock()

paddle = Paddle(x=200, y=380, w=80, h=20, color=(255, 255, 255))
ball = Ball(x=200, y=200, dx=6, dy=6, r=10, color=(255, 255, 255))
game = Game(w=w, h=h, paddle=paddle, ball=ball, n_bricks_x=4, n_bricks_y=3)

active = True
while active:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            active = False

        if event.type == pygame.MOUSEMOTION:
            paddle.move(event.pos)

    clock.tick(30)

    game.update(screen)
    game.draw(screen)
