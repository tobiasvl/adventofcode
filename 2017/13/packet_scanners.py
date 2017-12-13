import re

with open('input.txt') as f:
    lines = f.readlines()
    layers = re.search('(\d*): (\d*)', lines[-1].strip())
    firewall = []
    for i in range(int(layers.group(1)) + 1):
        firewall.append(None)
    for line in lines:
        layer = re.search('(\d*): (\d*)', line.strip())
        firewall[int(layer.group(1))] = int(layer.group(2))


def run(delay=0):
    # If the run is not delayed, return the severity of the run.
    # If the run is delayed, don't return the actual severity (for
    # optimizational reasons), but return False if the run is
    # successful (ie. has no severity) and True if it is unsuccessful
    # (ie. it has a severity).
    severity = 0
    for layer in range(len(firewall)):
        if firewall[layer] is not None:
            # Instead of the scanner bouncing up and down a layer of
            # length firewall[layer], we imagine it as a loop of length
            # 2 * firewall[layer] - 1. That way we can use modulo to
            # see when it's in position 0.
            if (delay + layer) % (2 * (firewall[layer] - 1)) == 0:
                # This is ugly but efficient
                if delay > 0:
                    return True
                severity += firewall[layer] * layer
    return severity


print "The severity of the trip without delay is %d" % run()

delay = 0
while True:
    if not run(delay):
        break
    delay += 1

print "The delay needed for a successful run is %d" % delay
