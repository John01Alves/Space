import pygame
from Game import menu

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    menu.window()
    menu.select()
    pygame.display.update()
