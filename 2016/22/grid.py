import re
import itertools

grid = []

with open("input.txt") as f:
    f.readline() 
    f.readline()
    for line in f:
        node = {k: int(v) for k, v in re.match("/dev/grid/node-x(?P<x>\d+)-y(?P<y>\d+)\s+(?P<size>\d+)T\s+(?P<used>\d+)T\s+(?P<available>\d+)T", line).groupdict().iteritems()}
        grid.append(node)

viable = 0
for pair in itertools.permutations(grid, 2):
    a = pair[0]
    b = pair[1]
    if a != b and a["used"] != 0 and a["used"] <= b["available"]:
        viable += 1

print "Viable pairs: %d" % viable
