import pygame
from pygame.locals import *
import time

SIZE = 40

class Fruit:
    def __init__(self, parent_screen) -> None:
        self.image = pygame.image.load("fruit.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3
    
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

        pygame.display.flip()


class Snake:
    def __init__(self, parent_screen, length) -> None:
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = "right"

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
        self.surface = pygame.display.set_mode((640, 480))
        self.surface.fill((200, 200, 200))
        self.snake = Snake(self.surface, 10)
        self.fruit = Fruit(self.surface)
        self.snake.draw()
        self.fruit.draw()

    def play(self):
        self.snake.crawl()
        self.fruit.draw()

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
            time.sleep(0.3)

if __name__ == "__main__":
    game = Game()
    game.run()