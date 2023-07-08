# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

robot_width = robot.get_width()
robot_height = robot.get_height()

window.fill((0,0,0))
for i in range(10):
    for j in range(10):
        window.blit(robot, (20+10*i+40*j, 100+i*20))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()