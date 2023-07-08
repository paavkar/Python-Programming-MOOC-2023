# WRITE YOUR SOLUTION HERE:
import pygame
import time

pygame.init()
width, height = 640, 480
display = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

hour = time.localtime().tm_hour
minute = time.localtime().tm_min
#second = time.localtime().tm_sec

x = width/2
y = height/2-180
print(x)
print(y)

second = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    pygame.display.set_caption(f"{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}")
    display.fill((0, 0, 0))

    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    #second = time.localtime().tm_sec

    pygame.draw.circle(display, (255, 0, 0), (width/2, height/2), height/2-40, 5)
    pygame.draw.circle(display, (255, 0, 0), (width/2, height/2), 10)
    print(second)
    if(second == 0):
        x = width/2
        y = height/2-180
        pygame.draw.line(display, (0, 0, 255), (width/2, height/2), (x, y))
        print("x and y at 0",x, y)
    if(second < 15 and x > 0):
        x += 11
        y += 11
        print(x, y)
        pygame.draw.line(display, (0, 0, 255), (width/2, height/2), (x, y))
    if(second == 15):
        x = width/2+180
        y = height/2
        print("x and y at 15",x, y)
        pygame.draw.line(display, (0, 0, 255), (width/2, height/2), (x, y))
    if(second > 15 and second < 30):
        x -= 12
        y += 12
        print(x, y)
        pygame.draw.line(display, (0, 0, 255), (width/2, height/2), (x, y))
    if(second == 30):
        x = width/2
        y = height/2+180
        print("x and y at 30",x, y)
        pygame.draw.line(display, (0, 0, 255), (width/2, height/2), (x, y))
    if(second > 30 and second < 45):
        x -= 12
        y -= 12
        print(x, y)
        pygame.draw.line(display, (0, 0, 255), (width/2, height/2), (x, y))
    if(second == 45):
        x = width/2-180
        y = height/2
        print("x and y at 45",x, y)
        pygame.draw.line(display, (0, 0, 255), (width/2, height/2), (x, y))
    if(second > 45 and second <= 59):
        x += 13
        y -= 13
        print(x, y)
        pygame.draw.line(display, (0, 0, 255), (width/2, height/2), (x, y))
    pygame.draw.line(display, (0, 0, 255), (width/2, height/2), (width/2+100, height/2-140), 2)
    pygame.draw.line(display, (0, 0, 255), (width/2, height/2), (width/2-100, height/2-80), 4)

    pygame.display.flip()
    second += 1
    if(second >=59):
        second = 0
    clock.tick(1)