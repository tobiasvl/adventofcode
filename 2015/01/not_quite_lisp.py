with open('input.txt') as f:
    elevator = ''.join([line.strip() for line in f])

floor = 0
basement = 0
basement_reached = False

for instruction in elevator:
    if instruction == '(':
        floor += 1
    elif instruction == ')':
        floor -= 1
    if not basement_reached:
        basement += 1
        if floor == -1:
            basement_reached = True

print "Santa ended up at floor %d" % floor
print "He first entered the basement at instruction %d" % basement
