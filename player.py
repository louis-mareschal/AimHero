import pygame
from projectile import Projectile
import math
import time


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


class Player(pygame.sprite.Sprite):  # On lui dis que c'est une classe Sprite qui nous permettra de le déplacer et autre

    def __init__(self, game):
        super().__init__()  # Il faut initialiser le sprite
        self.game = game
        self.health = 100
        self.max_health = 100
        self.health_upgrade = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.speed = 2
        self.pos = pygame.math.Vector2(400, 500)
        self.rect = self.image.get_rect(topleft=(400, 500))
        self.attack = 10
        self.speed_attack = 0.75
        self.upgrades = [0] * 7
        self.consommables = [50] * 1
        self.invincible = 1  # Temps pendant lequel le joueur ne prend pas de dégâts après avoir été touché
        self.t_invincible = time.time()
        self.projectile_velocity = 2
        self.vie_potion = 25

    def increase_speed_attack(self):
        if self.game.gold - 10 * 2**self.upgrades[6] >= 0:
            self.speed_attack = truncate(self.speed_attack * 0.8, 2)
            self.game.gold -= 10 * 2**self.upgrades[6]
            self.upgrades[6] += 1

    def increase_speed(self):
        if self.game.gold - 10 * 2 ** self.upgrades[5] >= 0:
            self.speed = truncate(self.speed * 1.1, 2)
            self.game.gold -= 10 * 2 ** self.upgrades[5]
            self.upgrades[5] += 1

    def increase_projectile_velocity(self):
        if self.game.gold - 10 * 2 ** self.upgrades[4] >= 0:
            self.projectile_velocity *= 1.2
            self.game.gold -= 10 * 2 ** self.upgrades[4]
            self.upgrades[4] += 1

    def increase_research(self):
        if self.game.gold - 10 * 2 ** self.upgrades[3] >= 0:
            self.consommables[0] = math.ceil(self.consommables[0] * 1.1)
            self.vie_potion = math.ceil(self.vie_potion * 1.2)
            self.game.gold -= 10 * 2 ** self.upgrades[3]
            self.upgrades[3] += 1

    def increase_income(self):
        if self.game.gold - 10 * 2 ** self.upgrades[2] >= 0:
            self.game.gold_income = truncate(self.game.gold_income * 1.2, 2)
            self.game.gold -= 10 * 2 ** self.upgrades[2]
            self.upgrades[2] += 1

    def increase_health(self):
        if self.game.gold - 10 * 2 ** self.upgrades[1] >= 0:
            self.health_upgrade = math.ceil(self.health_upgrade * 1.2)
            self.game.gold -= 10 * 2 ** self.upgrades[1]
            self.upgrades[1] += 1

    def increase_attack(self):
        if self.game.gold - 10 * 2 ** self.upgrades[0] >= 0:
            # Pour que ça soit pareil d'augmenter l'attaque ou la vitesse d'attaque
            self.attack = truncate(self.attack * 1 / 0.9, 2)
            self.game.gold -= 10 * 2 ** self.upgrades[0]
            self.upgrades[0] += 1

    def potion(self):
        if self.game.gold - self.consommables[0] >= 0:
            self.health = self.health + self.vie_potion / self.health_upgrade
            if self.health > self.max_health:
                self.health = self.max_health
            self.game.gold -= self.consommables[0]

    def damage(self, amount):
        if time.time() - self.t_invincible > self.invincible:
            if self.health - amount / self.health_upgrade > 0:
                self.t_invincible = time.time()
                self.health -= amount / self.health_upgrade
            else:
                # Fin de partie
                self.game.game_over()

    def update_health_bar(self, surface):
        # Définir la couleur des barres de vie (vair clair et rouge)
        bar_color = (111, 210, 46)
        back_bar_color = (255, 0, 0)
        # Définir la position, largeur et épaisseur des barres de vie
        bar_position = [self.rect.x - self.max_health // 2 + 42, self.rect.y - 10, self.health / 1.5, 7]
        back_bar_position = [self.rect.x - self.max_health // 2 + 42, self.rect.y - 10, self.max_health / 1.5, 7]

        # Dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))  # On donne self en argument car il faut lui donner les co du joueur

    def move_right(self):
        self.pos.x += self.speed
        self.rect.topleft = round(self.pos.x), round(self.pos.y)

    def move_left(self):
        self.pos.x -= self.speed
        self.rect.topleft = round(self.pos.x), round(self.pos.y)

    def move_up(self):
        self.pos.y -= self.speed
        self.rect.topleft = round(self.pos.x), round(self.pos.y)

    def move_down(self):
        self.pos.y += self.speed
        self.rect.topleft = round(self.pos.x), round(self.pos.y)

    def move_right_up(self):
        self.pos.x += math.sqrt(2) * self.speed / 2
        self.pos.y -= math.sqrt(2) * self.speed / 2
        self.rect.topleft = round(self.pos.x), round(self.pos.y)

    def move_right_down(self):
        self.pos.x += math.sqrt(2) * self.speed / 2
        self.pos.y += math.sqrt(2) * self.speed / 2
        self.rect.topleft = round(self.pos.x), round(self.pos.y)

    def move_left_down(self):
        self.pos.x -= math.sqrt(2) * self.speed / 2
        self.pos.y += math.sqrt(2) * self.speed / 2
        self.rect.topleft = round(self.pos.x), round(self.pos.y)

    def move_left_up(self):
        self.pos.x -= math.sqrt(2) * self.speed / 2
        self.pos.y -= math.sqrt(2) * self.speed / 2
        self.rect.topleft = round(self.pos.x), round(self.pos.y)
