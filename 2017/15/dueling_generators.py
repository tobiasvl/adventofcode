a = 289
b = 629

judge = 0

for i in range(40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a & 65535 == b & 65535:
        judge += 1

print "The judge's first count is %d" % judge

judge = 0
pairs = 0

while pairs < 5000000:
    while True:
        a = (a * 16807) % 2147483647
        if a % 4 == 0:
            break
    while True:
        b = (b * 48271) % 2147483647
        if b % 8 == 0:
            break
    if (a & 65535) == (b & 65535):
        judge += 1
    pairs += 1

print "The judge's second count is %d" % judge
