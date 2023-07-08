# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.png")

ball_width = ball.get_width()
ball_height = ball.get_height()

x_speed = 2
y_speed = 2
x = width/2
y = height/2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x += x_speed
    y += y_speed
    if(x == 0 or x+ball_width == width):
        x_speed = -x_speed
    if(y == 0 or y+ball_height == height):
        y_speed = -y_speed
    
    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    clock.tick(60)