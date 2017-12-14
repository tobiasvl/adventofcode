import sys
sys.path.append('../10')
from knot_hash import knot_hash

input = "xlqgujun"

grid = []
for i in range(128):
    grid.append(format(int(knot_hash("%s-%d" % (input, i)), 16), '0128b'))

print "%d squares are used in the grid" % sum(n.count("1") for n in grid)
