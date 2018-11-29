def assemble():
    instructions = []
    regs = {}

    with open('input.txt') as f:
        for line in f:
            element = line.strip().split()
            instructions.append({'operation': element[0],
                                'operands': tuple(element[1:])})
            try:
                int(element[1])
            except ValueError:
                regs.update({element[1]: 0})
    return (regs, instructions,)


def run(eggs, regs, instructions, optimize=False):
    def get_value(x):
        try:
            return int(x)
        except ValueError:
            return regs[x]


    regs['a'] = eggs
    i = 0

    while i >= 0 and i < len(instructions):
        instruction = instructions[i]['operation']
        operands = instructions[i]['operands']
        if optimize and i == 5:
            regs['a'] += regs['c'] * regs['d']
            i += 5
            continue
        if instruction == 'jnz':
            if get_value(operands[0]) != 0:
                i += get_value(operands[1])
                continue
        elif instruction == 'cpy':
            try:
                regs[operands[1]] = get_value(operands[0])
            except IndexError:
                pass
        elif instruction == 'dec':
            try:
                regs[operands[0]] -= 1
            except IndexError:
                pass
        elif instruction == 'inc':
            try:
                regs[operands[0]] += 1
            except IndexError:
                pass
        elif instruction == 'tgl':
            tgl_i = i + get_value(operands[0])
            try:
                toggle = instructions[tgl_i]
            except IndexError:
                pass
            else:
                if len(toggle['operands']) == 1:
                    if toggle['operation'] == 'inc':
                        toggle['operation'] = 'dec'
                    else:
                        toggle['operation'] = 'inc'
                elif len(toggle['operands']) == 2:
                    if toggle['operation'] == 'jnz':
                        toggle['operation'] = 'cpy'
                    else:
                        toggle['operation'] = 'jnz'
        i += 1
    return regs['a']

print "Value to send to the safe: %d" % run(7, *assemble())
print "Actual value to send to the safe: %d" % run(12, *assemble(), optimize=True)
