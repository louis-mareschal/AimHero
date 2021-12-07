import pygame
import random
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


class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.image = pygame.image.load("assets/ennemies/blop_happy.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        x = random.choice([0, 1080]) + random.randint(0, 200)
        y = random.choice([0, 720]) + random.randint(0, 200)
        self.pos = pygame.math.Vector2(x, y)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = 1
        self.angry = False
        self.health_upgrade = 1
        self.is_dead = False
        self.gold_reward_blop = 10
        self.boss = False

    def damage(self, amount):
        self.health -= (self.max_health * amount) / (self.max_health * self.health_upgrade)
        if self.boss is True:
            self.image = pygame.image.load("assets/ennemies/blop_angry.png")
            self.image = pygame.transform.scale(self.image, (50 + int(self.max_health-self.health), 50 + int(self.max_health-self.health)))
            self.velocity = 1 + int(self.max_health-self.health)*0.02
        if self.health <= 0:
            self.game.all_monsters.remove(self)
            self.game.all_monsters_blop.remove(self)
            self.game.gold += math.ceil(self.gold_reward_blop * self.game.gold_income)

    def update_health_bar(self, surface):
        # Définir la couleur des barres de vie (vair clair et rouge)
        bar_color = (111, 210, 46)
        back_bar_color = (255, 0, 0)
        # Définir la position, largeur et épaisseur des barres de vie
        if self.boss is not True:
            bar_position = [self.rect.x + (self.health_upgrade - 1 + int(self.angry)) * 5, self.rect.y - 13,
                            self.health / 2, 5]
            back_bar_position = [self.rect.x + (self.health_upgrade - 1 + int(self.angry)) * 5,
                                 self.rect.y - 13, self.max_health / 2, 5]
        else:
            bar_position = [self.rect.x +
                            (self.max_health - self.health)/2, self.rect.y - 13, self.health / 2, 7]
            back_bar_position = [self.rect.x +
                                 (self.max_health - self.health)/2, self.rect.y - 13, self.max_health / 2, 7]

        # Dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):

        temp = pygame.sprite.Group(self.game.all_monsters_blop)
        temp.remove(self)
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage(self.attack)
        else:
            # Pour éviter les tremblements je rajoute abs(...)
            rl = abs(self.rect.x - self.game.player.rect.x) > 2 * self.velocity
            ud = abs(self.rect.y - self.game.player.rect.y) > 2 * self.velocity
            right = self.rect.x < self.game.player.rect.x
            left = self.rect.x > self.game.player.rect.x
            up = self.rect.y > self.game.player.rect.y
            down = self.rect.y < self.game.player.rect.y
            if rl and ud:
                if right and up:
                    self.pos.x += math.sqrt(2) * self.velocity / 2
                    self.pos.y -= math.sqrt(2) * self.velocity / 2
                elif right and down:
                    self.pos.x += math.sqrt(2) * self.velocity / 2
                    self.pos.y += math.sqrt(2) * self.velocity / 2
                elif left and down:
                    self.pos.x -= math.sqrt(2) * self.velocity / 2
                    self.pos.y += math.sqrt(2) * self.velocity / 2
                elif left and up:
                    self.pos.x -= math.sqrt(2) * self.velocity / 2
                    self.pos.y -= math.sqrt(2) * self.velocity / 2
            elif rl:
                if self.rect.x < self.game.player.rect.x:
                    self.pos.x += self.velocity
                elif self.rect.x > self.game.player.rect.x:
                    self.pos.x -= self.velocity
            elif ud:
                if self.rect.y < self.game.player.rect.y:
                    self.pos.y += self.velocity
                elif self.rect.y > self.game.player.rect.y:
                    self.pos.y -= self.velocity

            self.rect.topleft = round(self.pos.x), round(self.pos.y)

            if self.game.check_collision(self, temp):
                for monstre in temp:
                    temp2 = pygame.sprite.Group(self.game.all_monsters_blop)
                    temp2.remove(monstre)
                    if self.game.check_collision(monstre, temp2):
                        break

                self.health_upgrade += monstre.health_upgrade
                self.health = math.trunc(
                    self.health * (self.health_upgrade - monstre.health_upgrade) / self.health_upgrade)
                self.health += monstre.health * monstre.health_upgrade / self.health_upgrade
                monstre.is_dead = True
                self.gold_reward_blop += 15
                if not self.angry:
                    self.image = pygame.image.load("assets/ennemies/blop_angry.png")
                    self.image = pygame.transform.scale(self.image, (
                    40 + self.health_upgrade * 10 + 10, 40 + self.health_upgrade * 10 + 10))
                    self.velocity += 1
                    self.angry = True
                else:
                    self.image = pygame.image.load("assets/ennemies/blop_angry.png")
                    self.image = pygame.transform.scale(self.image,
                                                        (40 + self.health_upgrade * 10, 40 + self.health_upgrade * 10))
                    self.velocity += 0.5
