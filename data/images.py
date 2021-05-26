import pygame
from random import random, randint


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('utilitie/images/ship.png')
        self.image = pygame.transform.scale(self.image, [64, 32])
        self.rect = pygame.Rect(64, 64, 50, 50)
        self.speed = 0

    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 4
        if keys[pygame.K_RIGHT]:
            self.rect.x += 4
        if keys[pygame.K_UP]:
            self.rect.y -= 4
        if keys[pygame.K_DOWN]:
            self.rect.y += 4
        else:
            self.rect.x += self.speed
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
            self.speed = 0
        elif self.rect.right > 830:
            self.rect.right = 830
            self.speed = 0
        elif self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        elif self.rect.bottom > 470:
            self.rect.bottom = 470
            self.speed = 0


class Shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('utilitie/images/leiser.png')
        self.image = pygame.transform.scale(self.image, [24, 3])
        self.rect = self.image.get_rect()
        self.speed = 12

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('utilitie/images/meteoro.png')
        lar = randint(40, 84)
        con = randint(40, 84)
        self.image = pygame.transform.scale(self.image, [lar, con])
        self.rect = self.image.get_rect()
        self.speed = 3 + random() * 2

        self.rect.x = 840 + randint(1, 100)
        self.rect.y = randint(1, 400)

    def update(self, *args):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
