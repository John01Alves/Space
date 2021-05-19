import pygame
import os
from pygame.locals import *
from data.levels.mission import game

menu = 1

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode([840, 480])
key_enter = False
clock = pygame.time.Clock()


def window():
    global menu, key_enter

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

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

        new_game = font.render('New Game', True, (0, 155, 220))
        screen.blit(new_game, ((800 / 2) - 22, (400 / 2)))

        load_game = font.render('Load Game', True, (255, 255, 255))
        screen.blit(load_game, ((800 / 2) - 24, (400 / 2) + 22))

        exit_game = font.render('Quit', True, (255, 255, 255))
        screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))
    elif menu == 2:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        new_game = font.render('New Game', True, (255, 255, 255))
        screen.blit(new_game, ((800 / 2) - 22, (400 / 2)))

        load_game = font.render('Load Game', True, (0, 155, 220))
        screen.blit(load_game, ((800 / 2) - 24, (400 / 2) + 22))

        exit_game = font.render('Quit', True, (255, 255, 255))
        screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))
    elif menu == 3:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        new_game = font.render('New Game', True, (255, 255, 255))
        screen.blit(new_game, ((800 / 2) - 22, (400 / 2)))

        load_game = font.render('Load Game', True, (255, 255, 255))
        screen.blit(load_game, ((800 / 2) - 24, (400 / 2) + 22))

        exit_game = font.render('Quit', True, (0, 155, 220))
        screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))

    if menu == 4:
        menu = 3
    elif menu == 0:
        menu = 1
    elif menu == 11:
        menu += 100
    elif menu == 13:
        pygame.quit()
        exit()
    elif menu == 12:
        menu = 2

    if menu == 111:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        msn = font.render('mission 01', True, (0, 155, 220))
        screen.blit(msn, ((800 / 2) - 22, (400 / 2)))

        back = font.render('Back', True, (255, 255, 255))
        screen.blit(back, ((800 / 2) - 1, (400 / 2) + 44))
    elif menu == 112:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        msn = font.render('mission 01', True, (255, 255, 255))
        screen.blit(msn, ((800 / 2) - 22, (400 / 2)))

        back = font.render('Back', True, (0, 155, 220))
        screen.blit(back, ((800 / 2) - 1, (400 / 2) + 44))

    if menu == 110:
        menu = 111
    elif menu == 113:
        menu = 112
    elif menu == 122:
        menu = 1
    elif menu == 121:
        menu += 100

    if menu == 221:
        screen.fill((0, 0, 0))
        while True:
            game()
