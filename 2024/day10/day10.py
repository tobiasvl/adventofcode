#!/usr/bin/python3

# Override lists and strings so negative indices don't wrap around
class gridlist(list):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError("Negative index")
        return list.__getitem__(self, n)

transforms = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def adjacent(location):
    return [(location[0] + direction[0], location[1] + direction[1]) for direction in transforms]

def main():
    with open('input') as f:
        grid = gridlist([gridlist([int(a) for a in line.strip()]) for line in f.readlines()])

    trailheads = list()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                trailheads.append((y,x))

    def find(location, seen=None):
        if grid[location[0]][location[1]] == 9:
            if seen != None:
                if location in seen:
                    return 0
                seen.add(location)
            return 1
        score = 0
        for new_location in adjacent(location):
            try:
                if grid[new_location[0]][new_location[1]] == grid[location[0]][location[1]] + 1:
                    score += find(new_location, seen)
            except IndexError:
                pass
        return score

    print(sum([find(location, set()) for location in trailheads]))
    print(sum([find(location) for location in trailheads]))

if __name__ == "__main__":
    main()
