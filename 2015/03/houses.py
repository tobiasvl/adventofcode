with open('input.txt') as f:
    input = f.readline()

def deliver_presents(robot_active=False):
    grid = {}
    grid[(0,0)] = 1
    grid_robot = {}
    grid_robot[(0,0)] = 1
    
    row = 0
    row_robot = 0
    column = 0
    column_robot = 0
    
    for direction in input:
        if direction == '<':
            column -= 1
        elif direction == '>':
            column += 1
        elif direction == '^':
            row -= 1
        elif direction == 'v':
            row += 1
        try:
            grid[(row, column)] += 1
            grid_robot[(row, column)] += 1
        except KeyError:
            grid[(row, column)] = 1
            grid_robot[(row, column)] = 1
        if robot_active:
            row, row_robot = row_robot, row
            column, column_robot = column_robot, column

    return len(grid)

print "%s get presents from Santa the first year" % deliver_presents()
print "%s get presents from Santa and Robo-Santa the next year" % deliver_presents(True)
