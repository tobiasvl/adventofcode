#!/usr/bin/python3
from collections import defaultdict
from itertools import permutations, combinations

def main():
    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]
        height = len(lines)
        width = len(lines[0])

        antennas = defaultdict(set)
        for y in range(height):
            for x in range(width):
                frequency = lines[y][x]
                if frequency != '.':
                    antennas[frequency].add((x, y))

    antinodes = set()
    antinodes_resonance = set()

    for frequency, location in antennas.items():
        for a, b in permutations(location, 2):
            vector = (a[0] - b[0], a[1] - b[1])

            vector = (a[0] + vector[0], a[1] + vector[1])
            if vector[0] < width and vector[0] >= 0 and vector[1] < height and vector[1] >= 0:
                antinodes.add(vector)

            vector = (a[0] - vector[0], a[1] - vector[1])
            while a[0] < width and a[0] >= 0 and a[1] < height and a[1] >= 0:
                antinodes_resonance.add(a)
                a = (a[0] - vector[0], a[1] - vector[1])


    print(len(antinodes))
    print(len(antinodes_resonance))

    #for y in range(height):
    #    for x in range(width):
    #        found = False
    #        for k,v in antennas.items():
    #            if (x,y) in v:
    #                found = True
    #                print(k, end='')
    #        if not found:
    #            if (x,y) in antinodes:
    #                print('#', end='')
    #            else:
    #                print('.', end='')
    #    print()


if __name__ == "__main__":
    main()
