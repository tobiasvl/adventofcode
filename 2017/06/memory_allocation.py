with open('input.txt') as f:
    banks = f.readline()
    banks = [int(bank.strip()) for bank in banks.split('\t')]

seen = {}
cycles = 0

while True:
    bank = banks.index(max(banks))
    blocks = banks[bank]
    banks[bank] = 0
    while blocks > 0:
        bank += 1
        blocks -= 1
        banks[bank % len(banks)] += 1
    cycles += 1
    # Naive hashing, about as fast as using hash(tuple(banks))
    if str(banks) in seen:
        break
    else:
        seen[str(banks)] = cycles

print "%d cycles first time entering loop" % cycles
print "%d cycles in loop" % (cycles - seen[str(banks)])
