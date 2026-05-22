### New Features:

1) Cleaner output
2) Better Bot messages
3) Safer try/Except

# whitney+

*Whitney+* is a decent tic-tac-toe engine , with new implemented features.


## Usage
When the engine starts, you'll see a screen like this:

~~~
Whitney+ is playing as X.
~|~|~
~|?|~
~|~|~
~~~

Go ahead and draw a 3x3 grid somewhere, with an X in the middle. For strategic reasons, this is always the first move that Whitney will make.

When you're ready to take your turn, write it down on your grid, and type the coordinates into Whitney. X goes from left to right and Y goes up to down; X=1 is the leftmost cell and Y=1 is the uppermost cell.

Whitney will make a output like:
~~~
O|~|~
X|X|~
~|~|~
~~~

In this example, the user placed an O at `1,1` and Whitney placed an X at `1,2`. When you get one of these outputs, make sure to write the X from Whitney on your grid.

This will continue until eventually you either enter a tie or Whitney finds a way to win.

## Comparison to human players
Whitney is about as difficult at tic-tac-toe as a well-informed human might be. Worst-case, Whitney will make a move that causes a draw, im not going to be confident and say it never loses, but its VERY unlikely.

Go ahead and use **Cython** to make it portable
