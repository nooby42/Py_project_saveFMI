import unittest
import gameengine
import mainview
import enemy
import pygame
import shelve

class PrimesTest(unittest.TestCase):
    def test_shelve_db(self):
        highscore = shelve.open('highscore.db')
        highscore["score"] = 5
        highscore.close()
        screen = pygame.display.set_mode((600, 600))
        score = gameengine.Game(screen, "koshi.bmp",
                         "koshi_dead.bmp", "Field.jpg",
                         "rain.wav").get_score()
        print('get from db test: '+str(score))
        self.assertEqual(5, score)

    def test_save_in_db(self):
        screen = pygame.display.set_mode((600, 600))
        game = gameengine.Game(screen, "koshi.bmp",
                        "koshi_dead.bmp", "Field.jpg",
                        "rain.wav")
        before = game.get_score()
        print('before save: ' + str(before))
        game.save_score(before + 1)
        after = game.get_score()
        print('after save: ' + str(after))
        self.assertEqual(after, before + 1)

if __name__ == '__main__':
    unittest.main()
