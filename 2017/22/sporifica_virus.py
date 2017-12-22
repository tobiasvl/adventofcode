with open('input.txt') as f:
    cluster = {}
    cluster_list = [line.strip() for line in f]


def infect(bursts, evolved=False):
    cluster = {}
    for row in range(len(cluster_list)):
        for column in range(len(cluster_list[0])):
            cluster[(row, column)] = cluster_list[row][column]
    direction = 'up'
    start = (len(cluster_list) / 2, len(cluster_list[0]) / 2)
    row, column = start
    burst = 0
    i = 0
    while i < bursts:
        if (row, column) not in cluster:
            cluster[(row, column)] = '.'
        if cluster[(row, column)] == '#':
            if direction == 'up':
                direction = 'right'
            elif direction == 'right':
                direction = 'down'
            elif direction == 'down':
                direction = 'left'
            elif direction == 'left':
                direction = 'up'
            if evolved:
                cluster[(row, column)] = 'F'
            else:
                cluster[(row, column)] = '.'
        elif cluster[(row, column)] == '.':
            if direction == 'up':
                direction = 'left'
            elif direction == 'right':
                direction = 'up'
            elif direction == 'down':
                direction = 'right'
            elif direction == 'left':
                direction = 'down'
            if evolved:
                cluster[(row, column)] = 'W'
            else:
                cluster[(row, column)] = '#'
                burst += 1
        elif cluster[(row, column)] == 'W' and evolved:
            burst += 1
            cluster[(row, column)] = '#'
        elif cluster[(row, column)] == 'F' and evolved:
            if direction == 'up':
                direction = 'down'
            elif direction == 'right':
                direction = 'left'
            elif direction == 'down':
                direction = 'up'
            elif direction == 'left':
                direction = 'right'
            cluster[(row, column)] = '.'
        if direction == 'up':
            row -= 1
        elif direction == 'right':
            column += 1
        elif direction == 'down':
            row += 1
        elif direction == 'left':
            column -= 1
        i += 1
    return burst


print "%d bursts infected a node" % infect(10000)
print "%d bursts infected a node by the evolved virus" % infect(10000000, True)
