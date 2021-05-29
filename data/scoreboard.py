import pygame


class Placar():
    def __init__(self):
        self.window = pygame.display.set_mode([840, 480])
        self.pontos = 0

    def cont(self):
        self.pontos += 1

    def contagem(self):
        fonte = pygame.font.SysFont('arial', 20, False, False)
        text = fonte.render('Pontos = ' + str(self.pontos), True, (255, 255, 255))
        textpos = text.get_rect()
        self.window.blit(text, textpos)
        self.window.blit(self.window, (0, 0))
