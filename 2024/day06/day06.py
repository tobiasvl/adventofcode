#!/usr/bin/python3
def main():
    with open('input') as f:
        grid = list([list(line.strip()) for line in f.readlines()])

    for row in range(len(grid)):
        try:
            column = grid[row].index('^')
            grid[row][column] = 'X'
            break
        except ValueError:
            pass

    transform = [
        (-1, 0), # 0, NORTH
        (0, 1),  # 1, EAST
        (1, 0),  # 2, SOUTH
        (0, -1)  # 3, WEST
    ]

    start = (row, column)

    def simulate(mark_visited=True):
        pos = start
        direction = 0
        visited = 1
        turns = set()

        while True:
            new_pos = (pos[0] + transform[direction][0], pos[1] + transform[direction][1])
            if new_pos[0] < 0 or new_pos[0] == len(grid) or new_pos[1] < 0 or new_pos[1] == len(grid[new_pos[0]]):
                # out of bounds
                return visited
            if grid[new_pos[0]][new_pos[1]] == '#':
                # hit an obstacle
                if (direction, pos) in turns:
                    return -1 # sentinel value for infinite loop
                turns.add((direction, pos))
                direction = (direction + 1) % 4
            else:
                # move
                pos = new_pos
                if grid[pos[0]][pos[1]] == '.':
                    if mark_visited:
                        grid[pos[0]][pos[1]] = 'X'
                    visited += 1

    print(simulate())

    loops = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (y, x) == start:
                continue
            if grid[y][x] == 'X':
                grid[y][x] = '#'
                if simulate(mark_visited=False) == -1:
                    loops += 1
                grid[y][x] = 'X'
    print(loops)

if __name__ == "__main__":
    main()
