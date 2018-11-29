
blacklist = []

with open("input.txt") as f:
    for line in f:
        blacklist.append(tuple(int(ip.strip()) for ip in line.split("-")))

#blacklist = [(5,8,),(0,2,),(4,7,)]

blacklist = sorted(blacklist, key=lambda x: x[0])

def find_allowed():
    lowest = blacklist[0][0]
    highest = blacklist[0][1]
    for x in blacklist:
        lo = x[0]
        hi = x[1]
        if lo > highest + 1:
            yield highest + 1
        if hi > highest:
            highest = hi

for ip in find_allowed():
    print "The first open IP: %d" % ip
    break

print "The number of open IPs: %d" % len([i for i in find_allowed()])
