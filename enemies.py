import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('utilitie/images/meteoro.png')
        lar = random.randint(40, 84)
        con = random.randint(40, 84)
        self.image = pygame.transform.scale(self.image, [lar, con])
        self.rect = self.image.get_rect()
        self.speed = 1 + random.random() * 2

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)

    def update(self, *args):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
