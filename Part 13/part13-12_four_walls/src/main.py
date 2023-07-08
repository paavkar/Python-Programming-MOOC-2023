# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()
x = width/2-robot_width/2
y = height/2-robot_height/2

to_right = False
to_left = False
to_up = False
to_down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False

        if event.type == pygame.QUIT:
            exit()
    
    if(y <= 0):
        to_up = False
    if(y+robot_height >= height):
        to_down = False
    if(x <= 0):
        to_left = False
    if(x+robot_width >= width):
        to_right = False

    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_up:
        y -= 2
    if to_down:
        y += 2
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)

### Example solution
x = max(x,0)
x = min(x,width-robot.get_width())
y = max(y,0)
y = min(y,height-robot.get_height())