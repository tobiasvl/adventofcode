import re
from itertools import product


def rotate_or_flip(square):
    # Generates all rotations and flips of a square
    return [square,
            tuple(''.join(i) for i in square[::-1]), # Flip
            tuple(''.join(i) for i in zip(*square[::-1])), # Rotate
            tuple(''.join(i) for i in zip(*square[::-1])[::-1]),
            tuple(''.join(i) for i in zip(*zip(*square[::-1])[::-1])),
            tuple(''.join(i) for i in zip(*zip(*square[::-1])[::-1])[::-1]),
            tuple(''.join(i) for i in zip(*zip(*zip(*square[::-1])[::-1])[::-1])[::-1]),
            tuple(''.join(i) for i in zip(*zip(*zip(*square[::-1])[::-1])[::-1]))]


rules = {}

with open('input.txt') as f:
    for line in f:
        k, v = re.findall('^([-#/\.]*) => ([-#/\.]*)$', line)[0]
        for transformation in rotate_or_flip(tuple(k.split('/'))):
            rules.update({tuple(transformation): tuple(v.split('/'))})


def enhance(iterations):
    pattern = ('.#.',
               '..#',
               '###')

    # This algorithm is a beautiful result of a lot of trial and error
    for _ in range(iterations):
        new_pattern = list('' for _ in range(len(pattern)))
        if len(pattern) % 2 == 0:
            j = 0
            old_coords = ()
            for i, m in product(zip(range(len(pattern))[0::2], range(len(pattern))[1::2]), repeat=2):
                if old_coords == ():
                    old_coords = i
                elif old_coords != i:
                    old_coords = i
                    j += 1
                square = (''.join((pattern[i[0]][m[0]], pattern[i[0]][m[1]])),
                        ''.join((pattern[i[1]][m[0]], pattern[i[1]][m[1]])))
                transformed = rules[square]
                try:
                    new_pattern[i[0] + j] += transformed[0]
                except IndexError:
                    new_pattern.insert(i[0] + j, transformed[0])
                try:
                    new_pattern[i[1] + j] += transformed[1]
                except IndexError:
                    new_pattern.insert(i[1] + j, transformed[1])
                try:
                    new_pattern[i[1] + 1 + j] += transformed[2]
                except IndexError:
                    new_pattern.insert(i[1] + 1 + j, transformed[2])
        elif len(pattern) % 3 == 0:
            j = 0
            old_coords = ()
            new_row = False
            for i, m in product(zip(range(len(pattern))[0::3], range(len(pattern))[1::3], range(len(pattern))[2::3]), repeat=2):
                if old_coords == ():
                    old_coords = i
                elif old_coords != i:
                    old_coords = i
                    j += 1
                square = (''.join((pattern[i[0]][m[0]], pattern[i[0]][m[1]], pattern[i[0]][m[2]])),
                        ''.join((pattern[i[1]][m[0]], pattern[i[1]][m[1]], pattern[i[1]][m[2]])),
                        ''.join((pattern[i[2]][m[0]], pattern[i[2]][m[1]], pattern[i[2]][m[2]])))
                transformed = rules[square]
                try:
                    new_pattern[i[0] + j] += transformed[0]
                except IndexError:
                    new_pattern.insert(i[0] + j, transformed[0])
                try:
                    new_pattern[i[1] + j] += transformed[1]
                except IndexError:
                    new_pattern.insert(i[1] + j, transformed[1])
                try:
                    new_pattern[i[2] + j] += transformed[2]
                except IndexError:
                    new_pattern.insert(i[2] + j, transformed[2])
                try:
                    new_pattern[i[2] + 1 + j] += transformed[3]
                except IndexError:
                    new_pattern.insert(i[2] + 1 + j, transformed[3])
        pattern = new_pattern

    counter = 0
    for row in pattern:
        counter += row.count('#')
    return counter

print enhance(5)
print enhance(18)
