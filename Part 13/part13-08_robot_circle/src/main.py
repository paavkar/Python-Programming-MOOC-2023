# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

robot_width = robot.get_width()
robot_height = robot.get_height()

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    for i in range(10):
        x = width/2+math.cos(angle + i * math.pi * 2 / 10)*130-robot.get_width()/2
        y = height/2+math.sin(angle + i * math.pi * 2 / 10)*130-robot.get_height()/2
        window.blit(robot, (x, y))
    pygame.display.flip()

    angle += 0.01

    clock.tick(60)

### Example solution
import pygame
import math
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
angle = 0
radius = 150
number = 10
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    screen.fill((0, 0, 0))
    for i in range(number):
        x = width/2+math.cos(angle+2*math.pi*i/number)*radius-robot.get_width()/2
        y = height/2+math.sin(angle+2*math.pi*i/number)*radius-robot.get_height()/2
        screen.blit(robot, (x, y))
    pygame.display.flip()
 
    angle += 0.01
    clock.tick(60)