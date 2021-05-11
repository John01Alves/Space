import pygame
import random
from player import Player
from shot import Shot
from enemies import Enemy


def jogo():
    pygame.init()
    window = pygame.display.set_mode([840, 480])
    clock = pygame.time.Clock()

    jogadorGrupo = pygame.sprite.Group()
    tiroGrupo = pygame.sprite.Group()
    inimigoGrupo = pygame.sprite.Group()

    jogador = Player(jogadorGrupo)

    timer = 0

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
        window.fill([0, 0, 0])
        jogadorGrupo.draw(window)
        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.3:
                novoinimigo = Enemy(jogadorGrupo, inimigoGrupo)
        colisao = pygame.sprite.spritecollide(jogador, inimigoGrupo, False)
        morte = pygame.sprite.groupcollide(tiroGrupo, inimigoGrupo, True, True)
        if colisao:
            pygame.quit()
            exit()
        jogadorGrupo.update()
        pygame.display.update()
