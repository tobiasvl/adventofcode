from collections import defaultdict

# { state: ( (input=1: output, direction, new_state),
#            (input=1: output, direction, new_state) ) }
states = {
    'a': ((1, 1, 'b'), (0, 1, 'c')),
    'b': ((0, -1, 'a'), (0, 1, 'd')),
    'c': ((1, 1, 'd'), (1, 1, 'a')),
    'd': ((1, -1, 'e'), (0, -1, 'd')),
    'e': ((1, 1, 'f'), (1, -1, 'b')),
    'f': ((1, 1, 'a'), (1, 1, 'e'))
}

state = 'a'
steps = 12399302

tape = defaultdict(lambda: 0)
cursor = 0

for _ in range(steps):
    output, direction, state = states[state][tape[cursor]]
    tape[cursor] = output
    cursor += direction

print "The checksum is %d" % sum(tape.values())
