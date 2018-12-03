import re

matches = []

with open('input.txt') as f:
    for line in f:
        match = re.match(r"#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)", line).groupdict()
        matches.append({k: int(v) for k, v in match.iteritems()})

fabric = []
for y in range(1000):
    fabric.append([])
    for x in range(1000):
        fabric[y].append([0, set()])

for k in matches:
    for y in range(k['y'], k['y'] + k['h']):
        for x in range(k['x'], k['x'] + k['w']):
            fabric[y][x][0] += 1
            fabric[y][x][1].add(k['id'])

overlap = 0
for y in fabric:
    for x in y:
        if x[0] > 1:
            overlap += 1
print overlap

for k in matches:
    intact = True
    for y in range(k['y'], k['y'] + k['h']):
        for x in range(k['x'], k['x'] + k['w']):
            if any(i != k['id'] for i in fabric[y][x][1]):
                intact = False
                break
    if intact:
        print k['id']
