import pygame
from player import Player


def missi():
    pygame.init()
    window = pygame.display.set_mode([840, 480])
    clock = pygame.time.Clock()

    jogadorGrupo = pygame.sprite.Group()

    jogador = Player(jogadorGrupo)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        jogadorGrupo.update()
        jogadorGrupo.draw(window)
        pygame.display.update()
