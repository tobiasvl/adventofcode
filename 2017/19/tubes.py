with open('input.txt') as f:
    diagram = [line for line in f]


def next_location(location, direction):
    if direction == 'down':
        return (location[0] + 1, location[1])
    elif direction == 'up':
        return (location[0] - 1, location[1])
    elif direction == 'left':
        return (location[0], location[1] - 1)
    elif direction == 'right':
        return (location[0], location[1] + 1)


def follow_junction(location, direction):
    if direction == 'down' or direction == 'up':
        if location[1] - 1 >= 0 and diagram[location[0]][location[1] - 1] == '-':
            return ((location[0], location[1] - 1), 'left')
        if location[1] + 1 < len(diagram[0]) and diagram[location[0]][location[1] + 1] == '-':
            return ((location[0], location[1] + 1), 'right')
    elif direction == 'left' or direction == 'right':
        if location[0] - 1 >= 0 and diagram[location[0] - 1][location[1]] == '|':
            return ((location[0] - 1, location[1]), 'up')
        elif location[0] + 1 < len(diagram) and diagram[location[0] + 1][location[1]] == '|':
            return ((location[0] + 1, location[1]), 'down')


location = (0, diagram[0].index('|'))
direction = 'down'
letters = []
steps = 0

while True:
    if diagram[location[0]][location[1]] == ' ':
        break
    elif diagram[location[0]][location[1]] == '+':
        location, direction = follow_junction(location, direction)
        steps += 1
        continue
    elif diagram[location[0]][location[1]].isalpha():
        letters.append(diagram[location[0]][location[1]])
    steps += 1
    location = next_location(location, direction)

print "The packet will see the letters %s" % ''.join(letters)
print "The packet needs to go %d steps" % steps
