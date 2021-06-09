import pygame


class Placar():
    def __init__(self):
        self.window = pygame.display.set_mode([840, 480])
        self.pontos = 0
        self.short = 5

    def cont(self):
        self.pontos += 1

    def conte(self):
        self.short -= 1

    def recar(self):
        self.short += 5

    def contagem(self):
        fonte = pygame.font.SysFont('arial', 20, False, False)
        text = fonte.render('Pontos = ' + str(self.pontos), True, (255, 255, 255))
        textpos = text.get_rect()
        self.window.blit(text, (0, 0))

        muni = fonte.render('Munição = ' + str(self.short), True, (255, 255, 255))
        pos = muni.get_rect()
        self.window.blit(muni, (150, 0))
