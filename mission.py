import pygame
import player


def jogo():
    pygame.init()
    window = pygame.display.set_mode([840, 480])
    clock = pygame.time.Clock()

    jogadorGrupo = pygame.sprite.Group()

    jogador = player.Player(jogadorGrupo)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        jogadorGrupo.update()
        jogadorGrupo.draw(window)
        pygame.display.update()
