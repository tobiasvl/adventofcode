from collections import deque

step = 349

buffer = [0]
position = 0

for i in xrange(1, 2018):
    position = (position + step) % len(buffer)
    buffer.insert(position+1, i)
    position += 1

print "The value following 2017 after 2017 insertions is %d" % buffer[buffer.index(2017) + 1]

# Well, that went well for part 1, but too slow for
# part 2. There are probably ways to figure this out
# without brute force, but brute force is surprisingly
# "fast" with a deque.

buffer = deque([0])

for i in xrange(1, 50000001):
    buffer.rotate(-step)
    buffer.append(i)

# Python 2's deque actually doesn't have index().
# Biggest reason to upgrade yet.
buffer = list(buffer)
print "The value following 0 after 50 000 000 insertions is %d" % buffer[buffer.index(0) + 1]
