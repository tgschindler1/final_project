import unittest
import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyzer

class DieTestSuite(unittest.TestCase):
    def setUp(self):
        self.faces = np.array([1, 2, 3, 4, 5, 6])
        self.die_one = Die(self.faces)
        self.die_two = Die(self.faces)
        self.die_three = Die(self.faces)
        self.dice = [self.die_one, self.die_two, self.die_three]
        self.game = Game(self.dice)
        self.game.play(100)
        self.analyzer = Analyzer(self.game)

    def test_die_init(self):
        self.assertEqual(len(self.die_one.df), len(self.faces))

    def test_change_weight(self):
        self.die_one.change_weight(1, 2)
        self.assertEqual(self.die_one.df.loc[1, 'weight'], 2)

    def test_roll(self):
        rolls = self.die_one.roll(4)
        self.assertEqual(len(rolls), 4)

    def test_die_show(self):
        df_copy = self.die_one.show()
        self.assertTrue(isinstance(df_copy, pd.DataFrame))
        
    def test_game_init(self):
        self.assertTrue(isinstance(self.dice, list))

    def test_play(self):
        self.game.play(10)
        self.assertEqual(len(self.game.play_result), 10)

    def test_game_show(self):
        game_copy = self.game.show()
        self.assertTrue(isinstance(game_copy, pd.DataFrame))

    def test_analyzer_init(self):
        self.assertTrue(isinstance(self.game, Game))
        
    def test_jackpot(self):
        jackpot_count = self.analyzer.jackpot()
        self.assertTrue(isinstance(jackpot_count, int))

    def test_face_counts_per_roll(self):
        counts_df = self.analyzer.face_counts_per_roll()
        self.assertTrue(isinstance(counts_df, pd.DataFrame))

    def test_combo_counts(self):
        combo_df = self.analyzer.combo_counts()
        self.assertTrue(isinstance(combo_df, pd.DataFrame))

    def test_permutation_counts(self):
        perm_df = self.analyzer.permutation_counts()
        self.assertTrue(isinstance(perm_df, pd.DataFrame))

if __name__ == '__main__':
    
    unittest.main(verbosity=3)
