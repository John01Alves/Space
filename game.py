import pygame
import os
from pygame.locals import *
from Game import player
menu = 1

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((840, 480), 0, 32)
key_enter = False
jogadorGrupo = pygame.sprite.Group()

jogador = Player(jogadorGrupo)


def window():
    global menu, key_enter

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                menu += 1
            elif event.key == K_UP:
                menu -= 1
            elif event.key == K_KP_ENTER:
                menu += 10


def select():
    global menu, key_enter

    if menu == 1:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        new_game = font.render('> New Game', True, (80, 80, 80))
        screen.blit(new_game, ((800 / 2) - 50, (400 / 2)))

        load_game = font.render(' Load Game', True, (80, 80, 80))
        screen.blit(load_game, ((800 / 2) - 50, (400 / 2) + 22))

        exit_game = font.render(' Quit', True, (80, 80, 80))
        screen.blit(exit_game, ((800 / 2) - 15, (400 / 2) + 44))
    elif menu == 2:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        new_game = font.render(' New Game', True, (80, 80, 80))
        screen.blit(new_game, ((800 / 2) - 50, (400 / 2)))

        load_game = font.render('> Load Game', True, (80, 80, 80))
        screen.blit(load_game, ((800 / 2) - 50, (400 / 2) + 22))

        exit_game = font.render(' Quit', True, (80, 80, 80))
        screen.blit(exit_game, ((800 / 2) - 15, (400 / 2) + 44))
    elif menu == 3:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        new_game = font.render(' New Game', True, (80, 80, 80))
        screen.blit(new_game, ((800 / 2) - 50, (400 / 2)))

        load_game = font.render(' Load Game', True, (80, 80, 80))
        screen.blit(load_game, ((800 / 2) - 50, (400 / 2) + 22))

        exit_game = font.render('> Quit', True, (80, 80, 80))
        screen.blit(exit_game, ((800 / 2) - 15, (400 / 2) + 44))

    if menu == 4:
        menu = 3
    elif menu == 0:
        menu = 1
    elif menu == 11:
        menu += 100
    elif menu == 13:
        pygame.quit()
    elif menu == 12:
        menu = 2

    if menu == 111:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        msn = font.render('> mission 01', True, (80, 80, 80))
        screen.blit(msn, ((800 / 2) - 80, (400 / 2)))

        back = font.render(' Back', True, (80, 80, 80))
        screen.blit(back, ((800 / 2) - 50, (400 / 2) + 32))
    elif menu == 112:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        msn = font.render(' mission 01', True, (80, 80, 80))
        screen.blit(msn, ((800 / 2) - 70, (400 / 2)))

        back = font.render('> Back', True, (80, 80, 80))
        screen.blit(back, ((800 / 2) - 60, (400 / 2) + 32))

    if menu == 110:
        menu = 111
    elif menu == 113:
        menu = 112
    elif menu == 122:
        menu = 1
    elif menu == 121:
        menu += 100

    if menu == 221:
        menu = 2221


while True:
    clock.tick(60)
    window()
    select()
    pygame.display.update()
