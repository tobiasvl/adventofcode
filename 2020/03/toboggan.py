#!/usr/bin/python3
def traverse(map, right=3, down=1):
    x, y, counter = 0, 0, 0
    while y < len(map):
        if map[y][x] == "#":
            counter += 1
        x = (x + right) % len(map[0])
        y += down
    return counter

def main():
    with open('input') as f:
        map = [line.strip() for line in f]

    print(traverse(map))
    print(traverse(map, 1, 1) * traverse(map, 3, 1) * traverse(map, 5, 1) * traverse(map, 7, 1) * traverse(map, 1, 2))

if __name__ == "__main__":
    main()
