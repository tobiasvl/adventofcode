import re

sample_discs = [{"id": 1, "size": 5, "position": 4}, {"id": 2, "size": 2, "position": 1}]
discs = []
with open("input.txt", "r") as f:
    for line in f:
        discs.append({k: int(v) for k, v in re.match(r"Disc #(?P<id>\d+) has (?P<size>\d+) positions; at time=0, it is at position (?P<position>\d+).", line).groupdict().iteritems()})

def simulate():
    time = 0
    while True:
        if all(((time + disc["position"] + disc["id"]) % disc["size"]) == 0 for disc in discs):
            return time
        time += 1


print "The first time you can push the button is %d" % simulate()
discs.append({"id": 7, "size": 11, "position": 0})
print "With the extra disc, you can first push at %d" % simulate()
