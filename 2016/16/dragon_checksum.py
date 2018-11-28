state = "00111101111101000"

def checksum(data, length):
    while len(data) < length:
        b = data[::-1]
        b = b.replace("0", "2").replace("1", "0").replace("2", "1")
        data = data + "0" + b

    data = data[:length]

    checksum = data

    while len(checksum) % 2 == 0:
        pairs = map(''.join, zip(*[iter(checksum)]*2))
        checksum = ""
        for pair in pairs:
            if pair[0] == pair[1]:
                checksum += "1"
            else:
                checksum += "0"
    return checksum

print "Checksum for first disk: %s" % checksum(state, 272)
print "Checksum for second disk: %s" % checksum(state, 35651584)
