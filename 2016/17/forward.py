import hashlib
from collections import deque

rooms = []
for i in range(6*4):
    if i % 6 == 0 or i % 6 == 5:
        rooms.append(False)
    else:
        rooms.append(True)

directions = "UDLR"
moves = [-6, 6, -1, 1]

def move(passcode="ihgpwlah", longest=False):
    longest_path = 0
    queue = deque([(1, "",)])

    while len(queue) > 0:
        state = queue.popleft()
        room = state[0]
        path = state[1]
        md5 = hashlib.md5(passcode + path).hexdigest()[:4]
        for char, direction, move in zip(md5, directions, moves):
            if char in "bcdef":
                new_room = room + move
                if new_room > 0 and new_room < len(rooms) - 1 and rooms[new_room]:
                    if new_room == len(rooms) - 2:
                        if not longest:
                            return path + direction
                        else:
                            longest_path = len(path) + 1
                    else:
                        queue.append((new_room, path + direction,)) 
    return longest_path

print "The shortest path is %s" % move("qtetzkpl")
print "The length of the longest path is %s" % move("qtetzkpl", longest=True)
