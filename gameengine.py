import pygame
import sys
import enemy
import shelve
from pygame.locals import *


class Game(object):

    def __init__(self, screen, enemy, enemy_dead, field, sound):
        """ Initializes Game object.

            Keyword arguments:
            screen -- pygame screen
            enemy -- image of the enemy
            enemy_dead -- image of killed enemy
            field -- background image
            sound -- wav sound file

        """
        self.screen = screen
        self.setup_initial_variables(sound)
        self.setup_images(enemy, enemy_dead, field)
        self.setup_enemies()

    def setup_initial_variables(self, sound):
        """ Loads pygame modules,creates clock object,loads sound file,
            removes mouse cursor"""
        pygame.font.init()
        pygame.mixer.init()
        self.running = 1
        self.pressed_down = False
        self.strike = False
        self.time = 0
        self.hits = 0
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(0)
        self.sound = pygame.mixer.Sound(sound)
        self.sound_smash = pygame.mixer.Sound('smash.wav')

    def setup_images(self, enemy, enemy_dead, field):
        """ Loads images and set color that wont be displayed.
            Keyword arguments:
            enemy -- image of the enemy
            enemy_dead -- image of killed enemy
            field -- backgroun image
        """
        self.enemy_image = pygame.image.load(enemy).convert()
        self.enemy_image.set_colorkey((180, 180, 180))
        self.cursor = pygame.image.load("capture.png").convert()
        self.cursor.set_colorkey((0, 0, 0))
        self.enemy_dead = pygame.image.load(enemy_dead).convert()
        self.enemy_dead.set_colorkey((180, 180, 180))
        self.background = pygame.image.load(field).convert()
        self.bang = pygame.image.load("Bang!.bmp").convert()
        self.bang.set_colorkey((255, 255, 255))

    def setup_enemies(self):
        """ Creates Enemy objects and adds them to a list."""
        self.enemy1 = enemy.Enemy(160, 140, 1000, 3000,
                                  False, self.enemy_image)
        self.enemy2 = enemy.Enemy(351, 140, 2500, 4500,
                                  False, self.enemy_image)
        self.enemy3 = enemy.Enemy(355, 401, 4000, 6500,
                                  False, self.enemy_image)
        self.enemy4 = enemy.Enemy(200, 401, 6500, 8000,
                                  False, self.enemy_image)
        self.enemy5 = enemy.Enemy(258, 275, 8500, 10500,
                                  False, self.enemy_image)
        self.enemy6 = enemy.Enemy(460, 527, 10000, 12000,
                                  False, self.enemy_image)
        self.enemy7 = enemy.Enemy(45, 528, 12500, 13500,
                                  False, self.enemy_image)
        self.enemy8 = enemy.Enemy(255, 530, 13000, 15000,
                                  False, self.enemy_image)
        self.enemy9 = enemy.Enemy(450, 94, 14500, 16500,
                                  False, self.enemy_image)
        self.enemy10 = enemy.Enemy(62, 94, 16000, 18000,
                                   False, self.enemy_image)
        self.enemy11 = enemy.Enemy(242, 94, 18800, 20000,
                                   False, self.enemy_image)
        self.enemies = [self.enemy1, self.enemy2, self.enemy3,
                        self.enemy4, self.enemy5, self.enemy6, self.enemy7,
                        self.enemy8, self.enemy9, self.enemy10, self.enemy11]

    def strike_checker(self, mouse_click_coordinates, x_of_image, y_of_image):
        """ Check if a mouse click is in the area of an image.
            Keyword arguments:
            mouse_click_coordinates -- tuple containing x and y of the click
            x_of_image -- x coordinate of the image
            y_of_image -- y coordinate of the image
        """
        if (mouse_click_coordinates[0] > x_of_image
            and mouse_click_coordinates[0] < x_of_image + 50
            and mouse_click_coordinates[1] > y_of_image
            and mouse_click_coordinates[1] < y_of_image + 70):
            return True

    def get_score(self):
        """ Opens shelve database file and returns the saved score in it"""
        highscore = shelve.open('highscore.db')
        result = highscore.get('score')
        highscore.close()
        return result

    def save_score(self):
        """ If current score is higher than one saved in the shelve db
            current score is saved in the shelve db
        """
        if self.hits > self.get_score():
            highscore = shelve.open('highscore.db')
            highscore["score"] = self.hits
            highscore.close()

    def clear_screen(self):
        """ Displays only the backgroun image"""
        self.screen.blit(self.background, (0, 0))

    def paint_enemy(self, enemy_image, x, y):
        """ Displays the enemy image
            Keyword arguments:
            enemy_image -- image of the enemy
            x -- x coordinate of the image
            y -- y coordinate of the image
        """
        self.screen.blit(enemy_image, (x, y))

    def time_checker(self, time, born_time, death_time):
        """ Check if current time is in a particular bounds
            Keyword arguments:
            time -- passed time in ms
            born_time -- left bound of the interval
            death_time -- right bound of the interval
        """
        if(time > born_time and time < death_time):
            return True

    def show_text(self, font_name, text, x, y):
        """ Loads font if unable loads default font. Displays the text
            Kyword arguments:
            font_name -- ttf file
            text -- text that will be displayed
            x -- x coordinate of the text
            y -- y coordinate of the text
        """
        try:
            font = pygame.font.Font(font_name, 25)
        except Exception:
            font = pygame.font.Font(None, 25)
        output = font.render(text, True, (255, 255, 255), (159, 182, 205))
        self.screen.blit(output, (x, y))

    def draw_mouse(self):
        """ Displays image instead of mouse cursor"""
        mouse_cords = pygame.mouse.get_pos()
        self.screen.blit(self.cursor, (mouse_cords[0], mouse_cords[1]))

    def main(self):
        """ Renders game scene listens for events"""
        while self.running:
            if pygame.event.peek():
                if not pygame.mixer.get_busy():
                    self.sound.play()
                event = pygame.event.poll()
                if event.type == pygame.QUIT:
                    pygame.mouse.set_visible(1)
                    pygame.mixer.stop()
                    self.save_score()
                    score = self.get_score()
                    self.running = 0
                self.screen.fill((0, 0, 0))
                self.clear_screen()
                if event.type == MOUSEBUTTONDOWN:
                    cords = pygame.mouse.get_pos()
                    for enemy in self.enemies:
                        if (self.time_checker(self.time,
                                             enemy.born, enemy.died)
                                             and not enemy.hit):
                            enemy.hit = self.strike_checker(cords,
                                                            enemy.x, enemy.y)
                            if enemy.hit:
                                self.sound_smash.play()
                                enemy.image = self.bang
                                self.hits = self.hits + 1
                if (event.type == MOUSEBUTTONUP):
                    self.pressed_down = False
                    for enemy in self.enemies:
                        if enemy.hit:
                            enemy.image = self.enemy_dead
            self.time = self.time + self.clock.get_time()
            if self.time > 20001:
                self.time = 0
                for enemy in self.enemies:
                    enemy.hit = False
                    enemy.image = self.enemy_image
            for enemy in self.enemies:
                if self.time_checker(self.time, enemy.born, enemy.died):
                    self.paint_enemy(enemy.image, enemy.x, enemy.y)
                if self.time >= enemy.died:
                    self.clear_screen()
            output = 'tohki: ' + str(self.hits)
            self.show_text('Fonter.ttf', output, 5, 5)
            self.draw_mouse()
            self.clock.tick(60)
            pygame.display.update()
