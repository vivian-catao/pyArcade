import unittest
from guessing_game import *

class Test_guessing_game_behaviour(unittest.TestCase):
    #def setUp(self):
    #    pass
    
    def test_if_the_player_is_right_returns_congrats(self):
        n_secret = 30
        guess = 30
        self.assertEqual('Congrats', divination(n_secret, guess))
    
    def test_if_the_player_is_wrong_returns_higher_or_lower(self):
        for guess in range(1, 50):
            n_secret = 51
            print(guess)
            self.assertEqual('higher', divination(n_secret, guess))
        
        for guess in range(51,100):
            n_secret = 50
            print(guess)
            self.assertEqual('lower', divination(n_secret, guess))

if __name__=='__main__':
    unittest.main()