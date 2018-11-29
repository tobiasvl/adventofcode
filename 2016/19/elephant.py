def steal_gifts(elves):
    ring = [1] * elves
    elf = 0
    while ring[elf] != elves:
        next_elf = (elf + 1) % elves
        if ring[elf] > 0:
            while True:
                if ring[next_elf] == 0:
                    next_elf = (next_elf + 1) % elves
                else:
                    break
            ring[elf] += ring[next_elf]
            ring[next_elf] = 0
        elf = next_elf
    return elf + 1

print steal_gifts(3005290)
