import pygame
import math


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):  # On lui donne la classe player pour qu'il puisse s'en servir
        super().__init__()
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        x = player.rect.x + 30
        y = player.rect.y + 5
        self.pos = pygame.math.Vector2(x, y)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = self.player.projectile_velocity
        self.origin_image = self.image
        self.attack = 10
        self.angle = 0

    def rotate(self):
        # Fait tourner le projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=(self.pos.x, self.pos.y))

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        if abs(pygame.mouse.get_pos()[0] - self.pos.x) > self.velocity:
            if pygame.mouse.get_pos()[0] - self.pos.x > 0:
                self.pos.x += self.velocity
            else:
                self.pos.x -= self.velocity

        if abs(pygame.mouse.get_pos()[1] - self.pos.y) > self.velocity:
            if pygame.mouse.get_pos()[1] - self.pos.y > 0:
                self.pos.y += self.velocity
            else:
                self.pos.y -= self.velocity

        self.rect.topleft = round(self.pos.x), round(self.pos.y)
        self.rotate()
        # Suppression des projectiles en cas de colisions avec un ennemie
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)
            if monster in self.player.game.all_monsters_blop and not monster.angry:
                monster.image = pygame.image.load("assets/ennemies/blop_angry.png")
                monster.image = pygame.transform.scale(monster.image, (60, 60))
                monster.velocity += 0.5
                monster.angry = True

        # Vérifier si le projectile est hors écran
        if self.rect.x > 1080 or self.rect.x < 0 or self.rect.y > 720 or self.rect.y < 0:
            # Supprimer le projectile
            self.remove()
