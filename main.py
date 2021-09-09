import pygame
from pygame.locals import *
import time

class Snake:
    def __init__(self, parent_screen) -> None:
        self.parent_screen = parent_screen
        self.block = pygame.image.load("block.jpg").convert()
        self.x = 200
        self.y = 200
        self.direction = "right"

    def draw(self):
        self.parent_screen.fill((200, 200, 200))
        self.parent_screen.blit(self.block, (self.x, self.y))
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
        if self.direction == "up":
            self.y -= 12
        elif self.direction == "down":
            self.y += 12
        elif self.direction == "left":
            self.x -= 12
        elif self.direction == "right":
            self.x += 12
        self.draw()


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode((640, 480))
        self.surface.fill((200, 200, 200))
        self.snake = Snake(self.surface)
        self.snake.draw()

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
            self.snake.crawl()
            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()