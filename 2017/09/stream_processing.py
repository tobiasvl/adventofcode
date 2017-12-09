with open('input.txt') as f:
    stream = iter(f.readline())

group_score = 0
total_score = 0
garbage = 0

for character in stream:
    if character == '!':
        character = next(stream)
        continue
    elif character == '<':
        character = next(stream)
        while character != '>':
            if character == '!':
                character = next(stream)
            else:
                garbage += 1
            character = next(stream)
    elif character == '{':
        group_score += 1
        total_score += group_score
    elif character == '}':
        group_score -= 1

print "The total score for all groups is %d" % total_score
print "The number of non-canceled garbage is %d" % garbage
