import operator

instructions = []
regs = {}
operations = {
    'inc': lambda x, y: x + y,
    'dec': lambda x, y: x - y,
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y
}

with open('input.txt') as f:
    for line in f:
        element = line.strip().split()
        instructions.append({'register': element[0],
                             'operation': operations[element[1]],
                             'operand': int(element[2]),
                             'cond_reg': element[4],
                             'cond_check': operations[element[5]],
                             'cond_operand': int(element[6])})
        regs.update({element[0]: 0})

highest_value = 0

for i in instructions:
    if i['cond_check'](regs[i['cond_reg']], i['cond_operand']):
        regs[i['register']] = i['operation'](regs[i['register']], i['operand'])
        if regs[i['register']] > highest_value:
            highest_value = regs[i['register']]

high_reg = max(regs.iteritems(), key=operator.itemgetter(1))
print "%d is the highest value (in register %s)" % (high_reg[1], high_reg[0])
print "%d was the highest value during computation" % highest_value
