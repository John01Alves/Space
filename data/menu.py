import pygame
import os
from pygame.locals import *
from data.levels.mission import game
from data.third_menu import now


def Game():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode([840, 480])
    clock = pygame.time.Clock()

    image = pygame.image.load('utilitie/images/menu.png')

    pygame.mixer.music.load('utilitie/music/electronic.wav')
    pygame.mixer.music.play(-1)

    menu = [0, 1]

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            mouse_pos = pygame.mouse.get_pos()
            mouse = mouse_pos[1]
            if mouse >= (400 / 2) < mouse <= ((400 / 2) + 21):
                menu[1] = 1
            elif mouse >= ((400 / 2) + 22) < mouse <= ((400 / 2) + 43):
                menu[1] = 2
            elif mouse >= ((400 / 2) + 44) < mouse <= ((400 / 2) + 62):
                menu[1] = 3
            elif mouse < (400 / 2):
                menu[1] = 0
            elif mouse > ((400 / 2) + 62):
                menu[1] = 0

            if event.type == MOUSEBUTTONDOWN:
                menu[1] += 10

        if menu == [0, 0]:
            screen.blit(image, (0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            new_game = font.render('New Game', True, (255, 255, 255))
            screen.blit(new_game, ((800 / 2) - 22, (400 / 2)))

            load_game = font.render('Load Game', True, (255, 255, 255))
            screen.blit(load_game, ((800 / 2) - 24, (400 / 2) + 22))

            exit_game = font.render('Quit', True, (255, 255, 255))
            screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))
        elif menu == [0, 1]:
            screen.blit(image, (0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            new_game = font.render('New Game', True, (0, 155, 220))
            screen.blit(new_game, ((800 / 2) - 22, (400 / 2)))

            load_game = font.render('Load Game', True, (255, 255, 255))
            screen.blit(load_game, ((800 / 2) - 24, (400 / 2) + 22))

            exit_game = font.render('Quit', True, (255, 255, 255))
            screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))
        elif menu == [0, 2]:
            screen.blit(image, (0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            new_game = font.render('New Game', True, (255, 255, 255))
            screen.blit(new_game, ((800 / 2) - 22, (400 / 2)))

            load_game = font.render('Load Game', True, (0, 155, 220))
            screen.blit(load_game, ((800 / 2) - 24, (400 / 2) + 22))

            exit_game = font.render('Quit', True, (255, 255, 255))
            screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))
        elif menu == [0, 3]:
            screen.blit(image, (0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            new_game = font.render('New Game', True, (255, 255, 255))
            screen.blit(new_game, ((800 / 2) - 22, (400 / 2)))

            load_game = font.render('Load Game', True, (255, 255, 255))
            screen.blit(load_game, ((800 / 2) - 24, (400 / 2) + 22))

            exit_game = font.render('Quit', True, (0, 155, 220))
            screen.blit(exit_game, ((800 / 2) + 2, (400 / 2) + 44))

        if menu == [0, 11]:
            menu = [1, 0]
        elif menu == [0, 12]:
            menu = [0, 2]
        elif menu == [0, 13]:
            exit()

        if menu == [1, 0] or menu == [1, 2]:
            screen.blit(image, (0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            msn = font.render('mission 01', True, (255, 255, 255))
            screen.blit(msn, ((800 / 2) - 22, (400 / 2)))

            back = font.render('Back', True, (255, 255, 255))
            screen.blit(back, ((800 / 2) - 1, (400 / 2) + 44))

        elif menu == [1, 1]:
            screen.blit(image, (0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            msn = font.render('mission 01', True, (0, 155, 220))
            screen.blit(msn, ((800 / 2) - 22, (400 / 2)))

            back = font.render('Back', True, (255, 255, 255))
            screen.blit(back, ((800 / 2) - 1, (400 / 2) + 44))
        elif menu == [1, 3]:
            screen.blit(image, (0, 0))
            font = pygame.font.SysFont('arial', 20, False, False)

            msn = font.render('mission 01', True, (255, 255, 255))
            screen.blit(msn, ((800 / 2) - 22, (400 / 2)))

            back = font.render('Back', True, (0, 155, 220))
            screen.blit(back, ((800 / 2) - 1, (400 / 2) + 44))

        if menu == [1, 11]:
            screen.fill((0, 0, 0))
            game()
            menu = [3, 1]
        elif menu == [1, 13]:
            menu = [0, 1]

        if menu == [3, 1]:
            screen.fill((0, 0, 0))
            now()
            menu = [0, 1]
        pygame.display.update()
