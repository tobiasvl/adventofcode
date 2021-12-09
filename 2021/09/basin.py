#!/usr/bin/python3
from functools import reduce
adjacent = [
        lambda y, x: (y - 1, x),
        lambda y, x: (y + 1, x),
        lambda y, x: (y, x - 1),
        lambda y, x: (y, x + 1),
]

def is_low(depths, y, x):
    point = depths[y][x]
    for adj in adjacent:
        _y, _x = adj(y, x)
        if _y < 0 or _x < 0 or _y >= len(depths) or _x >= len(depths[0]):
            continue
        if point >= depths[_y][_x]:
            return False
    return True

def recurse_basin(depths, y, x, basin):
    if y < 0 or x < 0 or y >= len(depths) or x >= len(depths[0]):
        return basin
    for adj in adjacent:
        _y, _x = adj(y, x)
        if _y < 0 or _x < 0 or _y >= len(depths) or _x >= len(depths[0]):
            continue
        if depths[y][x] >= depths[_y][_x] or depths[_y][_x] == 9:
            continue
        basin.add((_y, _x))
        basin |= recurse_basin(depths, _y, _x, basin)
    return basin | {(y, x)}

def main():
    with open('input') as f:
        depths = [[int(height) for height in line.strip()] for line in f]

    low_points = []
    width = len(depths[0])
    for y in range(len(depths)):
        for x in range(width):
            if is_low(depths, y, x):
                low_points.append((y, x))

    print(sum(depths[y][x] + 1 for y, x in low_points))

    print(reduce(lambda x, y: x * y, (sorted(len(recurse_basin(depths, y, x, set())) for y, x in low_points))[-3:]))

if __name__ == "__main__":
    main()
