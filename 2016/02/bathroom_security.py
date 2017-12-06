with open('input.txt') as f:
    instructions = [line.strip() for line in f if line != '\n']

imagined_layout = [['1', '2', '3'],
                   ['4', '5', '6'],
                   ['7', '8', '9']]

actual_layout = [[None, None, '1', None, None],
                 [None,  '2', '3',  '4', None],
                 [ '5',  '6', '7',  '8',  '9'],
                 [None,  'A', 'B',  'C', None],
                 [None, None, 'D', None, None]]

def input_code(keypad):
    row = 1
    column = 1
    code = ""
    
    for button in instructions:
        for direction in button:
            new_row = row
            new_column = column
            if direction == 'U':
                new_row -= 1
            elif direction == 'D':
                new_row += 1
            elif direction == 'L':
                new_column -= 1
            elif direction == 'R':
                new_column += 1
            # I'm regretting using Python, since negative indices are valid
            if new_row < 0 or new_column < 0:
                continue
            try:
                if not keypad[new_row][new_column]:
                    continue
            except IndexError:
                continue
            else:
                row, column = new_row, new_column
        code += keypad[row][column]
    return code


print "The bathroom code is " + input_code(imagined_layout)
print "The ACTUAL bathroom code is " + input_code(actual_layout)
