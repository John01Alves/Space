import pygame
import os
from pygame.locals import *

menu = 99

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode([840, 480])
key_enter = False
clock = pygame.time.Clock()


def windo():
    global menu, key_enter

    clock.tick(60)
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


def selec():
    global menu, key_enter

    if menu == 99:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 20, False, False)

        new_game = font.render('MISSION FAILED!', True, (80, 80, 80))
        screen.blit(new_game, ((800 / 2) - 50, (400 / 2)))

        exit_game = font.render('  > Quit <', True, (80, 80, 80))
        screen.blit(exit_game, ((800 / 2) - 15, (400 / 2) + 44))

    if menu == 100:
        menu = 99
    elif menu == 98:
        menu = 99

    if menu == 109:
        pygame.quit()
        exit()
