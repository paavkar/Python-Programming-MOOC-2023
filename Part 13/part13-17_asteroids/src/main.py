# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

pygame.display.set_caption("Asteroids")

robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")
game_font = pygame.font.SysFont("Arial", 24)

robot_width = robot.get_width()
robot_height = robot.get_height()

robot_x = width/2

to_left = False
to_right = False

points = 0

x_velocity = 0
rock_velocity = 1
rocks = []
number = 10
for i in range(number):
    rocks.append({"file": rock, "x": randint(100, width-rock.get_width()-50), "y": -randint(100,2000), "rock_velocity": rock_velocity})
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

    if to_right:
        robot_x += 5
    if to_left:
        robot_x -= 5

    window.fill((0,0,0))

    window.blit(robot, (robot_x, height-robot_height))
    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (width-text.get_width()-30, text.get_height()-10))

    for i in range(number):
        window.blit(rocks[i]["file"], (rocks[i]["x"], rocks[i]["y"]))
        rocks[i]["y"] = rocks[i]["y"] + rocks[i]["rock_velocity"]

        if(rocks[i]["x"] >= robot_x-robot_width/2 and rocks[i]["x"] <= robot_x+robot_width/2 and rocks[i]["y"]+rocks[i]["file"].get_height()/2 >= height-robot_height):
            points += 1
            rocks[i]["x"] = randint(20, width-rock.get_width()-50)
            rocks[i]["y"] = -randint(100,2000)

        ## Game starts over when player misses an asteroid
        #elif rocks[i]["y"]+rocks[i]["file"].get_height() == height:
            #rocks.clear()
            #for i in range(number):
                #rocks.append({"file": rock, "x": randint(20, width-rock.get_width()-50), "y": -randint(100,2000), "rock_velocity": rock_velocity})
            #points = 0
            #break
        ## Game ends (program closes) when player misses an asteroid
        elif rocks[i]["y"]+rocks[i]["file"].get_height() == height:
            exit()

    pygame.display.flip()
    clock.tick(60)