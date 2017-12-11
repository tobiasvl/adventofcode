with open('input.txt') as f:
    steps = f.readline().strip().split(',')

x = 0
y = 0
z = 0
max_distance = 0

for direction in steps:
    if direction == 'n':
        x -= 1
        z += 1
    elif direction == 'nw':
        x -= 1
        y += 1
    elif direction == 'ne':
        y -= 1
        z += 1
    elif direction == 'sw':
        y += 1
        z -= 1
    elif direction == 'se':
        x += 1
        y -= 1
    elif direction == 's':
        x += 1
        z -= 1
    distance = sum(filter(lambda x: x > 0, (x, y, z)))
    if distance > max_distance:
        max_distance = distance

print "The child process can be reached in %d steps" % distance
print "The furthest the child process got was %d steps" % max_distance
