#!/usr/bin/python3
import itertools

def main():
    with open('input') as f:
        entries = {}
        for line in f:
            foo, bar = [foo for foo in line.strip().split(' | ')]
            entries[tuple([''.join(sorted(pattern)) for pattern in foo.split(' ')])] = [''.join(sorted(value)) for value in bar.split(' ')]

    count = 0
    for _, v in entries.items():
        for value in v:
            if len(value) in [2, 3, 4, 7]:
                count += 1
    print(count)

    digits = [
        (1, 2, 3, 5, 6, 7),
        (3, 6),
        (1, 3, 4, 5, 7),
        (1, 3, 4, 6, 7),
        (2, 3, 4, 6),
        (1, 2, 4, 6, 7),
        (1, 2, 4, 5, 6, 7),
        (1, 3, 6),
        (1, 2, 3, 4, 5, 6, 7),
        (1, 2, 3, 4, 6, 7)
    ]

    # Map each possible configuration of A-F segments into actual segmented numbers, regardless of consistency
    # Store them in a dict where the key is the configurations of the unique segmented numbers (1, 4 and 7; 8 is always the same)
    maps = {}
    for combo in [{k: v for k, v in zip(each_permutation, 'abcdefg')} for each_permutation in itertools.permutations([1,2,3,4,5,6,7])]:
        key = []
        mapped_digits = []
        for digit in digits:
            mapped_digit = ''.join(sorted(combo[segment] for segment in digit))
            mapped_digits.append(mapped_digit)
            if len(digit) in [2, 3, 4]:
                key.append(mapped_digit)
        try:
            maps[tuple(sorted(key))].append(mapped_digits)
        except:
            maps[tuple(sorted(key))] = [mapped_digits]

    # Go through all patterns, look up numbers 1, 4 and 7 in the dict above and get all the digits, check if they match
    full_count = 0
    for patterns, values in entries.items():
        key = []
        for p in patterns:
            if len(p) in [2, 3, 4]:
                key.append(p)
        key = tuple(sorted(key))
        mapped_digits = maps[key]
        for mapped in mapped_digits:
            if set(mapped) == set(patterns):
                count = ''
                for value in values:
                    for i in range(10):
                        if mapped[i] == value:
                            count += str(i)
                            break
                full_count += int(count)
    print(full_count)

if __name__ == "__main__":
    main()
