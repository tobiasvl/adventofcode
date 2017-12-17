step = 349

buffer = [0]
position = 0

for i in range(1, 2018):
    position = (position + step) % len(buffer)
    buffer.insert(position+1, i)
    position += 1

print "The value following 2017 after 2017 insertions is %d" % buffer[buffer.index(2017) + 1]
