## PS: Whitney+ is still under development

# whitney+

*Whitney+* is a decent tic-tac-toe engine , with new implemented features.


## Usage
When the engine starts, you'll see a screen like this:

~~~
Whitney+ iss playing as X.
~|~|~
~|?|~
~|~|~
~~~

Go ahead and draw a 3x3 grid somewhere, with an ? (? BEING A X OR A O) in the middle; for strategic reasons, this is always the first move that Whitney will make.

When you're ready to take your turn, write it down on your grid, and type the coordinates into Whitney. X goes from left to right and Y goes up to down; X=1 is the leftmost cell and Y=1 is the uppermost cell.

Whitney will take a short moment to choose a move, and then it will produce an output like this:

~~~
O|~|~
X|X|~
~|~|~
~~~

In this example, the user placed an O at `1,1` and Whitney placed an X at `1,2`. When you get one of these outputs, make sure to write the X from Whitney on your grid.

This will continue until eventually you either enter a tie or Whitney finds a way to win.

## Comparison to human players
Whitney is about as difficult at tic-tac-toe as a well-informed human might be. Worst-case, Whitney will make a move that causes a draw; it never loses unless there's a bug that I don't know about.

