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
Successfully loaded puzzle (took 0.0007970333099365234 seconds)
Searched solution depth 1 (8 possible paths, took 0.003138303756713867 seconds)
Searched solution depth 2 (10 possible paths, took 0.0069048404693603516 seconds)
Searched solution depth 3 (15 possible paths, took 0.009195327758789062 seconds)
...
Searched solution depth 78 (242 possible paths, took 0.520179271697998 seconds)
Searched solution depth 79 (201 possible paths, took 0.47776293754577637 seconds)
Searched solution depth 80 (159 possible paths, took 0.3911776542663574 seconds)
Found a solution of length 81 moves (took 39.795703649520874 seconds). Saving solution...
Solution saved to ./examples/queens_escape_solution.txt
```

## Todo
- Optimize this. It's really really slow right now; 40 seconds to solve the classic puzzle is bad enough, but half an hour to solve *Diabolical Box* is kind of embarrassing.
- Add support for moving multiple pieces at once under certain circumstances ("Touch Stone" from *Last Specter/Spectre's Call*)

## Thanks
Credit goes to this article for giving me the push I needed to actually try this. I decided to use Python instead of Scala as the author did here (and took the chance to brush up on it), but much of the same concepts apply.  
https://alaraph.com/2021/09/10/solving-the-klotski-puzzle-in-scala/
