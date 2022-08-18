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
Successfully loaded puzzle (took 0.0003650188446044922 seconds)
Searched solution depth 1 (8 possible paths, took 0.0005521774291992188 seconds)
Searched solution depth 2 (10 possible paths, took 0.005505084991455078 seconds)
Searched solution depth 3 (15 possible paths, took 0.0034568309783935547 seconds)
...
Searched solution depth 78 (242 possible paths, took 0.08317828178405762 seconds)
Searched solution depth 79 (201 possible paths, took 0.07758283615112305 seconds)
Searched solution depth 80 (159 possible paths, took 0.0615544319152832 seconds)
Found a solution of length 81 moves (took 7.984530925750732 seconds). Saving solution...
Solution saved to ./examples/queens_escape_solution.txt
```

## Todo
- Optimize this further if possible; it's not very fast. My tests showed the program took 5 seconds to solve "Queen's Escape", 75 seconds to solve "The Diabolical Box", and is not going to solve "The Time Machine" anytime soon (I gave up after 10 minutes).
  - Granted, puzzles like "The Diabolical Box" and "The Time Machine" don't benefit much from trimming move paths because every piece shape is unique. Worse, the latter quickly suffers from Exploding Tree™; it broke the 100000-path mark 22 moves in, and as of the 25th move there were nearly 400000 possibilities.
- Add support for moving multiple pieces at once under certain circumstances (this would allow it to solve "Touch Stone" from *Last Specter/Spectre's Call*, albeit with a slightly incorrect move count)

## Thanks
Credit goes to this article for giving me the push I needed to actually try this. I decided to use Python instead of Scala as the author did here (and took the chance to brush up on it), but much of the same concepts apply.  
https://alaraph.com/2021/09/10/solving-the-klotski-puzzle-in-scala/
