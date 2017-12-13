import re

with open('input.txt') as f:
    lines = f.readlines()
    layers = re.search('(\d*): (\d*)', lines[-1].strip())
    firewall = []
    for i in range(int(layers.group(1)) + 1):
        firewall.append([])
    for line in lines:
        layer = re.search('(\d*): (\d*)', line.strip())
        firewall[int(layer.group(1))] = [0, int(layer.group(2)), False]


def advance(layer):
    severity = 0
    try:
        if firewall[layer][0] == 0:
            severity += firewall[layer][1] * layer
    except IndexError:
        pass
    for layer in firewall:
        try:
            if layer[0] == layer[1] - 1 and layer[2] == False:
                layer[2] = True
            elif layer[0] == 0 and layer[2] == True:
                layer[2] = False
            if layer[2] == True:
                layer[0] -= 1
            else:
                layer[0] += 1
        except IndexError:
            pass
    return severity


severity = 0
for picosecond in range(len(firewall)):
    severity += advance(picosecond)
print "The severity of the trip without delay is %d" % severity
