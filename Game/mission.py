import pygame
from Game import player


class Jo(pygame, player):
    def jogo(self):
        pygame.init()
        self.window = pygame.display.set_mode([840, 480])
        self.clock = pygame.time.Clock()

        self.jogadorGrupo = pygame.sprite.Group()

        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.jogadorGrupo.update()
            self.jogadorGrupo.draw(self.window)
            self.pygame.display.update()
