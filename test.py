import unittest
import gameengine
import mainview
import enemy
import pygame
import shelve


class GameEngineTests(unittest.TestCase):

    def setUp(self):
        """Creates Game object needed for the tests."""
        self.screen = pygame.display.set_mode((600, 600))
        self.game = gameengine.Game(self.screen, "koshi.bmp",
                        "koshi_dead.bmp", "Field.jpg",
                        "rain.wav")

    def test_shelve_db(self):
        """Tests geting information from the data base."""
        highscore = shelve.open('highscore.db')
        highscore["score"] = 5
        highscore.close()
        score = self.game.get_score()
        print('\n get from db test: ' + str(score), '\n')
        self.assertEqual(5, score)

    def test_save_in_db(self):
        """Tests saving in the data base."""
        before = self.game.get_score()
        print('\n before save: ' + str(before), '\n')
        self.game.save_score(before + 1)
        after = self.game.get_score()
        print(' after save: ' + str(after), '\n')
        self.assertEqual(after, before + 1)

    def test_font_displaying(self):
        """Tests what happens when font file is missing."""
        self.assertRaises(Exception,
                          self.game.show_text('DOES NOT EXIST', 'test', 5, 5))
        print('\n default font loaded')

    def test_mouse_clicks_coordinates(self):
        """Tests if clicks are detected properly."""
        click = self.game.strike_checker((10, 10), 5, 5)
        self.assertTrue(click)
        print('\n click in the image area detected', '\n')
        click = self.game.strike_checker((10, 10), 100, 100)
        self.assertFalse(click)
        print(' click outside the image area detected', '\n')

    def test_time_bounds(self):
        """Tests if time bounds are detected properly."""
        time = self.game.time_checker(2000, 1000, 1500)
        self.assertFalse(time)
        print('\n not in time bounds', '\n')
        time = self.game.time_checker(2000, 1000, 4000)
        self.assertTrue(time)
        print(' in time bounds', '\n')

if __name__ == '__main__':
    unittest.main()
