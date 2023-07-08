# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()
x = width/2-robot_width/2
y = height/2-robot_height/2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(event.pos[0] <= x+robot_width/2+18 and event.pos[0] >= x+robot_width/2-18 and event.pos[1] <= y+robot_height/2+40 and event.pos[1] >= y-robot_height/2+50):
                x = randint(0, width-robot_width)
                y = randint(0, height-robot_height)

                window.fill((0, 0, 0))
                window.blit(robot, (x, y))
                pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    clock.tick(60)

### Example solution
if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
 
            hit_x = mouse_x >= x and mouse_x <= x+robot.get_width()
            hit_y = mouse_y >= y and mouse_y <= y+robot.get_height()
 
            if hit_x and hit_y:
                x = randint(0, width-robot.get_width())
                y = randint(0, height-robot.get_height())