import re
import collections

programs = {}
with open('input.txt') as f:
    for line in f:
        if line != '\n':
            program = re.match('^(?P<name>[a-z]*) \((?P<weight>[0-9]*)\)( -> (?P<children>[a-z, ]*))?$',
                               line.strip()).groupdict()
            if program['children']:
                program['children'] = program['children'].split(', ')
            program['weight'] = int(program['weight'])
            programs.update({program['name']: program})

for k, v in programs.iteritems():
    found = False
    for k2, v2 in programs.iteritems():
        if v2['children'] and k in v2['children']:
            found = True
            break
    if not found:
        root = k


def find_weight(node):
    if programs[node]['children'] is None:
        return node, programs[node]['weight']
    child_weights = []
    for child in programs[node]['children']:
        child_weights.append(find_weight(child))
    common_weights = collections.Counter(child[1] for child in child_weights).most_common(2)
    if not len(common_weights) == 1:
        wrong_weight = common_weights[1][0]
        weight_diff = wrong_weight - common_weights[0][0]
        for child in child_weights:
            if child[1] == wrong_weight:
                raise Warning, "%s should weigh %d" % (child[0], programs[child[0]]['weight'] - weight_diff)
    else:
        return node, programs[node]['weight'] + sum([c[1] for c in child_weights])


print "The bottom program is %s" % root
try:
    print "The tree is in balance and weighs %d" % find_weight(root)[1]
except Warning as e:
    print e
