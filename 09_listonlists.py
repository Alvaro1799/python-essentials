row = []
WHITE_PAWN = "white_pawn"

for i in range(8):
    row.append(WHITE_PAWN)
'''
It builds a list containing eight elements representing the second row of the 
chessboard ‒ the one filled with pawns (assume that WHITE_PAWN is a 
predefined symbol representing a white pawn).'''


'''
A list comprehension is actually a list, but created on-the-fly during program execution, 
and is not described statically.

Take a look at the snippet:
'''

row = [WHITE_PAWN for i in range(8)]

#Example 1
squares = [x ** 2 for x in range(10)]
'''The snippet produces a ten-element list filled with squares of ten integer numbers 
starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)'''

#Example 2
twos = [2 ** i for i in range(8)]
'''The snippet creates an eight-element array containing the first eight powers of 
two (1, 2, 4, 8, 16, 32, 64, 128)'''

#Example 3
odds = [x for x in squares if x % 2 != 0 ]
'''The snippet makes a list with only the odd elements of the squares list'''


'''Let's also assume that a predefined symbol 
named EMPTY designates an empty field on the chessboard.
So, if we want to create a list of lists representing the whole chessboard, 
it may be done in the following way:'''
board = []
EMPTY = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

'''Note:

    the inner part of the loop creates a row consisting of eight elements 
    (each of them equal to EMPTY) and appends it to the board list;
    the outer part repeats it eight times;
    in total, the board list consists of 64 elements (all equal to EMPTY)

This model perfectly mimics the real chessboard, which is in fact 
an eight-element list of elements, all being single rows. Let's summarize our observations:

    the elements of the rows are fields, eight of them per row;
    the elements of the chessboard are rows, eight of them per chessboard.

The board variable is now a two-dimensional array. It's also called, 
by analogy to algebraic terms, a matrix.'''

'''As list comprehensions can be nested, we can shorten the board creation in the following way:'''
board = [[EMPTY for i in range(8)] for j in range(8)]

'''Access to the selected field of the board requires two indices ‒ 
the first selects the row; the second ‒ the field number inside the row, 
which is de facto a column number.'''