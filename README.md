# whitney
Whitney is a reasonably-powerful tic-tac-toe engine that never loses (or so I hope). Ties are common.

It always starts as X; support for starting as O might be added in the future.

## Usage
When the engine starts, you'll see a screen like this:

~~~
CPU is playing as X.
~|~|~
~|X|~
~|~|~
~~~

Go ahead and draw a 3x3 grid somewhere, with an X in the middle; for strategic reasons, this is always the first move that Whitney will make.

When you're ready to take your turn, write it down on your grid, and type the coordinates into Whitney. X goes from left to right and Y goes up to down; X=1 is the leftmost cell and Y=1 is the uppermost cell.

Whitney will take a short moment to choose a move, and then it will produce an output like this:

~~~
O|~|~
X|X|~
~|~|~
~~~

In this example, the user placed an O at `1,1` and Whitney placed an X at `1,2`. When you get one of these outputs, make sure to write the X from Whitney on your grid.

This will continue until eventually you either enter a tie or Whitney finds a way to win.
