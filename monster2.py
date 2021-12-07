import pygame
import random
import time
from split_projectile import Projectile_split
import math


def collision(rectA, rectB):
    if rectB.right < rectA.left:
        # rectB est à gauche
        return False
    if rectB.bottom < rectA.top:
        # rectB est au-dessus
        return False
    if rectB.left > rectA.right:
        # rectB est à droite
        return False
    if rectB.top > rectA.bottom:
        # rectB est en-dessous
        return False
    # Dans tous les autres cas il y a collision
    return True


class Monster2(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 60
        self.max_health = 60
        self.attack = 40
        self.image = pygame.image.load("assets/ennemies/split_dad.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        x = random.choice([200, 800]) + random.randint(-100, 100)
        y = random.choice([200, 600]) + random.randint(-100, 50)
        self.pos = pygame.math.Vector2(x, y)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = pygame.math.Vector2((0.5 + random.randint(0, 150) / 100) * random.choice([-1, 1]),
                                            (0.5 + random.randint(0, 150) / 100) * random.choice([-1, 1]))
        self.time_attack = time.time() - random.randint(0, 200) / 100
        self.is_split = False

    def creer_monstres_splits(self):
        monster2 = Monster2(self.game)
        monster2.image = pygame.image.load("assets/ennemies/split_child.png")
        monster2.image = pygame.transform.scale(monster2.image, (40, 40))
        monster2.velocity = pygame.math.Vector2((1 + random.randint(0, 200) / 100) * random.choice([-1, 1]),
                                                (1 + random.randint(0, 200) / 100) * random.choice([-1, 1]))
        monster2.health = 30
        monster2.max_health = 30
        monster2.is_split = True
        x = self.pos.x
        y = self.pos.y
        monster2.pos = pygame.math.Vector2(x, y)
        monster2.rect = monster2.image.get_rect(topleft=(x, y))
        self.game.all_monsters.add(monster2)
        self.game.all_monsters_split.add(monster2)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            # Si le monstre n'est pas encore split, on créé deux nouveaux monstres avec is_split = True
            if not self.is_split:
                for i in range(random.randint(1, 3)):
                    self.creer_monstres_splits()
            # On supprime le monstre principal dans tous les cas
            self.game.all_monsters.remove(self)
            self.game.all_monsters_split.remove(self)
            self.game.gold += math.ceil(self.game.gold_reward_split * self.game.gold_income)

    def update_health_bar(self, surface):
        # Définir la couleur des barres de vie (vair clair et rouge)
        bar_color = (111, 210, 46)
        back_bar_color = (255, 0, 0)
        # Définir la position, largeur et épaisseur des barres de vie
        if not self.is_split:
            bar_position = [self.rect.x - 4, self.rect.y - 13, self.health, 5]
            back_bar_position = [self.rect.x - 4, self.rect.y - 13, self.max_health, 5]
        else:
            bar_position = [self.rect.x - 4, self.rect.y - 13, self.health * 8/5, 5]
            back_bar_position = [self.rect.x - 4, self.rect.y - 13, self.max_health * 8/5, 5]

        # Dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        if self.rect.x + self.velocity.x > 1030:
            self.velocity.x *= -1
        if self.rect.x + 2 * self.velocity.x < 0:
            self.velocity.x *= -1
        if self.rect.y + 2 * self.velocity.y > 670:
            self.velocity.y *= -1
        if self.rect.y + self.velocity.y < 10:
            self.velocity.y *= -1
        self.pos += self.velocity
        self.rect.topleft = round(self.pos.x), round(self.pos.y)

    def launch_projectile(self, direction):
        self.game.all_projectiles_split.add(Projectile_split(self, direction))  # On donne self en argument car il faut lui donner les co du joueur