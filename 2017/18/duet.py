from collections import deque

# PART 1

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


sound = 0
recovered = 0
i = 0

while i >= 0 and i < len(instructions):
    instruction = instructions[i]['operation']
    operands = instructions[i]['operands']
    if instruction == 'snd':
        sound = get_value(operands[0])
    elif instruction == 'rcv':
        recovered_value = get_value(operands[0])
        if recovered_value != 0:
            recovered = sound
            print "The first recovered frequence is %d" % sound
            break
    elif instruction == 'jgz':
        if get_value(operands[0]) > 0:
            i += get_value(operands[1])
            continue
    elif instruction == 'set':
        regs[operands[0]] = get_value(operands[1])
    elif instruction == 'add':
        regs[operands[0]] += get_value(operands[1])
    elif instruction == 'mul':
        regs[operands[0]] *= get_value(operands[1])
    elif instruction == 'mod':
        regs[operands[0]] %= get_value(operands[1])
    i += 1

# PART 2

instructions = []
regs = [{}, {}]

with open('input.txt') as f:
    for line in f:
        element = line.strip().split()
        instructions.append({'operation': element[0],
                             'operands': tuple(element[1:])})
        try:
            int(element[1])
        except ValueError:
            regs[0].update({element[1]: 0})
            regs[1].update({element[1]: 0})
        regs[1]['p'] = 1


def get_value(p, x):
    try:
        return int(x)
    except ValueError:
        return regs[p][x]


queues = [deque(), deque()]
times_sent = [0, 0]
terminated = [False, False]
waiting = [False, False]
i = [0, 0]

# High cyclomatic complexity, not ideal
while True:
    if any(x == [True, True] for x in (waiting, terminated)):
        break
    for p in (0, 1):
        if terminated[p]:
            continue
        instruction = instructions[i[p]]['operation']
        operands = instructions[i[p]]['operands']
        if instruction == 'snd':
            queues[p ^ 1].appendleft(get_value(p, operands[0]))
            times_sent[p] += 1
        elif instruction == 'rcv':
            if len(queues[p]) == 0:
                waiting[p] = True
                continue
            else:
                waiting[p] = False
                regs[p][operands[0]] = queues[p].pop()
        elif instruction == 'jgz':
            if get_value(p, operands[0]) > 0:
                i[p] += get_value(p, operands[1])
                if i[p] < 0 or i[p] >= len(instructions):
                    terminated[p] = True
                continue
        elif instruction == 'set':
            regs[p][operands[0]] = get_value(p, operands[1])
        elif instruction == 'add':
            regs[p][operands[0]] += get_value(p, operands[1])
        elif instruction == 'mul':
            regs[p][operands[0]] *= get_value(p, operands[1])
        elif instruction == 'mod':
            regs[p][operands[0]] %= get_value(p, operands[1])
        i[p] += 1

print "Program 1 sent %d values" % times_sent[1]
