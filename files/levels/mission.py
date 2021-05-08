import pygame
from player import Player
from shot import Shot


def jogo():
    pygame.init()
    window = pygame.display.set_mode([840, 480])
    clock = pygame.time.Clock()

    jogadorGrupo = pygame.sprite.Group()
    tiroGrupo = pygame.sprite.Group()

    jogador = Player(jogadorGrupo)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    novodisparo = Shot(jogadorGrupo, tiroGrupo)
                    novodisparo.rect.center = jogador.rect.center
        window.fill((0, 0, 0))
        jogadorGrupo.draw(window)
        jogadorGrupo.update()
        pygame.display.update()
