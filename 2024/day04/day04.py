#!/usr/bin/python3

import re

# Override lists and strings so negative indices don't wrap around
class gridlist(list):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError("Negative index")
        return list.__getitem__(self, n)

class gridstring(str):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError("Negative index")
        return str.__getitem__(self, n)

# Please don't read this code.
def search(grid, m, y):
    matches = 0
    try:
        if grid[y - 1][m] == 'M':
            if grid[y - 2][m] == 'A':
                if grid[y - 3][m] == 'S':
                    matches += 1
    except IndexError:
        pass
    try:
        if grid[y + 1][m] == 'M':
            if grid[y + 2][m] == 'A':
                if grid[y + 3][m] == 'S':
                    matches += 1
    except IndexError:
        pass
    try:
        if grid[y - 1][m - 1] == 'M':
            if grid[y - 2][m - 2] == 'A':
                if grid[y - 3][m - 3] == 'S':
                    matches += 1
    except IndexError:
        pass
    try:
        if grid[y + 1][m + 1] == 'M':
            if grid[y + 2][m + 2] == 'A':
                if grid[y + 3][m + 3] == 'S':
                    matches += 1
    except IndexError:
        pass
    try:
        if grid[y - 1][m + 1] == 'M':
            if grid[y - 2][m + 2] == 'A':
                if grid[y - 3][m + 3] == 'S':
                    matches += 1
    except IndexError:
        pass
    try:
        if grid[y + 1][m - 1] == 'M':
            if grid[y + 2][m - 2] == 'A':
                if grid[y + 3][m - 3] == 'S':
                    matches += 1
    except IndexError:
        pass
    return matches

def check_slash(grid, m, y):
    try:
        if grid[y - 1][m + 1] == 'M':
            if grid[y + 1][m - 1] == 'S':
                return True
            else:
                pass
        else:
            pass
    except IndexError:
        return False
    try:
        if grid[y - 1][m + 1] == 'S':
            if grid[y + 1][m - 1] == 'M':
                return True
            else:
                pass
        else:
            pass
    except IndexError:
        return False
    return False

def check_backslash(grid, m, y):
    try:
        if grid[y - 1][m - 1] == 'M':
            if grid[y + 1][m + 1] == 'S':
                return True
            else:
                pass
        else:
            pass
    except IndexError:
        return False
    try:
        if grid[y - 1][m - 1] == 'S':
            if grid[y + 1][m + 1] == 'M':
                return True
            else:
                pass
        else:
            pass
    except IndexError:
        return False
    return False

def searchcross(grid, m, y):
    return check_slash(grid, m, y) and check_backslash(grid, m, y)

def main():
    with open('input') as f:
        grid = gridlist([gridstring(line.strip()) for line in f])

    part1 = 0

    for y in range(len(grid)):
        part1 += len([m for m in re.finditer('XMAS', grid[y])])
        part1 += len([m for m in re.finditer('SAMX', grid[y])])

        x = [m.start() for m in re.finditer('X', grid[y])]

        for m in x:
            part1 += search(grid, m, y)

    print(part1)

    part2 = 0

    for y in range(len(grid)):
        x = [m.start() for m in re.finditer('A', grid[y])]

        for m in x:
            part2 += searchcross(grid, m, y)

    print(part2)

if __name__ == "__main__":
    main()
