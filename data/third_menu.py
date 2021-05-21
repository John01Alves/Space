import pygame
import os
from pygame.locals import *

menu = 0

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode([840, 480])
clock = pygame.time.Clock()


def windows():
    global menu

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


def options():
    global menu

    if menu == 0:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        new_game = font.render('MISSION FAILED!', True, (255, 0, 0))
        screen.blit(new_game, ((800 / 2) - 66, (400 / 2)))

        load_game = font.render('restarting the game wait!', True, (255, 255, 255))
        screen.blit(load_game, ((800 / 2) - 66, (400 / 2) + 22))

        exit_game = font.render('Quit', True, (255, 255, 255))
        screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))
    elif menu == 1:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        new_game = font.render('MISSION FAILED!', True, (255, 0, 0))
        screen.blit(new_game, ((800 / 2) - 66, (400 / 2)))

        load_game = font.render('restarting the game wait!', True, (0, 155, 220))
        screen.blit(load_game, ((800 / 2) - 66, (400 / 2) + 22))

        exit_game = font.render('Quit', True, (255, 255, 255))
        screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))
    elif menu == 2:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        new_game = font.render('MISSION FAILED!', True, (255, 0, 0))
        screen.blit(new_game, ((800 / 2) - 66, (400 / 2)))

        load_game = font.render('restarting the game wait!', True, (255, 255, 255))
        screen.blit(load_game, ((800 / 2) - 66, (400 / 2) + 22))

        exit_game = font.render('Quit', True, (0, 155, 220))
        screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))

    if menu == -1:
        menu = 0
    elif menu == 3:
        menu = 2

    if menu == 11:
        menu = 1
    elif menu == 12:
        pygame.quit()
        exit()

