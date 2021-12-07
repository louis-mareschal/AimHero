from player import Player
from monster import Monster
from monster2 import Monster2
from wave import Wave


import pygame
from pygame.locals import *
import time



class Game:

    def __init__(self):
        # Définir si le jeu a commencé
        self.is_playing = False
        # Génerer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}   # Contient toutes les touches maintenues enfoncées
        # Définir le groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.all_monsters_blop = pygame.sprite.Group()
        self.all_monsters_split = pygame.sprite.Group()
        # Gérer l'argent
        self.gold = 100
        self.gold_income = 1
        self.gold_reward_split = 15
        # Gérer l'image du viseur
        self.cursor = pygame.image.load('assets/cursor.png')
        self.cursor = pygame.transform.scale(self.cursor, (40, 40))
        self.cursor_rect = self.cursor.get_rect()
        self.cursor.fill((255, 255, 255, 100), special_flags=BLEND_RGBA_MULT)
        self.start_shooting = False
        self.wave = Wave(self)
        self.time_attack = time.time()
        self.all_projectiles_split = pygame.sprite.Group()

    def start(self):
        # Compteur pour lancer un projectile à interval régulier
        self.is_playing = True
        pygame.mouse.set_visible(False)
        self.time_attack = time.time()

    def game_over(self):
        # Rénitialiser le jeu
        pygame.mouse.set_visible(True)
        self.gold = self.wave.wave_number * 30
        self.gold_income = 1
        self.wave = Wave(self)
        self.all_projectiles_split = pygame.sprite.Group()
        self.all_monsters = pygame.sprite.Group()
        self.all_monsters_split = pygame.sprite.Group()
        self.all_monsters_blop = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.is_playing = False

    def update(self, screen):
        # Afficher le curseur pour les améliorations
        if (150 < pygame.mouse.get_pos()[0] < 680) and pygame.mouse.get_pos()[1] < 70:
            pygame.mouse.set_visible(True)
            self.cursor = pygame.image.load('assets/cursor.png')
            self.cursor = pygame.transform.scale(self.cursor, (40, 40))
            self.cursor.fill((255, 255, 255, 0), special_flags=BLEND_RGBA_MULT)
        else:
            pygame.mouse.set_visible(False)
            self.cursor = pygame.image.load('assets/cursor.png')
            self.cursor = pygame.transform.scale(self.cursor, (40, 40))
            self.cursor.fill((255, 255, 255, 125), special_flags=BLEND_RGBA_MULT)
        # Appliquer l'image du joueur
        # L'image du joueur se positionne par rapport à rect (son rectangle définit dans la classe player)
        screen.blit(self.player.image, self.player.rect)
        # Afficher l'argent du joueur
        font = pygame.font.Font(None, 50)
        gold = font.render(str(self.gold), True, (255, 227, 0))
        screen.blit(gold, (60, 15))
        # Afficher le prix des upgrades
        font = pygame.font.Font(None, 25)
        x = 150
        for i in range(7):
            cost = font.render(str(10 * 2**self.player.upgrades[i]), True, (255, 227, 0))
            screen.blit(cost, (x, 55))
            x += 80
        # Afficher le prix des consommables
        y = 155
        for i in range(1):
            cost = font.render(str(self.player.consommables[0]), True, (255, 227, 0))
            screen.blit(cost, (1040, y))
            y += 150
        # Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        # Projectile si le click droit est enfoncé
        if self.start_shooting is True and len(self.player.all_projectiles) == 0 and time.time() - self.time_attack > self.player.speed_attack:
            self.player.launch_projectile()
            self.time_attack = time.time()
        # Projectile des monstres split
        for monster2 in self.all_monsters_split:
            if time.time() - monster2.time_attack > 2:
                for i in range(1, 5):
                    monster2.launch_projectile(i)
                monster2.time_attack = time.time()
        # Recupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
        # Recupérer les projectiles des monstres splits
        for projectile in self.all_projectiles_split:
            projectile.move()
        # Obliger de séparer car ils ont les mêmes noms de fonctions mais des propriétés différentes
        for monster in self.all_monsters_blop:
            if not monster.is_dead:
                monster.forward()
                monster.update_health_bar(screen)
        for monster in self.all_monsters_split:
            monster.forward()
            monster.update_health_bar(screen)
        for monster in self.all_monsters_blop:
            if monster.is_dead:
                self.all_monsters.remove(monster)
                self.all_monsters_blop.remove(monster)

        # Appliquer l'ensemble des images de mon groupe projectile
        self.all_projectiles_split.draw(screen)
        # Appliquer l'ensemble des images de mon groupe projectile
        self.player.all_projectiles.draw(screen)
        # Appliquer l'ensemble des images de mon groupe de monstres
        self.all_monsters.draw(screen)
        # Vérifier les déplacements du joueur (touches enfoncées ou non)
        right = self.player.rect.x + self.player.rect.width + 5 < screen.get_width()
        left = self.player.rect.x - 5 > 0
        up = self.player.rect.y - 15 > 0
        down = self.player.rect.y + self.player.rect.height + 5 < screen.get_height()
        if self.pressed.get(100) and self.pressed.get(119) and right and up:
            self.player.move_right_up()
        elif self.pressed.get(100) and self.pressed.get(115) and right and down:
            self.player.move_right_down()
        elif self.pressed.get(97) and self.pressed.get(115) and left and down:
            self.player.move_left_down()
        elif self.pressed.get(97) and self.pressed.get(119) and left and up:
            self.player.move_left_up()
        elif self.pressed.get(100) and right:
            self.player.move_right()
        elif self.pressed.get(97) and left:
            self.player.move_left()
        elif self.pressed.get(119) and up:
            self.player.move_up()
        elif self.pressed.get(115) and down:
            self.player.move_down()
        # Gérer la wave en cours
        self.wave.lunch_wave(screen)
        if len(self.all_monsters) == 0:
            self.wave.wave_number += 1
        # Appliquer l'image du curseur viseur
        self.cursor_rect.x = pygame.mouse.get_pos()[0] - 20
        self.cursor_rect.y = pygame.mouse.get_pos()[1] - 20
        screen.blit(self.cursor, self.cursor_rect)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
        self.all_monsters_blop.add(monster)

    def spawn_monster2(self):
        monster2 = Monster2(self)
        self.all_monsters.add(monster2)
        self.all_monsters_split.add(monster2)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)