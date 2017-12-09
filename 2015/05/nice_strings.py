import itertools

with open('input.txt') as f:
    strings = [line.strip() for line in f if line != '\n']

nice = 0

for string in strings:
    # Naughty strings contain fewer than three vowels:
    if reduce(lambda x, y: x + y, map(string.count, "aeiou")) < 3:
        continue
    # Naughty strings contain no letters that appear twice in a row:
    if string == ''.join(ch for ch, _ in itertools.groupby(string)):
        continue
    # Naughty strings do not contain these particular substrings:
    if any(bad_sequence in string for bad_sequence in ['ab', 'cd', 'pq', 'xy']):
        continue
    nice += 1

new_nice = 0

for string in strings:
    # Naughty strings do not contain at least one letter which repeats
    # with exactly one letter between them:
    if not any(triple[0] == triple[2] for triple in zip(string, string[1:], string[2:])):
        continue
    # OK, this one is tougher. Can probably be improved.
    # Nice strings contain at least one pair of any two letters that
    # appears twice in the string without overlapping.
    # Generate all pairs:
    pairs = zip(string, string[1:])
    # Add the index of the first letter in the pair:
    for i in range(len(pairs)):
        pairs[i] = (i, pairs[i])
    # Compare all pairs with each other:
    combinations = itertools.combinations(pairs, 2) 
    for pair1, pair2 in combinations:
        if pair1[1] == pair2[1]:
            # If the pair's indices are not exactly one apart, that's nice:
            if not abs(pair1[0] - pair2[0]) == 1:
                new_nice += 1
                break

print "%d nice strings" % nice
print "%d nice strings under new rules" % new_nice
