import pygame
import os
from pygame.locals import *


def now():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode([840, 480])
    clock = pygame.time.Clock()

    jogadorGrup = pygame.sprite.Group()

    bg = pygame.sprite.Sprite(jogadorGrup)
    bg.image = pygame.image.load('../utilitie/images/menu.png')
    bg.image = pygame.transform.scale(bg.image, [840, 480])
    bg.rect = bg.image.get_rect()

    menu = 0

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            mouse_pos = pygame.mouse.get_pos()
            mouse = mouse_pos[1]
            if mouse >= ((400 / 2) + 22) < mouse <= ((400 / 2) + 43):
                menu = 1
            elif mouse >= ((400 / 2) + 44) < mouse <= ((400 / 2) + 62):
                menu = 2
            elif mouse < ((400 / 2) + 23):
                menu = 0
            elif mouse > ((400 / 2) + 62):
                menu = 0

            if event.type == MOUSEBUTTONDOWN:
                menu += 10

        jogadorGrup.draw(screen)
        if menu == 0:
            jogadorGrup.draw(screen)
            font = pygame.font.SysFont('arial', 20, False, False)

            new_game = font.render('MISSION FAILED!', True, (255, 0, 0))
            screen.blit(new_game, ((800 / 2) - 66, (400 / 2)))

            load_game = font.render('Menu', True, (255, 255, 255))
            screen.blit(load_game, ((800 / 2) - 4, (400 / 2) + 22))

            exit_game = font.render('Quit', True, (255, 255, 255))
            screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))
        elif menu == 1:
            jogadorGrup.draw(screen)
            font = pygame.font.SysFont('arial', 20, False, False)

            new_game = font.render('MISSION FAILED!', True, (255, 0, 0))
            screen.blit(new_game, ((800 / 2) - 66, (400 / 2)))

            load_game = font.render('Menu', True, (0, 155, 220))
            screen.blit(load_game, ((800 / 2) - 4, (400 / 2) + 22))

            exit_game = font.render('Quit', True, (255, 255, 255))
            screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))
        elif menu == 2:
            jogadorGrup.draw(screen)
            font = pygame.font.SysFont('arial', 20, False, False)

            new_game = font.render('MISSION FAILED!', True, (255, 0, 0))
            screen.blit(new_game, ((800 / 2) - 66, (400 / 2)))

            load_game = font.render('Menu', True, (255, 255, 255))
            screen.blit(load_game, ((800 / 2) - 4, (400 / 2) + 22))

            exit_game = font.render('Quit', True, (0, 155, 220))
            screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))

        if menu == 11:
            break
        elif menu == 12:
            exit()
        pygame.display.update()
