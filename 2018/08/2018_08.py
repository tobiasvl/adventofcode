import aocd

def parse(nodes=1):
    metasum = 0
    for n in range(nodes):
        children = tree.pop()
        meta = tree.pop()

        metasum += parse(children)

        for i in range(meta):
            metasum += tree.pop()

    return metasum

def parse2():
    metasum = 0
    children = tree.pop()
    meta = tree.pop()

    if children == 0:
        for i in range(meta):
            metasum += tree.pop()
    else:
        childvalues = dict()
        for i in range(children):
            childvalues[i+1] = parse2()
        for i in range(meta):
            try:
                metasum += childvalues[tree.pop()]
            except KeyError:
                pass

    return metasum

values = [int(n) for n in aocd.data.split()]

tree = values[::-1]
print parse()
tree = values[::-1]
print parse2()
