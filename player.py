import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('utilitie/images/ship.png')
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)
        self.speed = 0

    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
        if keys[pygame.K_UP]:
            self.rect.y -= 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2
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
