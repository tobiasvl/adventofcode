import itertools
import re

with open('input.txt') as f:
    instructions = [re.match('^(?P<action>[a-z ]*) (?P<startrow>[0-9]*),(?P<startcol>[0-9]*) through (?P<endrow>[0-9]*),(?P<endcol>[0-9]*)$',
                    line.strip()).groupdict()
                    for line in f]

for instruction in instructions:
    for k, v in instruction.iteritems():
        if k in ['startrow', 'endrow', 'startcol', 'endcol']:
            instruction[k] = int(v)

# Could do a deep copy instead perhaps
grid = []
for i in range(0, 1000):
    grid.append([])
    for _ in range(0, 1000):
        grid[i].append(False)

switch = {'turn on': lambda x: True,
          'turn off': lambda x: False,
          'toggle': lambda x: not x}

grid2 = []
for i in range(0, 1000):
    grid2.append([])
    for _ in range(0, 1000):
        grid2[i].append(0)

brightness_switch = {'turn on': lambda x: x + 1,
                     'turn off': lambda x: 0 if x == 0 else x - 1,
                     'toggle': lambda x: x + 2}

def follow_instructions(grid, switch):
    for instruction in instructions:
        for row in range(instruction['startrow'], instruction['endrow'] + 1):
            for column in range(instruction['startcol'], instruction['endcol'] + 1):
                grid[row][column] = switch[instruction['action']](grid[row][column])
    return grid

print "%d lights are lit" % sum(list(itertools.chain.from_iterable(follow_instructions(grid, switch))))
print "%d is the total brightness" % sum(list(itertools.chain.from_iterable(follow_instructions(grid2, brightness_switch))))
