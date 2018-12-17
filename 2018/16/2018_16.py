import re

samples, program = open('input.txt').read().strip().split('\n\n\n\n')

samples = [map(lambda x: tuple(map(int, re.search(r'(\d+),? (\d+),? (\d+),? (\d+)', x).groups())), s) for s in [s.split('\n') for s in samples.split('\n\n')]]
program = [map(int, s.split(' ')) for s in program.split('\n')]

opcodes = {
    'addr': lambda a, b, regs: regs[a] + regs[b],
    'addi': lambda a, b, regs: regs[a] + b,
    'mulr': lambda a, b, regs: regs[a] * regs[b],
    'muli': lambda a, b, regs: regs[a] * b,
    'banr': lambda a, b, regs: regs[a] & regs[b],
    'bani': lambda a, b, regs: regs[a] & b,
    'borr': lambda a, b, regs: regs[a] | regs[b],
    'bori': lambda a, b, regs: regs[a] | b,
    'setr': lambda a, b, regs: regs[a],
    'seti': lambda a, b, regs: a,
    'gtir': lambda a, b, regs: int(a > regs[b]),
    'gtri': lambda a, b, regs: int(regs[a] > b),
    'gtrr': lambda a, b, regs: int(regs[a] > regs[b]),
    'eqir': lambda a, b, regs: int(a == regs[b]),
    'eqri': lambda a, b, regs: int(regs[a] == b),
    'eqrr': lambda a, b, regs: int(regs[a] == regs[b]),
}

matching_samples = {}
possible_matches = [set(op for op in opcodes) for _ in range(16)]
total = 0

for before, operation, after in samples:
    op, a, b, c = operation
    matching_samples[(before, operation, after)] = set()
    matches = set()
    for instruction, opcode in opcodes.iteritems():
        registers = list(before)
        registers[c] = opcode(a, b, before)
        if registers == list(after):
            matching_samples[(before, operation, after)].add(instruction)
            matches.add(instruction)
    possible_matches[op] &= matches
    if len(matching_samples[(before, operation, after)]) >= 3:
        total += 1

print total

disambiguated = set()

while any(len(s) > 1 for s in possible_matches):
    for s in possible_matches:
        if len(s) == 1:
            disambiguated |= s
        else:
            s -= disambiguated

possible_matches = [s.pop() for s in possible_matches]
registers = [0, 0, 0, 0]

for op, a, b, c in program:
    registers[c] = opcodes[possible_matches[op]](a, b, registers)

print registers[0]
