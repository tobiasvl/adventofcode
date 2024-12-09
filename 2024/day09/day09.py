#!/usr/bin/python3
from collections import defaultdict
from itertools import permutations, combinations

def main():
    with open('input') as f:
        string = f.readline().strip()

    disk_map = []
    file = False
    i = 0
    for length in string:
        length = int(length)
        file = not file
        for _ in range(length):
            if file:
                disk_map.append(str(i))
            else:
                disk_map.append('.')
        if file:
            i += 1

    i = 0
    j = len(disk_map) - 1
    while True:
        if i == j:
            break
        if (disk_map[i] == '.' and disk_map[j] == '.'):
            j -= 1
        if disk_map[i] != '.':
            i += 1
            continue
        if disk_map[j] != '.':
            disk_map[i] = disk_map[j]
            disk_map[j] = '.'
            i += 1
            j -= 1

    checksum = 0
    for i in range(len(disk_map)):
        if disk_map[i] != '.':
            checksum += i * int(disk_map[i])
    print(checksum)

    disk_map = []
    file = False
    i = 0
    for length in string:
        length = int(length)
        file = not file
        if file:
            disk_map.append([str(i), length])
            i += 1
        else:
            disk_map.append(['.', length])

    i = 0
    j = len(disk_map) - 1
    while True:
        if j == 0:
            break
        if i >= len(disk_map) or i == j or (disk_map[i][0] == '.' and disk_map[j][0] == '.'):
            j -= 1
            i = 0
            continue
        if disk_map[i][0] != '.' or disk_map[i][1] == 0:
            i += 1
            continue
        if disk_map[j][0] != '.':
            if disk_map[i][1] == disk_map[j][1]:
                disk_map[i][0] = disk_map[j][0]
                disk_map[j][0] = '.'
                j -= 1
                i = 0
            elif disk_map[i][1] > disk_map[j][1]:
                length1 = disk_map[i][1]
                length2 = disk_map[j][1]
                disk_map[i] = disk_map[j][:]
                disk_map[j][0] = '.'
                disk_map.insert(i + 1, ['.', length1 - length2])
                i = 0
            else:
                i += 1

    checksum = 0
    i = 0
    for obj in disk_map:
        for _ in range(int(obj[1])):
            if obj[0] != '.' and obj[1] > 0:
                checksum += i * int(obj[0])
            if obj[1] > 0:
                i += 1
    print(checksum)


if __name__ == "__main__":
    main()
