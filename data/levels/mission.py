import pygame
import os
from random import random
from data.images import Player, Shot, Meteor
from data.scoreboard import Placar


def game():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    window = pygame.display.set_mode([840, 480])
    clock = pygame.time.Clock()

    player_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    meteor_group = pygame.sprite.Group()

    bg = pygame.sprite.Sprite(player_group)
    bg.image = pygame.image.load('utilitie/images/background0.png')
    bg.image = pygame.transform.scale(bg.image, [840, 480])
    bg.rect = bg.image.get_rect()

    player = Player(player_group)
    placar = Placar()

    pygame.mouse.set_visible(False)

    timer = 0

    while True:
        clock.tick(90)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_shot = Shot(player_group, shot_group)
                    new_shot.rect.center = player.rect.center
        player_group.draw(window)
        timer += 1
        if timer > 30:
            timer = 0
            if random() < 0.3:
                new_enemy = Meteor(player_group, meteor_group)
        collision = pygame.sprite.spritecollide(player, meteor_group, False)
        death = pygame.sprite.groupcollide(shot_group, meteor_group, True, True)
        if collision:
            break
        if death:
            placar.cont()
        player_group.update()
        placar.contagem()
        pygame.display.update()
