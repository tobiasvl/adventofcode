from collections import deque

def play(players, goal):
    ring = deque([0])
    elves = [0] * players

    for lowest in range(1, goal):
        if lowest % 23 != 0:
            ring.rotate(-1)
            ring.append(lowest)
        else:
            ring.rotate(7)
            elves[lowest % players] += lowest + ring.pop()
            ring.rotate(-1)

    return max(elves)

print play(459, 72103)
print play(459, 72103 * 100)
