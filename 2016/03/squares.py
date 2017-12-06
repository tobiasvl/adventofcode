import itertools

with open('input.txt') as f:
    triangles = [[int(side) for side in line.strip().split()] for line in f if line != '\n']

impossible_triangles = 0

for triangle in triangles:
    for sides in itertools.permutations(triangle, 3):
        if sides[0] + sides[1] <= sides[2]:
            impossible_triangles += 1
            break

print "%d triangles are possible" % (len(triangles) - impossible_triangles)

impossible_triangles = 0

for row in xrange(0, len(triangles), 3):
    for column in range(3):
        triangle = [triangles[row][column], triangles[row+1][column], triangles[row+2][column]]
        for sides in itertools.permutations(triangle, 3):
            if sides[0] + sides[1] <= sides[2]:
                impossible_triangles += 1
                break

print "%d triangles by column are possible" % (len(triangles) - impossible_triangles)
