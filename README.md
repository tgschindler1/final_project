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

Package can be installed from github and ran in Python3.
https://github.com/tgschindler1/final_project/blob/main

```bash
pip install montecarlo
```

```python
from montecaro.montecarlo import Die, Game, Analyzer

self.faces = np.array([1, 2, 3, 4, 5, 6])
self.die_one = Die(self.faces)
self.die_two = Die(self.faces)
self.die_three = Die(self.faces)
self.dice = [self.die_one, self.die_two, self.die_three]
self.game = Game(self.dice)
self.game.play(100)
self.analyzer = Analyzer(self.game)
```

