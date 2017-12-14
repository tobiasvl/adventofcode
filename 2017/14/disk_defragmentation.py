import sys
sys.path.append('../10')
from knot_hash import knot_hash

input = "xlqgujun"

grid = []
for i in range(128):
    grid.append(format(int(knot_hash("%s-%d" % (input, i)), 16), '0128b'))

print "%d squares are used in the grid" % sum(n.count('1') for n in grid)

# by god
neighbors = {(line, char):
             [(x, y) for x, y in
                 ((line, char-1), (line-1, char), (line, char+1), (line+1, char))
                 if x >= 0 and y >= 0 and x < 128 and y < 128 and grid[x][y] == '1']
             for char in range(128) for line in range(128) if grid[line][char] == '1'}

# What follows is basically my day 12 solution,
# a depth-first search
visited = set()


def find_neighbors(square):
    if square in visited:
        return
    if grid[square[0]][square[1]] == '0':
        return
    visited.add(square)
    if square in neighbors:
        for s in neighbors[square]:
            find_neighbors(s)


regions = 0

for s in neighbors:
    if s not in visited and grid[s[0]][s[1]] == '1':
        find_neighbors(s)
        regions += 1

print "There are %d regions in the grid" % regions
