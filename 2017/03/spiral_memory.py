import itertools

input = 277678

def spiral(input):
    # Represent spiral as 2D array, implemented as a dict of
    # tuples of (x,y) coordinates
    grid = {}

    # The length of the current side in the spiral
    side = 1

    # Variables holding current location in the grid and spiral
    row = 0
    column = 0
    location = 1
    horizontal = True
    quarter_rotations = 0
    grid[(0,0)] = 1

    # Alternate between walking right/up/down/left
    increment = lambda x: x + 1
    decrement = lambda x: x - 1

    data_carried = False
    value_written = False

    while location < input:
        for i in range(side):
            # Initialize cell, except for the starting cell
            if location != 1:
                grid[(row,column)] = 0
            # Check neighbors
            for j in itertools.product([-1, 0, 1], [-1, 0, 1]):
                try:
                    # Don't check yourself
                    if j != (0,0):
                        grid[(row,column)] += grid[(row+j[0],column+j[1])]
                except KeyError:
                    continue
            if location >= input and not data_carried:
                distance = abs(row) + abs(column)
                data_carried = True
            if grid[(row,column)] > input and not value_written:
                largest_value = grid[(row, column)]
                value_written = True
            if data_carried and value_written:
                return (distance, largest_value)
            if horizontal:
                column = increment(column)
            else:
                row = decrement(row)
            location += 1
        horizontal = not horizontal
        quarter_rotations += 1
        if quarter_rotations % 2 == 0:
            # Extend spiral
            side += 1
            # Change direction so we spiral around
            increment, decrement = decrement, increment


distance, largest_value = spiral(input)
print "%d steps required to carry data" % distance
print "%d is first value written larger than input" % largest_value
