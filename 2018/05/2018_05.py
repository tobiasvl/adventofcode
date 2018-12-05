import collections
import string

with open("input.txt") as f:
    polymer = f.read().strip('\n')

def react(polymer):
    result = collections.deque()
    for c in polymer:
        if len(result) > 0:
            c2 = result[-1]
            if c.lower() == c2.lower() and ((c.islower() and c2.isupper()) or (c2.islower() and c.isupper())):
                result.pop()
                continue
        result.append(c)
    return result

print len(react(polymer))

print min(map(len, [react(polymer.replace(l[0], '').replace(l[1], '')) for l in zip(string.lowercase, string.uppercase)]))
