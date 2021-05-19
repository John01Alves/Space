import pygame

tela = pygame.display.set_mode((840, 480))


class Scoreboard:
    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 20)
        self.pontos = 1

    def contagem(self):
        self.text = self.fonte.render('Pontos = ' + str(self.pontos), 1, (255, 255, 255))
        self.textpos = self.text.get_rect()
        self.textpos.centerx = tela.get_width() / 2
        tela.blit(self.text, self.textpos)
        tela.blit(tela, (0, 0))
