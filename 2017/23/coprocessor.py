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


def run_debug():
    i = 0
    muls = 0

    for reg in regs:
        regs[reg] = 0

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

print "The mul instruction is invoked %d times" % run_debug()

# I should probably patch the actual assembler instead
def run_patched():
    regs['a'] = 1 # as of now the patch doesn't solve part 1
    regs['h'] = 0 # return
    regs['b'] = 81
    regs['c'] = regs['b']
    regs['b'] *= 100
    regs['b'] -= -100000
    regs['c'] = regs['b'] - -17000

    while True:
        regs['f'] = 1
        regs['d'] = 2
        regs['e'] = 2
        while True:
            if regs['b'] % regs['d'] == 0:
                regs['f'] = 0
            regs['d'] -= -1
            if regs['d'] != regs['b']:
                continue
            if regs['f'] == 0:
                regs['h'] -= -1
            if regs['b'] == regs['c']:
                return regs['h']
            regs['b'] -= -17
            break

print "Register h holds the value %d" % run_patched()
