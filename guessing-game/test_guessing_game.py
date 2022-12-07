import unittest
from guessing_game import *

class Test_guessing_game_parameters(unittest.TestCase):
    def test_default_is_valid(self):
        self.assertEqual(1, 1)

class Test_guessing_game_behaviour(unittest.TestCase):
    #def setUp(self):
    #    pass
    
    def test_if_the_player_is_right_returns_congrats(self):
        n_secret = 30
        guess = 30
        self.assertEqual('Congrats', divination(n_secret, guess))
    
    def test_if_the_player_is_wrong_returns_higher_or_lower(self):
        n_secret = 30
        guess = 20
        self.assertEqual('higher', divination(n_secret, guess))
        n_secret = 30
        guess = 50
        self.assertEqual('lower', divination(n_secret, guess))

if __name__=='__main__':
    unittest.main()