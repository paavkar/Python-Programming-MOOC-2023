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
    window.blit(robot, (60+robot_width*i, 80))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()