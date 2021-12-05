#!/usr/bin/python3
def count_overlaps(vents):
    count = 0
    for y in range(len(vents)):
        for x in range(len(vents[y])):
            if vents[y][x] > 1:
                count += 1
    return count

def visualize(vents):
    for y in range(len(vents)):
        for x in range(len(vents[y])):
            if vents[y][x] == 0:
                print('.', end='')
            else:
                print(vents[y][x], end='')
        print()

def map_vents(coords, diagonals=False):
    width = max(max(coord[0][0], coord[1][0]) for coord in coords) + 1
    height = max(max(coord[0][1], coord[1][1]) for coord in coords) + 1
    vents = [[0 for i in range(0, height)] for i in range(0, width)]
    for (x1, y1), (x2, y2) in coords:
        if x1 != x2 and y1 != y2:
            if diagonals:
                # this is very ugly
                if x1 < x2:
                    x2 += 1
                elif x1 > x2:
                    x2 -= 1
                if y1 < y2:
                    y2 += 1
                elif y1 > y2:
                    y2 -= 1
                while x1 != x2 and y1 != y2:
                    vents[y1][x1] += 1
                    if x1 < x2:
                        x1 += 1
                    else:
                        x1 -= 1
                    if y1 < y2:
                        y1 += 1
                    else:
                        y1 -= 1
            continue
        for y in range(y1, y2 + (1 if y1 < y2 else -1), 1 if y1 < y2 else -1):
            for x in range(x1, x2 + (1 if x1 < x2 else -1), 1 if x1 < x2 else -1):
                vents[y][x] += 1
    return vents

def main():
    coords = []
    with open('input') as f:
        for line in f:
            line = line.strip('\n').split(' -> ')
            x1, y1 = tuple(int(coord) for coord in line[0].split(','))
            x2, y2 = tuple(int(coord) for coord in line[1].split(','))
            foo = coords.append([(x1, y1), (x2, y2)])
    
    vents = map_vents(coords)
    print(count_overlaps(vents))

    vents = map_vents(coords, True)
    print(count_overlaps(vents))

if __name__ == "__main__":
    main()
