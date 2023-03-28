import time
import pygame
import sys
import random

class Snake:
    def __init__(self):
        self.body = [pygame.math.Vector2(3,5),pygame.math.Vector2(2,5),pygame.math.Vector2(1,5)]
        self.direction = pygame.math.Vector2(1,0)
        self.new_block = False
    def d_snake(self):
        for item in self.body:
            snake_rect = pygame.Rect(item.x * food_size,item.y * food_size,food_size,food_size)
            pygame.draw.rect(screen,(0,0,0),snake_rect)
    def m_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
    def big(self):
        self.new_block = True
class Eat:
    def __init__(self):
        self.rand()

    def d_food(self):
        food_rect = pygame.Rect(self.pos.x * food_size,self.pos.y * food_size,food_size+12,food_number+12)
        pygame.draw.rect(screen,(255,0,0),food_rect)

    def rand(self):
        self.x = random.randint(0,food_number*4 - 1)
        self.y = random.randint(0,food_number*4 - 1)
        self.pos = pygame.math.Vector2(self.x,self.y)
class Main:
    def __init__(self):
        self.snake = Snake()
        self.food = Eat()
        self.snake_size = 0
    def update(self):
        self.snake.m_snake()
        self.eat()
        self.die()
    def draw_elements(self):
        self.food.d_food()
        self.snake.d_snake()
    def eat(self):
        if self.snake.body[0] == self.food.pos:
            self.food.rand()
            self.snake.big()
            self.snake_size += 1
    def die(self):
        if not 0 <= self.snake.body[0].x < food_number*4:
            self.game_over()
        if not 0 <= self.snake.body[0].y < food_number*4:
            self.game_over()
        for item in self.snake.body[1:]:
            if item == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        largeFont = pygame.font.SysFont('Timesnewroman',100)
        score = largeFont.render('Twój wynik: ' + str(self.snake_size),True,(0,0,0))
        score_rect = score.get_rect(center=(400,400))
        screen.blit(score,score_rect)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()
pygame.init()
food_size = 20
food_number = 10
screen = pygame.display.set_mode((4 * food_size * food_number,4 * food_size * food_number))
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,133)
main_game = Main()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = pygame.math.Vector2(0,-1)
            elif event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = pygame.math.Vector2(-1,0)
            elif event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = pygame.math.Vector2(0,1)
            elif event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = pygame.math.Vector2(1,0)
            else:
                main_game = Main()
    screen.fill((50,220,255))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)