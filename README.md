 # Final Project Report

* Class: DS 5100
* Student Name: Thomas Schindler
* Project Name: Montecarlo Simulator

The module will implement a simple [Monte Carlo
simulator](https://en.wikipedia.org/wiki/Monte_Carlo_method) using a set
of three related classes — a Die class, a Game class, and an Analyzer
class.

The classes are related in the following way: Game objects are
initialized with a Die object, and Analyzer objects are initialized with
a Game object.

\[Die\] &rarr; \[Game\] &rarr; \[Analyzer\]

# Installation

To install package, clone this repo https://github.com/tgschindler1/final_project.
cd into repo and run following comand.

```bash
pip install .
```

# Sample Usage

Import package:
```python
from montecaro.montecarlo import Die, Game, Analyzer
```
## Use Die class:
```python
faces = np.array([1, 2, 3, 4, 5, 6])
die_one = Die(faces)
die_two = Die(faces)
die_three = Die(faces)
die_one.change_weight(1, 5)
```

## Use Game class:
```python
dice = [die_one, die_two, die_three]
game = Game(dice)
game.play(100)
```

## Use Analyzer class:
```python
analyzer = Analyzer(game)
jackpot_count = analyzer.jackpot()
```
# Class Descriptions

## class Die(faces)
   
   -A die has 'N' sides, or “faces”, and 'W' weights, and can be rolled
   to select a face.
   
   -Each side contains a unique symbol. Symbols may be all alphabetic or
   all numeric.
   
   -Weight defaults to 1.0 for each face but can be changed after the
   object is created.
   
   -The die has one behavior, which is to be rolled one or more times.
   
   ### Methods defined here:
   
   **__init__(self, faces)**
   
   -Takes a NumPy array of faces as an argument and throws a `TypeError` if
    not a NumPy array.
    
   -Tests to see if the values are distinct and raises a `ValueError` if not.
    
   -Internally initializes the weights to 1.0 for each face.
    
   
   **change_weight(self, face, new_weight)**
   
  -Takes two arguments: the face value to be changed and the new
  weight.
  
  -Checks to see if the face passed is valid value, i.e. if it is in
  the die array. If not, raises an `IndexError`.
  
  -Checks to see if the weight is a valid type, i.e. if it is numeric
  (integer or float) or castable as numeric. If not, raises a
  `TypeError`.
   
   **roll(self, num_rolls=1)**
   
  -Takes a parameter of how many times the die is to be rolled;
  defaults to 1.
  
  -Returns a Python list of outcomes.
   
   **show(self)**
   
  -Returns data frame of die with its faces and weights.

## class Game(dice)
   
   -A game consists of rolling of one or more similar dice (Die objects)
   one or more times.
   
   -Game objects have a behavior to play a game, i.e. to roll all of the
   dice a given number of times.
   
   -Game objects only keep the results of their most recent play.
   
   ### Methods defined here:
   
   **__init__(self, dice)**
   
 -Each game is initialized with a Python list that contains one or
 more dice.
   
   **play(self, rolls)**
   
 -Takes an integer parameter to specify how many times the dice should
 be rolled.
   
   **show(self, form='wide')**
   
 -Returns a data frame of the play result.
 
 -Takes a parameter to return the data frame in narrow or wide form
 which defaults to wide form.
       
## class Analyzer(game)
   
   -An Analyzer object takes the results of a single game and computes
   various descriptive statistical properties about it.
   
   ### Methods defined here:
   
**__init__(self, game)**

 -Takes a game object as its input parameter. 
 
 -Throws a `ValueError` if the passed value is not a Game object.

**combo_counts(self)**

 -Computes the distinct combinations of faces rolled, along with their
 counts.
 
 -Combinations are order-independent and may contain repetitions.
 
 -Returns a data frame of results.

**face_counts_per_roll(self)**

 -Computes how many times a given face is rolled in each event.
 
 -For example, if a roll of five dice has all sixes, then the
 counts for this roll would be $5$ for the face value ‘6’ and $0$
 for the other faces.
 
 -Returns a data frame of results.

**jackpot(self)**

 -A jackpot is a result in which all faces are the same, e.g. all ones
 for a six-sided die.
 
 -Computes how many times the game resulted in a jackpot.
 
 -Returns an integer for the number of jackpots.

**permutation_counts(self)**

 -Computes the distinct permutations of faces rolled, along with their
 counts.
 
 -Permutations are order-independent and may contain repetitions.
 
 -Returns a data frame of results.
