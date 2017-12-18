from collections import deque


def run(programs):
    def get_value(x, p=0):
        try:
            return int(x)
        except ValueError:
            return regs[p][x]

    instructions = []
    regs = []
    for _ in xrange(programs):
        regs.append({})

    with open('input.txt') as f:
        for line in f:
            element = line.strip().split()
            instructions.append({'operation': element[0],
                                 'operands': tuple(element[1:])})
            try:
                int(element[1])
            except ValueError:
                for i in xrange(programs):
                    regs[i].update({element[1]: 0})
                    regs[i]['p'] = i

    queues = [deque() for _ in xrange(programs)]
    times_sent = [0 for _ in xrange(programs)]
    terminated = [False for _ in xrange(programs)]
    waiting = [False for _ in xrange(programs)]
    i = [0 for _ in xrange(programs)]

    # High cyclomatic complexity, not ideal
    while True:
        terminate = True
        for x in zip(waiting, terminated):
            if not (x[0] or x[1]):
                terminate = False
        if terminate:
            return times_sent
        for p in xrange(programs):
            if terminated[p]:
                continue
            instruction = instructions[i[p]]['operation']
            operands = instructions[i[p]]['operands']
            if instruction == 'snd':
                if programs == 1:
                    queues[0].append(get_value(operands[0]))
                else:
                    queues[p - 1].appendleft(get_value(operands[0], p))
                    times_sent[p] += 1
            elif instruction == 'rcv':
                if programs == 1:
                    recovered_value = get_value(operands[0])
                    if recovered_value != 0:
                        recovered = queues[0].pop()
                        return recovered
                else:
                    if len(queues[p]) == 0:
                        waiting[p] = True
                        continue
                    else:
                        waiting[p] = False
                        regs[p][operands[0]] = queues[p].pop()
            elif instruction == 'jgz':
                if get_value(operands[0], p) > 0:
                    i[p] += get_value(operands[1], p)
                    if i[p] < 0 or i[p] >= len(instructions):
                        terminated[p] = True
                    continue
            elif instruction == 'set':
                regs[p][operands[0]] = get_value(operands[1], p)
            elif instruction == 'add':
                regs[p][operands[0]] += get_value(operands[1], p)
            elif instruction == 'mul':
                regs[p][operands[0]] *= get_value(operands[1], p)
            elif instruction == 'mod':
                regs[p][operands[0]] %= get_value(operands[1], p)
            i[p] += 1


print "The first recovered frequence is %d" % run(1)
print "Program 1 sent %d values" % run(2)[1]
print run(100)
