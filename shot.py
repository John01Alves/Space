import pygame


class Shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('utilitie/images/leiser.png')
        self.image = pygame.transform.scale(self.image, [24, 3])
        self.rect = self.image.get_rect()
        self.speed = 6

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()
