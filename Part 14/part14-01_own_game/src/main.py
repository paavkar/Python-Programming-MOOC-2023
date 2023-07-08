# Complete your game here
import pygame
from random import randint

class MonsterEvaderCoinCollect:
    def __init__(self):
        pygame.init()
        
        self.load_images()

        self.points = 0
        self.game_over = False
        self.new_game_cond = True

        self.window_width = 640
        self.window_height = 480

        self.set_coordinates()

        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        self.game_font = pygame.font.SysFont("Arial", 24)

        pygame.display.set_caption("Own game")
        self.main_loop()

    def set_coordinates(self):
        self.coin_x = randint(0+self.coin.get_width(), self.window_width-self.coin.get_width())
        self.coin_y = randint(0+self.coin.get_height(), self.window_height-self.coin.get_height())
        self.x = self.window_width/2-self.robot.get_width()/2
        self.y = self.window_height/2-self.robot.get_height()/2
        self.monster_x = 0
        self.monster_y = 0

    def load_images(self):
        self.coin = pygame.image.load("coin.png")
        self.robot = pygame.image.load("robot.png")
        self.monster = pygame.image.load("monster.png")

    def main_loop(self):
        clock = pygame.time.Clock()
        self.x_speed = 2
        self.y_speed = 2
        if(self.new_game_cond):
            self.new_game_screen()
        while True:
            self.check_events()
            self.monster_movement()
            self.check_coin()
            self.check_monster()
            self.draw_window()
            clock.tick(60)

    def monster_movement(self):
        self.monster_x += self.x_speed
        self.monster_y += self.y_speed
        if(self.monster_x == 0 or self.monster_x+self.monster.get_width() == self.window_width):
            self.x_speed = -self.x_speed
        if(self.monster_y == 0 or self.monster_y+self.monster.get_height() == self.window_height):
            self.y_speed = -self.y_speed

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if(self.game_over or self.new_game_cond):
                    if event.key == pygame.K_SPACE:
                        self.new_game()
                if event.key == pygame.K_LEFT:
                    self.move(-20, 0)
                if event.key == pygame.K_RIGHT:
                    self.move(20, 0)
                if event.key == pygame.K_UP:
                    self.move(0, -20)
                if event.key == pygame.K_DOWN:
                    self.move(0, 20)
                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.QUIT:
                exit()
    
    def move(self, x: int, y: int):
        if(self.x+x >= 0 and self.x+self.robot.get_width()+x <= self.window_width):
            self.x += x
        if(self.y+y >= 0 and self.y+self.robot.get_height()+y <= self.window_height):
            self.y += y

    def check_coin(self):
        if(self.coin_y <= self.y+self.robot.get_height() and self.coin_y+self.coin.get_height() >= self.y):
            if(self.coin_x <= self.x+self.robot.get_width() and self.coin_x+self.coin.get_width() >= self.x):
                self.coin_x = randint(0+self.coin.get_width(), self.window_width-self.coin.get_width())
                self.coin_y = randint(0+self.coin.get_height(), self.window_height-self.coin.get_height())
                self.points += 1
                self.window.blit(self.coin, (self.coin_x, self.coin_y))

    def check_monster(self):
        if(self.monster_y+self.monster.get_height()/2+10 >= self.y and self.monster_y+10 <= self.y+self.robot.get_height()):
            if(self.monster_x <= self.x+self.robot.get_width()/2 and self.monster_x+self.monster.get_width()/2 >= self.x):
                self.game_over_screen()

    def game_over_screen(self):
        self.game_over = True
        text = self.game_font.render(f"Game Over!", True, (0, 0, 0))
        text3 = self.game_font.render(f"Pres Space to start a new game", True, (0, 0, 0))
        self.window.blit(text, (self.window_width/2-text.get_width(), self.window_height/2-text.get_height()))
        self.window.blit(text3, (self.window_width/2-text3.get_width(), self.window_height/2+text3.get_height()))
        pygame.display.flip()
        while True:
            self.check_events()

    def new_game_screen(self):
        self.new_game_cond = True
        self.window.fill((0,120,0))
        text = self.game_font.render(f"Collect coins and avoid the monster", True, (0, 0, 0))
        text3 = self.game_font.render(f"Pres Space to start a new game", True, (0, 0, 0))
        self.window.blit(text, (self.window_width/2-text.get_width(), self.window_height/2-text.get_height()))
        self.window.blit(text3, (self.window_width/2-text3.get_width(), self.window_height/2+text3.get_height()))
        pygame.display.flip()
        while True:
            self.check_events()

    def new_game(self):
        self.new_game_cond = False
        self.game_over = False
        self.x_speed = 2
        self.y_speed = 2
        
        self.set_coordinates()
        self.points = 0
        self.main_loop()

    def draw_window(self):
        self.window.fill((0,120,0))

        self.window.blit(self.robot, (self.x, self.y))
        
        text = self.game_font.render(f"Points: {self.points}", True, (0, 0, 0))
        self.window.blit(text, (self.window_width-text.get_width()-30, text.get_height()-10))
        self.window.blit(self.coin, (self.coin_x, self.coin_y))
        self.window.blit(self.monster, (self.monster_x, self.monster_y))
        pygame.display.flip()

    
if __name__ == "__main__":
    MonsterEvaderCoinCollect()