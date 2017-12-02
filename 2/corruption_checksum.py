import itertools

with open("input.txt") as f:
    spreadsheet = [[int(x) for x in line.split()] for line in f]

checksum1 = sum([(max(row) - min(row)) for row in spreadsheet])
print "Checksum 1: %d" % checksum1

checksum2 = 0
for row in spreadsheet:
    result = 0
    for x, y in list(itertools.combinations(row, 2)):
        if x % y == 0:
            result = x / y
            break
        elif y % x == 0:
            result = y / x
            break
    checksum2 = checksum2 + result

print "Checksum 2: %d" % checksum2
