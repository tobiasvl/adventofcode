#!/usr/bin/python3
def scan(depths, window_size=1, debug=False):
    counter = 0
    for i in range(len(depths) - window_size + 1):
        depth = sum(depths[i: i + window_size])
        if debug:
            print(depth, end='')
        if i > 0:
            if depth > last_depth:
                counter += 1
                if debug:
                    print(" (increased)", end='')
        last_depth = depth
        if debug:
            print()
    return counter

def main():
    debug = False
    depths = []
    with open('input') as f:
        depths = [int(freq.strip()) for freq in f]
    print(scan(depths, debug=debug))
    print(scan(depths, 3, debug=debug))

if __name__ == "__main__":
    main()
