#!/usr/bin/python3
def main():
    left, right = [], []
    with open('input') as f:
        for line in f:
            line = [l.strip() for l in line.split()]
            left.append(int(line[0]))
            right.append(int(line[1]))
    left.sort()
    right.sort()

    assert(len(left) == len(right))

    print(sum([abs(left[i] - right[i]) for i in range(len(left))]))

    from collections import defaultdict

    right_freq = defaultdict(int)
    for number in right:
        right_freq[number] += 1

    print(sum([num * right_freq[num] for num in left]))

if __name__ == "__main__":
    main()
