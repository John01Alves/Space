import pygame
from data.menu import window, select

pygame.display.set_caption('Space')

while True:
    window()
    select()
    pygame.display.update()
