import string
from itertools import combinations

with open('input.txt') as f:
    ids = [line.strip() for line in f]

twos = 0
threes = 0

for idx in ids:
    idx_list = [a for a in idx]
    twos_found = False
    threes_found = False
    for x in string.ascii_lowercase:
        if idx_list.count(x) == 2 and not twos_found:
            twos += 1
            twos_found = True
        if idx_list.count(x) == 3 and not threes_found:
            threes += 1
            threes_found = True

print twos * threes

def hamming_distance(s1, s2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

for s1, s2 in combinations(ids, 2):
    if hamming_distance(s1, s2) == 1:
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2:
                print s1.replace(ch1, '')
