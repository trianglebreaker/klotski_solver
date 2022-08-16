# klotski_solver
Solver for Klotski-like sliding block puzzles.

## Why?
I've been playing the Professor Layton games quite a bit recently; if you've played them before, I'm sure you know what this is all about. Sliding block puzzles are the hardest challenges those games have to offer, and I can count the ones I've actually solved without a guide on one hand. Naturally, the solution is to ~~meet the puzzles directly~~ make a computer do the thinking for me.

## Features
- Customizable board configuration; solves more than the classic puzzle ("Queen's Escape" from *Curious Village*)
- Support for irregularly shaped boards and pieces ("The Diabolical Box" from *Diabolical/Pandora's Box*)
- Support for multiple goal pieces ("The Time Machine" from *Unwound/Lost Future*)
- Writes the step-by-step solution to a file

The three puzzles mentioned above are included in the `examples` folder to show you how to format your own puzzles.

## Usage Example
(with verbose output turned on in the code)
```
$ python3 main.py ./examples/queens_escape.txt
Successfully loaded puzzle (took 0.0004177093505859375 seconds)
Searched solution depth 1 (8 possible paths, took 0.00613856315612793 seconds)
Searched solution depth 2 (10 possible paths, took 0.018468141555786133 seconds)
Searched solution depth 3 (15 possible paths, took 0.024233341217041016 seconds)
...
Searched solution depth 78 (242 possible paths, took 1.2743418216705322 seconds)
Searched solution depth 79 (201 possible paths, took 1.083054542541504 seconds)
Searched solution depth 80 (159 possible paths, took 0.8214399814605713 seconds)
Found a solution of length 81 moves (took 93.02886247634888 seconds). Saving solution...
Solution saved to ./examples/queens_escape_solution.txt
```

## Todo
- Optimize this. It's really really slow right now; 90 seconds to solve the classic puzzle is honestly kind of embarrassing.
- Add support for moving multiple pieces at once under certain circumstances ("Touch Stone" from *Last Specter/Spectre's Call*)

## Thanks
Credit goes to this article for giving me the push I needed to actually try this. I decided to use Python instead of Scala as the author did here (and took the chance to brush up on it), but much of the same concepts apply.  
https://alaraph.com/2021/09/10/solving-the-klotski-puzzle-in-scala/
