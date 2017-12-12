with open('input.txt') as f:
    pipes = {int(x): eval('[' + y + ']') for x, y in [line.strip().split(' <-> ') for line in f if line != '\n']}

group = [] 

def find_pipes(pipe=0):
    if pipe in group:
        return []
    else:
        group.append(pipe)
    return [find_pipes(p) for p in pipes[pipe]] + [pipe]

find_pipes()
print "The group containing program 0 has %d programs" % len(group)

group = [] 
groups = set()

for p in pipes:
    find_pipes(p)
    groups.add(tuple(sorted(group)))
    group = []

print "There are %d groups in total" % len(groups)
