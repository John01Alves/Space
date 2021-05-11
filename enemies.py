import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('utilitie/images/meteoro.png')
        self.image = pygame.transform.scale(self.image, [84, 84])
        self.rect = pygame.Rect(50, 50, 100, 100)
        self.speed = 1 + random.random() * 2

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)

    def update(self, *args):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
