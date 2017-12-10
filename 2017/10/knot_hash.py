from itertools import cycle, islice
from collections import deque

input = '183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88'

def knot(rope, input, pos, skip):
    for l in input:
        if l > len(rope):
            continue

        # This is so dumb
        rope = deque(rope)
        rope.rotate(-pos)
        rope = list(rope)
        rope = rope[:l][::-1] + rope[l:]
        rope = deque(rope)
        rope.rotate(pos)

        pos += l + skip
        skip += 1
    return list(rope), pos, skip


rope = range(256)

knotted_rope, _, _ = knot(rope, eval('[' + input + ']'), 0, 0)
print "The product of the first two numbers is %d" % (knotted_rope[0] * knotted_rope[1])

input = [ord(i) for i in input]
input = input + [17, 31, 73, 47, 23]

pos = 0
skip = 0

for i in range(64):
    rope, pos, skip = knot(rope, input, pos, skip)

dense = [reduce(lambda x, y: x ^ y, rope[i:i + 16])
         for i in xrange(0, len(rope), 16)]

hex_hash = ''
for i in dense:
    hex_hash += "%02x" % i
print "The Knot Hash is %s" % hex_hash
