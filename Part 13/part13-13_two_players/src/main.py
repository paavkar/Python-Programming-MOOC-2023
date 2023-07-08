# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()
x = width-robot_width
y = height-robot_height

x2 = 0
y2 = 0

to_right = False
to_left = False
to_up = False
to_down = False

to_right2 = False
to_left2 = False
to_up2 = False
to_down2 = False

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
            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_w:
                to_up2 = True
            if event.key == pygame.K_s:
                to_down2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_w:
                to_up2 = False
            if event.key == pygame.K_s:
                to_down2 = False

        if event.type == pygame.QUIT:
            exit()
    
    x = max(x,0)
    x = min(x,width-robot_width)
    y = max(y,0)
    y = min(y,height-robot_height)
    x2 = max(x2,0)
    x2 = min(x2,width-robot_width)
    y2 = max(y2,0)
    y2 = min(y2,height-robot_height)

    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_up:
        y -= 2
    if to_down:
        y += 2
    
    if to_right2:
        x2 += 2
    if to_left2:
        x2 -= 2
    if to_up2:
        y2 -= 2
    if to_down2:
        y2 += 2
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)

### Example solution
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
# positions of robots
positions = [[0, 0],
          [width-robot.get_width(), height-robot.get_height()]]
 
controls = []
# key, which robot moves, horizontal movement, vertical movement
controls.append((pygame.K_LEFT, 0, -2, 0))
controls.append((pygame.K_RIGHT, 0, 2, 0))
controls.append((pygame.K_UP, 0, 0, -2))
controls.append((pygame.K_DOWN, 0, 0, 2))
controls.append((pygame.K_a, 1, -2, 0))
controls.append((pygame.K_d, 1, 2, 0))
controls.append((pygame.K_w, 1, 0, -2))
controls.append((pygame.K_s, 1, 0, 2))
 
clock = pygame.time.Clock()
 
key_pressed = {}
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_pressed[event.key] = True
 
        if event.type == pygame.KEYUP:
            del key_pressed[event.key]
 
        if event.type == pygame.QUIT:
            exit()
 
    for key in controls:
        if key[0] in key_pressed:
            positions[key[1]][0] += key[2]
            positions[key[1]][1] += key[3]
 
    screen.fill((0, 0, 0))
    for i in range(2):
        screen.blit(robot, (positions[i][0], positions[i][1]))
    pygame.display.flip()
 
    clock.tick(60)