import pygame
import os
import math
from game import Game

pygame.init()
# Générer la fenêtre
pygame.display.set_caption("Jeu")
screen = pygame.display.set_mode((1080, 720))
os.environ['SDL_VIDEO_WINDOW_POS']="0,0"  # Permet de choisir la position de la fenêtre
# Arrière plan
background = pygame.image.load('assets/bg.jpg')
# Bannière

player_b = pygame.image.load('assets/player.png')
player_b = pygame.transform.scale(player_b, (300, 300))
player_b_rect = player_b.get_rect()
player_b_rect.x = 430
player_b_rect.y = 220

monster_blop_b = pygame.image.load('assets/ennemies/blop_angry.png')
monster_blop_b = pygame.transform.scale(monster_blop_b, (200, 200))
monster_blop_b_rect = monster_blop_b.get_rect()
monster_blop_b_rect.x = 482
monster_blop_b_rect.y = 85

monster_split_b = pygame.image.load('assets/ennemies/split_child.png')
monster_split_b = pygame.transform.scale(monster_split_b, (200, 200))
monster_split_b_rect = monster_split_b.get_rect()
monster_split_b = pygame.transform.rotozoom(monster_split_b, 45, 1)
monster_split_b_rect.x = 280
monster_split_b_rect.y = 200

monster_laser_b = pygame.image.load('assets/ennemies/laser_angry.png')
monster_laser_b = pygame.transform.scale(monster_laser_b, (200, 200))
monster_laser_b_rect = monster_laser_b.get_rect()
monster_laser_b = pygame.transform.rotozoom(monster_laser_b, -45, 1)
monster_laser_b_rect.x = 600
monster_laser_b_rect.y = 200

# CHarger le bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = 380
play_button_rect.y = 500
# Boutons pour toutes les améliorations

# Charger le bouton pour augmenter sa force d'attaque
attack_button = pygame.image.load('assets/upgrades/attack.png')
attack_button = pygame.transform.scale(attack_button, (50, 50))
attack_button_rect = attack_button.get_rect()
attack_button_rect.x = 150
# Charger le bouton pour augmenter sa vie
health_button = pygame.image.load('assets/upgrades/health.png')
health_button = pygame.transform.scale(health_button, (50, 50))
health_button_rect = health_button.get_rect()
health_button_rect.x = 230
# Charger le bouton pour augmenter les récompenses
income_button = pygame.image.load('assets/upgrades/income.png')
income_button = pygame.transform.scale(income_button, (50, 50))
income_button_rect = income_button.get_rect()
income_button_rect.x = 310
# Charger le bouton pour augmenter l'efficacité des potions
research_button = pygame.image.load('assets/upgrades/research.png')
research_button = pygame.transform.scale(research_button, (50, 50))
research_button_rect = research_button.get_rect()
research_button_rect.x = 390
# Charger le bouton pour augmenter le taille des projectiles
projectile_button = pygame.image.load('assets/upgrades/projectile.png')
projectile_button = pygame.transform.scale(projectile_button, (50, 50))
projectile_button_rect = projectile_button.get_rect()
projectile_button_rect.x = 470
# Charger le bouton pour augmenter sa vitesse
speed_button = pygame.image.load('assets/upgrades/speed.png')
speed_button = pygame.transform.scale(speed_button, (50, 50))
speed_button_rect = speed_button.get_rect()
speed_button_rect.x = 550
# Charger le bouton pour augmenter sa vitesse d'attaque
speed_attack_button = pygame.image.load('assets/upgrades/speed_attack.png')
speed_attack_button = pygame.transform.scale(speed_attack_button, (50, 50))
speed_attack_button_rect = speed_attack_button.get_rect()
speed_attack_button_rect.x = 630
# Charger les images coin
coin = pygame.image.load('assets/coin.png')
coin = pygame.transform.scale(coin, (15, 15))
# Charger l'image coins
coins = pygame.image.load('assets/coins.png')
coins = pygame.transform.scale(coins, (40, 40))
coins_rect = coins.get_rect()

# Boutons pour toutes les consommables:

# Charger l'image de la potion de vie
potion = pygame.image.load('assets/consommables/potion.png')
potion = pygame.transform.scale(potion, (50, 50))
potion_rect = potion.get_rect()
potion_rect.x = 1030
potion_rect.y = 100

# Charger jeu :
game = Game()
running = True
# Boucle du jeu
while running:
    # Arrière plan
    screen.blit(background, (0, 0))
    # Vérifier si le jeu a commencé
    if game.is_playing:
        # Appliquer l'image des coin et coins
        screen.blit(coins, coins_rect)
        coin_rect = coin.get_rect()
        coin_rect.x = 190
        coin_rect.y = 55
        for i in range(7):
            screen.blit(coin, coin_rect)
            coin_rect.x += 80
        coin_rect.x = 1060
        coin_rect.y = 155
        for i in range(1):
            screen.blit(coin, coin_rect)
            coin_rect.y += 80

        # Aplliquer l'image des boutons d'améliorations
        screen.blit(attack_button, attack_button_rect)
        screen.blit(health_button, health_button_rect)
        screen.blit(income_button, income_button_rect)
        screen.blit(research_button, research_button_rect)
        screen.blit(projectile_button, projectile_button_rect)
        screen.blit(speed_button, speed_button_rect)
        screen.blit(speed_attack_button, speed_attack_button_rect)
        # Appliquer l'image des consommables
        screen.blit(potion, potion_rect)
        # Actualiser l'écran
        game.update(screen)
    else:
        screen.blit(monster_laser_b, monster_laser_b_rect)
        screen.blit(monster_split_b, monster_split_b_rect)
        screen.blit(monster_blop_b, monster_blop_b_rect)
        screen.blit(player_b, player_b_rect)
        screen.blit(play_button, play_button_rect)
        pygame.font.init()
        font = pygame.font.Font("assets/font/sirens.otf", 102)
        gold = font.render("AimHero", True, (0, 0, 0))
        screen.blit(gold, (374, 447))
        font = pygame.font.Font("assets/font/sirens.otf", 100)
        gold = font.render("AimHero", True, (232, 0, 88))
        screen.blit(gold, (380, 450))


    # Mettre à jour l'écran
    pygame.display.flip()
    # Parcourt de la lsite des évenements (actions du joueur)
    for event in pygame.event.get():
        # Fermeture fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Détection quand le joueur maintient ou relache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Vérifie si c'est bien un click droit
            game.start_shooting = True
            # Vérification si on click sur le bouton play
            if play_button_rect.collidepoint(event.pos) and not game.is_playing:
                # Lancer le jeu
                game.start()
            # Vérification si on click sur les boutons d'améliorations
            elif attack_button_rect.collidepoint(event.pos):
                # Augmenter l'attaque
                game.player.increase_attack()
            elif health_button_rect.collidepoint(event.pos):
                # Augmenter la vie
                game.player.increase_health()
            elif income_button_rect.collidepoint(event.pos):
                # Augmenter les récompenses en tuant des monstres
                game.player.increase_income()
            elif research_button_rect.collidepoint(event.pos):
                # Augmenter la taille des projectiles
                game.player.increase_research()
            elif projectile_button_rect.collidepoint(event.pos):
                # Augmenter la vitesse max d'attaque
                game.player.increase_projectile_velocity()
            elif speed_button_rect.collidepoint(event.pos):
                game.player.increase_speed()
            elif speed_attack_button_rect.collidepoint(event.pos):
                game.player.increase_speed_attack()
            # Vérification si on click sur les boutons consommables
            elif potion_rect.collidepoint(event.pos):
                # Achète une potion de vie pour le joueur
                game.player.potion()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            game.start_shooting = False





