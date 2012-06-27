import pygame
import sys
import gameengine
import pygame.mixer
from pygame.locals import *


class Chooser(object):

    def __init__(self, screen):
        """ Initializes Chooser object, loads images,
            loads pygame modules,loads sound, creates clock object.
        """
        self.clock = pygame.time.Clock()
        self.running = 1
        self.screen = screen
        self.azis = pygame.image.load("azis.bmp").convert()
        self.koshi = pygame.image.load("koshi.bmp").convert()
        self.bg = pygame.image.load("start.PNG").convert()
        pygame.font.init()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("test.wav")

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

    def main(self):
        """ Renders the initial scene of the game,
            listens for events and handle them."""
        while self.running:
            if pygame.event.peek():
                event = pygame.event.poll()
                if event.type == pygame.QUIT:
                    self.running = 0

                self.screen.fill((0, 0, 0))
                self.screen.blit(self.bg, (0, 0))
                self.screen.blit(self.azis, (200, 250))
                self.screen.blit(self.koshi, (380, 250))
                if (event.type == MOUSEBUTTONDOWN):
                    cordss = pygame.mouse.get_pos()
                    if (cordss[0] > 200 and cordss[0] < 200 + 58 and
                        cordss[1] > 250 and cordss[1] < 250 + 68):
                            self.sound.play()
                            gameengine.Game(self.screen, "azis.bmp",
                                             "azis_dead.bmp", "original.jpg",
                                             "jungle.wav").main()
                    if (cordss[0] > 380 and cordss[0] < 380 + 50 and
                        cordss[1] > 250 and cordss[1] < 250 + 70):
                            self.sound.play()
                            gameengine.Game(self.screen, "koshi.bmp",
                                             "koshi_dead.bmp", "Field.jpg",
                                             "rain.wav").main()
                self.show_text("Fonter.ttf", "izberi svoq protivnik", 150, 200)
                highscore = gameengine.Game.get_score(self)
                output = "naj-visok rezultat: " + str(highscore)
                self.show_text("Fonter.ttf", output, 150, 400)
                self.clock.tick(10)
                pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    Chooser(screen).main()
