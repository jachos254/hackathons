import pygame
from random import randint

green = (76, 153, 0)
grey = (69, 69, 69)
red = (204, 0, 0)
brown = (150, 70, 0)
color = (randint(0, 255), randint(0, 255), randint(0, 255))

class Alien:
    score = 0

    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 20
        self.score = 0

    def draw(self):
        pygame.draw.rect(self.game.screen,
                        color,
                        pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += 0.1

    def check_collision(self, game):

        for rocket in game.rockets:
            if (rocket.x < self.x + self.size and
                rocket.x > self.x - self.size and
                rocket.y < self.y + self.size and
                rocket.y > self.y - self.size):

                game.rockets.remove(rocket)
                game.aliens.remove(self)
                Alien.score += 1

class Hero:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    def draw(self):
        w = 20
        length = 5
        pygame.draw.rect(self.game.screen,
                        grey,
                        pygame.Rect(self.x, self.y, w, length))

class Generator:
    def __init__(self, game):
        margin = 30
        width = 50
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y))

class Rocket:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen,
                        red,
                        pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 5

