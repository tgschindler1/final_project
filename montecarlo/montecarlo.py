import numpy as np
import pandas as pd

class Die:
    """
    A die has 'N' sides, or “faces”, and 'W' weights, and can be rolled
    to select a face.

    Each side contains a unique symbol. Symbols may be all alphabetic or
    all numeric.

    Weight defaults to 1.0 for each face but can be changed after the
    object is created.

    The die has one behavior, which is to be rolled one or more times.
    """
    def __init__(self, faces):
        """
        Takes a NumPy array of faces as an argument and throws a `TypeError` if
        not a NumPy array.
        
        Tests to see if the values are distinct and raises a `ValueError` if not.
        
        Internally initializes the weights to 1.0 for each face.

        Saves both faces and weights in a private data frame.
        """
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a NumPy array.")
        
        if np.unique(faces).size != faces.size:
            raise ValueError("Faces must be unique.")
        
        self._df = pd.DataFrame({'weight': 1.0}, index=faces)

    def change_weight(self, face, new_weight):
        """
        Takes two arguments: the face value to be changed and the new
        weight.

        Checks to see if the face passed is valid value, i.e. if it is in
        the die array. If not, raises an `IndexError`.

        Checks to see if the weight is a valid type, i.e. if it is numeric
        (integer or float) or castable as numeric. If not, raises a
        `TypeError`.
        """
        if face not in self._df.index:
            raise IndexError("Face not found in the die.")
        
        if not isinstance(new_weight, (int, float)):
            raise TypeError("Weight must be a numeric value.")

        self._df.loc[face, 'weight'] = new_weight

    def roll(self, num_rolls=1):
        """
        Takes a parameter of how many times the die is to be rolled;
        defaults to 1.

        Returns a Python list of outcomes.
        """
        outcomes = self._df.sample(n=num_rolls, replace=True, weights='weight').index.tolist()
        return outcomes
    

    def show(self):
        """
        Returns a copy of the private die data frame.
        """
        return self._df.copy()
    
    
class Game:
    """
    A game consists of rolling of one or more similar dice (Die objects)
    one or more times.

    Game objects have a behavior to play a game, i.e. to roll all of the
    dice a given number of times.

    Game objects only keep the results of their most recent play.
    """
    def __init__(self, dice):
        """
        Each game is initialized with a Python list that contains one or
        more dice.

        """
        self.dice = dice
        self._play_result = None 
        

    def play(self, rolls):
        """
        Takes an integer parameter to specify how many times the dice should
        be rolled.

        Saves the result of the play to a private data frame.
        """
        roll_result = {}
        for index, die in enumerate(self.dice):
            roll_result[index] = die.roll(rolls)
        
        self._play_result = pd.DataFrame(roll_result)

    def show(self, form='wide'):  
        """
        Returns a copy of the private play data frame
        
        Takes a parameter to return the data frame in narrow or wide form
        which defaults to wide form.
        """
        if form == 'wide':
            return self._play_result.copy()
        
        elif form == 'narrow':
            return pd.DataFrame(self._play_result.stack()).copy()
        
        else:
            raise ValueError("Form must be 'wide' or 'narrow'.")
            
            
class Analyzer:
    """
    An Analyzer object takes the results of a single game and computes
    various descriptive statistical properties about it.
    """
    def __init__(self, game):
        """
        Takes a game object as its input parameter. 
        
        Throws a `ValueError` if the passed value is not a Game object.
        """
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object.")
        
        self.game = game
        self.play_result = self.game.show()

    def jackpot(self):
        """
        A jackpot is a result in which all faces are the same, e.g. all ones
        for a six-sided die.

        Computes how many times the game resulted in a jackpot.

        Returns an integer for the number of jackpots.
        """
        jackpot = self.play_result.nunique(axis=1) == 1
        jackpot_sum = sum(jackpot)
        return jackpot_sum

    def face_counts_per_roll(self):
        """
        Computes how many times a given face is rolled in each event.

        For example, if a roll of five dice has all sixes, then the
        counts for this roll would be $5$ for the face value ‘6’ and $0$
        for the other faces.

        Returns a data frame of results.

        """
        face_counts = self.play_result.apply(pd.Series.value_counts, axis=1)
        face_counts = face_counts.fillna(0)
        return face_counts.copy()

    def combo_counts(self):
        """
        Computes the distinct combinations of faces rolled, along with their
        counts.

        Combinations are order-independent and may contain repetitions.

        Returns a data frame of results.
        """
        combos = self.play_result.apply(lambda row: sorted(row), axis=1)
        combo_counts = combos.apply(tuple).value_counts()
        combo_counts = pd.DataFrame(combo_counts)
        return combo_counts.copy()
    
    def permutation_counts(self):
        """
        Computes the distinct permutations of faces rolled, along with their
        counts.

        Permutations are order-independent and may contain repetitions.

        Returns a data frame of results.
        """
        permutations = self.play_result.apply(tuple, axis=1).value_counts()
        permutation_counts = pd.DataFrame(permutations)
        return permutation_counts.copy()
