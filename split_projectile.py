import pygame
import math
import random


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


class Projectile_split(pygame.sprite.Sprite):

    def __init__(self, monster2, direction):  # On lui donne la classe player pour qu'il puisse s'en servir
        super().__init__()
        self.monster2 = monster2
        self.velocity = abs(max(self.monster2.velocity)) + 2 + random.randint(0, 100) / 100
        if direction == 1:
            self.velocity_x = self.velocity
            self.velocity_y = self.velocity
        elif direction == 2:
            self.velocity_x = -self.velocity
            self.velocity_y = self.velocity
        elif direction == 3:
            self.velocity_x = -self.velocity
            self.velocity_y = -self.velocity
        elif direction == 4:
            self.velocity_x = self.velocity
            self.velocity_y = -self.velocity
        self.image = pygame.image.load("assets/split_projectile.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        x = self.monster2.pos.x + 15
        y = self.monster2.pos.y + + 15
        self.pos = pygame.math.Vector2(x, y)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.origin_image = self.image
        self.attack = 10

    def remove(self):
        self.monster2.game.all_projectiles_split.remove(self)

    def move(self):
        self.pos.x += self.velocity_x
        self.pos.y += self.velocity_y
        self.rect.topleft = round(self.pos.x), round(self.pos.y)
        # Suppression des projectiles en cas de colisions avec un ennemie
        for projectile in self.monster2.game.check_collision(self, self.monster2.game.all_players):
            self.remove()
            self.monster2.game.player.damage(self.monster2.attack)

        # Vérifier si le projectile est hors écran
        if self.rect.x > 1080 or self.rect.x < 0 or self.rect.y > 720 or self.rect.y < 0:
            # Supprimer le projectile
            self.remove()