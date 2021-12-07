import pygame


class Wave:

    def __init__(self, game):
        self.game = game
        self.wave_number = 1
        self.wave_already_lauched = [False] * 15

    def lunch_wave(self, screen):
        self.print_wave(screen)
        if self.wave_number == 1:
            if self.wave_already_lauched[0] is False:
                self.wave_1()
                self.wave_already_lauched[0] = True
        elif self.wave_number == 2:
            if self.wave_already_lauched[1] is False:
                self.wave_2()
                self.wave_already_lauched[1] = True
        elif self.wave_number == 3:
            if self.wave_already_lauched[2] is False:
                self.wave_3()
                self.wave_already_lauched[2] = True
        elif self.wave_number == 4:
            if self.wave_already_lauched[3] is False:
                self.wave_4()
                self.wave_already_lauched[3] = True
        elif self.wave_number == 5:
            if self.wave_already_lauched[4] is False:
                self.wave_5()
                self.wave_already_lauched[4] = True
        elif self.wave_number == 6:
            if self.wave_already_lauched[5] is False:
                self.wave_6()
                self.wave_already_lauched[5] = True
        elif self.wave_number == 7:
            if self.wave_already_lauched[6] is False:
                self.wave_7()
                self.wave_already_lauched[6] = True
        elif self.wave_number == 8:
            if self.wave_already_lauched[7] is False:
                self.wave_8()
                self.wave_already_lauched[7] = True
        elif self.wave_number == 9:
            if self.wave_already_lauched[8] is False:
                self.wave_9()
                self.wave_already_lauched[8] = True
        elif self.wave_number == 10:
            if self.wave_already_lauched[9] is False:
                self.wave_10()
                self.wave_already_lauched[9] = True
        elif self.wave_number == 11:
            if self.wave_already_lauched[10] is False:
                self.wave_11()
                self.wave_already_lauched[10] = True
        elif self.wave_number == 12:
            if self.wave_already_lauched[11] is False:
                self.wave_12()
                self.wave_already_lauched[11] = True
        elif self.wave_number == 13:
            if self.wave_already_lauched[12] is False:
                self.wave_13()
                self.wave_already_lauched[12] = True
        elif self.wave_number == 14:
            if self.wave_already_lauched[13] is False:
                self.wave_14()
                self.wave_already_lauched[13] = True
        elif self.wave_number == 15:
            if self.wave_already_lauched[14] is False:
                self.wave_15()
                self.wave_already_lauched[14] = True
        else:
            self.game.game_over()

    def print_wave(self, screen):
        # Afficher le numéro de wave
        font = pygame.font.Font(None, 40)
        text_wave = font.render("Wave " + str(self.wave_number), True, (255, 0, 0))
        screen.blit(text_wave, (screen.get_width() - 120, 5))

    def wave_1(self):
        while len(self.game.all_monsters_blop) < 1:
            self.game.spawn_monster()
            for monster in self.game.all_monsters_blop:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_blop.remove(monster)

    def wave_2(self):
        while len(self.game.all_monsters_blop) < 2:
            self.game.spawn_monster()
            for monster in self.game.all_monsters_blop:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_blop.remove(monster)

    def wave_3(self):
        while len(self.game.all_monsters_split) < 1:
            self.game.spawn_monster2()
            for monster in self.game.all_monsters_split:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_split.remove(monster)

    def wave_4(self):
        while len(self.game.all_monsters_split) < 1:
            self.game.spawn_monster2()
            for monster in self.game.all_monsters_split:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_split.remove(monster)

        while len(self.game.all_monsters_blop) < 1:
            self.game.spawn_monster()
            for monster in self.game.all_monsters_blop:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_blop.remove(monster)

    def wave_5(self):
        while len(self.game.all_monsters_split) < 1:
            self.game.spawn_monster2()
            for monster in self.game.all_monsters_split:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_split.remove(monster)

        while len(self.game.all_monsters_blop) < 2:
            self.game.spawn_monster()
            for monster in self.game.all_monsters_blop:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_blop.remove(monster)

    def wave_6(self):
        while len(self.game.all_monsters_split) < 2:
            self.game.spawn_monster2()
            for monster in self.game.all_monsters_split:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_split.remove(monster)

    def wave_7(self):
        while len(self.game.all_monsters_split) < 2:
            self.game.spawn_monster2()
            for monster in self.game.all_monsters_split:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_split.remove(monster)
        while len(self.game.all_monsters_blop) < 2:
            self.game.spawn_monster()
            for monster in self.game.all_monsters_blop:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_blop.remove(monster)

    def wave_8(self):
        while len(self.game.all_monsters_split) < 2:
            self.game.spawn_monster2()
            for monster in self.game.all_monsters_split:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_split.remove(monster)
        while len(self.game.all_monsters_blop) < 3:
            self.game.spawn_monster()
            for monster in self.game.all_monsters_blop:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_blop.remove(monster)

    def wave_9(self):
        while len(self.game.all_monsters_split) < 3:
            self.game.spawn_monster2()
            for monster in self.game.all_monsters_split:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_split.remove(monster)
        while len(self.game.all_monsters_blop) < 3:
            self.game.spawn_monster()
            for monster in self.game.all_monsters_blop:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_blop.remove(monster)

    def wave_10(self):
        #Vague boss !!
        self.game.spawn_monster()
        for monster in self.game.all_monsters:
            monster.boss = True
            monster.angry = True
            monster.attack = 60
            monster.health_upgrade = 10
            monster.gold_reward_blop = 200

    def wave_11(self):
        while len(self.game.all_monsters_split) < 4:
            self.game.spawn_monster2()
            for monster in self.game.all_monsters_split:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_split.remove(monster)
        while len(self.game.all_monsters_blop) < 4:
            self.game.spawn_monster()
            for monster in self.game.all_monsters_blop:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_blop.remove(monster)

    def wave_12(self):
        while len(self.game.all_monsters_split) < 6:
            self.game.spawn_monster2()
            for monster in self.game.all_monsters_split:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_split.remove(monster)

    def wave_13(self):
        while len(self.game.all_monsters_blop) < 8:
            self.game.spawn_monster()
            for monster in self.game.all_monsters_blop:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_blop.remove(monster)

    def wave_14(self):
        while len(self.game.all_monsters_split) < 6:
            self.game.spawn_monster2()
            for monster in self.game.all_monsters_split:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_split.remove(monster)
        while len(self.game.all_monsters_blop) < 6:
            self.game.spawn_monster()
            for monster in self.game.all_monsters_blop:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_blop.remove(monster)

    def wave_15(self):
        while len(self.game.all_monsters_split) < 7:
            self.game.spawn_monster2()
            for monster in self.game.all_monsters_split:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_split.remove(monster)
        while len(self.game.all_monsters_blop) < 7:
            self.game.spawn_monster()
            for monster in self.game.all_monsters_blop:
                temp = pygame.sprite.Group(self.game.all_monsters)
                temp.remove(monster)
                if self.game.check_collision(monster, temp):
                    self.game.all_monsters.remove(monster)
                    self.game.all_monsters_blop.remove(monster)
