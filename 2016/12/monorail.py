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


def get_value(x):
    try:
        return int(x)
    except ValueError:
        return regs[x]


def run(ignition = False):
    i = 0

    for reg in regs:
        regs[reg] = 0

    if ignition:
        regs['c'] = 1

    while i >= 0 and i < len(instructions):
        instruction = instructions[i]['operation']
        operands = instructions[i]['operands']
        if instruction == 'jnz':
            if get_value(operands[0]) != 0:
                i += get_value(operands[1])
                continue
        elif instruction == 'cpy':
            regs[operands[1]] = get_value(operands[0])
        elif instruction == 'dec':
            regs[operands[0]] -= 1
        elif instruction == 'inc':
            regs[operands[0]] += 1
        i += 1
    return regs['a']

print "Register a holds the value %d" % run()
print "With ignition key, register a holds the value %d" % run(True)
