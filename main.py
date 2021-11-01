import pygame
from pygame.locals import *
import time
import random

SIZE = 40
WIDTH = 640
HEIGHT = 480

class Fruit:
    def __init__(self, parent_screen) -> None:
        self.image = pygame.image.load("fruit.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3
    
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, WIDTH/SIZE - 1) * SIZE
        self.y = random.randint(1, HEIGHT/SIZE - 1) * SIZE


class Snake:
    def __init__(self, parent_screen, length) -> None:
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = "right"

    def increment_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((0, 0, 0))

        for _ in range(self.length):
            self.parent_screen.blit(self.block, (self.x[_], self.y[_]))

        pygame.display.flip()

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"
    
    def crawl(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] -= SIZE
        elif self.direction == "down":
            self.y[0] += SIZE
        elif self.direction == "left":
            self.x[0] -= SIZE
        elif self.direction == "right":
            self.x[0] += SIZE
        self.draw()


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.surface.fill((200, 200, 200))
        self.snake = Snake(self.surface, 2)
        self.fruit = Fruit(self.surface)
        self.snake.draw()
        self.fruit.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < (x2 + SIZE):
            if y1 >= y2 and y1 < (y2 + SIZE):
                return True
        return False

    def play(self):
        self.snake.crawl()
        self.fruit.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.fruit.x, self.fruit.y):
            self.snake.increment_length()
            self.fruit.move()

    def display_score(self):
        font = pygame.font.SysFont('arial',25)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(WIDTH - 3 * SIZE, SIZE))

    def run(self):
        running = True
        while running :
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP and self.snake.direction != "down":
                        self.snake.move_up()
                    if event.key == K_DOWN and self.snake.direction != "up":
                        self.snake.move_down()
                    if event.key == K_LEFT and self.snake.direction != "right":
                        self.snake.move_left()
                    if event.key == K_RIGHT and self.snake.direction != "left":
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
                
            self.play()
            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()