with open('input.txt') as f:
    directions = f.readline().strip().split(', ')

grid = {}

current_direction = 'N'
row = 0
column = 0
duplicate_found = False
duplicate_row = 0
duplicate_column = 0

for direction in directions:
    turn = direction[0]
    steps = int(direction[1:])
    if turn == 'L':
        if current_direction == 'N':
            current_direction = 'W'
        elif current_direction == 'W':
            current_direction = 'S'
        elif current_direction == 'S':
            current_direction = 'E'
        elif current_direction == 'E':
            current_direction = 'N'
    elif turn == 'R':
        if current_direction == 'N':
            current_direction = 'E'
        elif current_direction == 'E':
            current_direction = 'S'
        elif current_direction == 'S':
            current_direction = 'W'
        elif current_direction == 'W':
            current_direction = 'N'
    for i in range(steps):
        if current_direction == 'N':
            row -= 1
        elif current_direction == 'W':
            column -= 1
        elif current_direction == 'S':
            row += 1
        elif current_direction == 'E':
            column += 1
        if not duplicate_found:
            if (row, column) not in grid:
                grid[(row, column)] = True
            else:
                duplicate_row, duplicate_column = row, column
                duplicate_found = True

print "%d blocks to apparent Easter Bunny HQ location" % (abs(row) + abs(column))
print "%d blocks to first location visited twice" % (abs(duplicate_row) + abs(duplicate_column))
