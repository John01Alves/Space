import pygame
from random import random
from player import Player
from shot import Shot
from enemies import Enemy
from data.third_menu import windows, options


def game():
    pygame.init()
    window = pygame.display.set_mode([840, 480])
    clock = pygame.time.Clock()

    player_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    player = Player(player_group)

    timer = 0
    tempo = 0

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_shot = Shot(player_group, shot_group)
                    new_shot.rect.center = player.rect.center
        window.fill([0, 0, 0])
        player_group.draw(window)
        timer += 1
        if timer > 30:
            timer = 0
            if random() < 0.3:
                new_enemy = Enemy(player_group, enemy_group)
        collision = pygame.sprite.spritecollide(player, enemy_group, False)
        death = pygame.sprite.groupcollide(shot_group, enemy_group, True, True)
        if collision:
            while True:
                windows()
                options()
                tempo += 1
                pygame.display.update()
                if tempo >= 1000:
                    break
        player_group.update()
        pygame.display.update()
