with open('input.txt') as f:
    components = [(int(x), int(y)) for x, y in [line.strip().split('/') for line in f]]

# Consolidate these methods into one
def build_strongest(path, components, pins):
    strongest_bridge = []
    for component in components:
        if pins in component:
            bridge = build_strongest(path + [component], [comp for comp in components if comp != component], component[0] if component[1] == pins else component[1])
            if sum(map(sum, bridge)) > sum(map(sum, strongest_bridge)):
                strongest_bridge = bridge
    if strongest_bridge == []:
        return path
    else:
        return strongest_bridge

def build_longest(path, components, pins):
    longest_bridge = []
    for component in components:
        if pins in component:
            bridge = build_longest(path + [component], [comp for comp in components if comp != component], component[0] if component[1] == pins else component[1])
            if len(bridge) > len(longest_bridge):
                longest_bridge = bridge
            elif len(bridge) == len(longest_bridge):
                if sum(map(sum, bridge)) > sum(map(sum, longest_bridge)):
                    longest_bridge = bridge
    if longest_bridge == []:
        return path
    else:
        return longest_bridge

part1 = build_strongest([], components, 0)
print "The strongest bridge has strength %d" % sum(map(sum, part1))

part2 = build_longest([], components, 0)
print "The longest bridge has strength %d" % sum(map(sum, part2))
