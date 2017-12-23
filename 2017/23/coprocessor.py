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


def run(debug=False):
    i = 0
    muls = 0

    for reg in regs:
        regs[reg] = 0
    if debug:
        regs['a'] = 1

    while i >= 0 and i < len(instructions):
        instruction = instructions[i]['operation']
        operands = instructions[i]['operands']
        if instruction == 'jnz':
            if get_value(operands[0]) != 0:
                i += get_value(operands[1])
                continue
        elif instruction == 'set':
            regs[operands[0]] = get_value(operands[1])
        elif instruction == 'sub':
            regs[operands[0]] -= get_value(operands[1])
        elif instruction == 'mul':
            regs[operands[0]] *= get_value(operands[1])
            muls += 1
        i += 1
    return muls

print "The mul instruction is invoked %d times" % run()
#run(True)
#print regs['h']
