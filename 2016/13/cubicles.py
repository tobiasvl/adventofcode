from collections import deque

def move(favorite=10, goal=(7,4,)):
    queue = deque([((1,1,), 0,)])
    maze = {(1,1,): True}
    visited = {(1,1,)}

    while len(queue) > 0:
        state = queue.popleft()
        room = state[0]
        steps = state[1]

        cur_x = room[0]
        cur_y = room[1]

        visited.add((cur_x, cur_y,))
        
        for new_room in ((-1,0,),(0,-1,),(0,1,),(1,0,),):
            x = cur_x + new_room[0]
            y = cur_y + new_room[1]
            if x >= 0 and y >= 0:
                try:
                    maze[(x, y,)]
                except KeyError:
                    binary = "{0:b}".format(x*x + 3*x + 2*x*y + y + y*y + favorite)
                    maze[(x, y,)] = binary.count("1") % 2 == 0
                if maze[(x, y,)] and not (x, y,) in visited:
                    if isinstance(goal, tuple):
                        if goal == (x, y,):
                            return steps + 1
                        queue.append(((x, y,), steps + 1,))
                    if isinstance(goal, int):
                        if steps < goal:
                            queue.append(((x, y,), steps + 1,))
    if isinstance(goal, int):
        return len(visited)

print "Fewest number of steps to reach 31,39: %s" % move(1352, (31,39,))
print "Reachable locations in 50 steps: %s" % move(1352, 50)
