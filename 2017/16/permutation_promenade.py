with open('input.txt') as f:
    dance_moves = f.readline().strip().split(',')

programs = list('abcdefghijklmnop')


def dance(dancers):
    for move in dance_moves:
        if move[0] == 's':
            n = int(move[1:])
            dancers = dancers[-n:] + dancers[:-n]
        elif move[0] == 'x':
            a, b = map(int, move[1:].split('/'))
            dancers[a], dancers[b] = dancers[b], dancers[a]
        elif move[0] == 'p':
            a, b = map(dancers.index, move[1:].split('/'))
            dancers[a], dancers[b] = dancers[b], dancers[a]
    return dancers


print "After the dance, the order is %s" % ''.join(dance(programs[:]))

i = 0
while i < 1000000000:
    programs = dance(programs)
    i += 1
    if programs == list('abcdefghijklmnop'):
        # Cycle found
        i = 1000000000 - (1000000000 % i)

print "After a billion dances, the order is %s" % ''.join(programs)
