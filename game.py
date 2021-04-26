import pygame
import os
from pygame.locals import *
from sys import exit

menu = 1
game_loop = True

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 400), 0, 32)
key_enter = False


def window():
    global menu, key_enter

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_s or event.key == K_DOWN:
                menu += 1
            elif event.key == K_w or event.key == K_UP:
                menu -= 1


def select():
    global menu, key_enter

    if menu == 1:
        screen.fill((0, 0, 0))

        font = pygame.font.SysFont('arial', 20, False, False)
        new_game = font.render('> New Game', True, (80, 80, 80))
        screen.blit(new_game, ((800 / 2) - 50, (400 / 2)))

        font = pygame.font.SysFont('arial', 20, False, False)
        load_game = font.render(' Load Game', True, (80, 80, 80))
        screen.blit(load_game, ((800 / 2) - 50, (400 / 2) + 22))
    elif menu == 2:
        screen.fill((0, 0, 0))

        font = pygame.font.SysFont('arial', 20, False, False)
        new_game = font.render(' New Game', True, (80, 80, 80))
        screen.blit(new_game, ((800 / 2) - 50, (400 / 2)))

        font = pygame.font.SysFont('arial', 20, False, False)
        load_game = font.render('> Load Game', True, (80, 80, 80))
        screen.blit(load_game, ((800 / 2) - 50, (400 / 2) + 22))

    if menu == 6:
        menu = 5
    elif menu == 0:
        menu = 1


while game_loop:
    clock.tick(30)
    window()
    select()
    pygame.display.update()
