#!/usr/bin/python3
parens = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def parse_line(line):
    values = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
    }

    stack = []

    for char in line:
        if char in parens:
            stack.append(char)
        else:
            if parens[stack[-1]] == char:
                stack.pop()
            else:
                return values[char]
    return 0

def fix_line(line):
    values = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4
    }

    stack = []

    for char in line:
        if char in parens:
            stack.append(char)
        else:
            if parens[stack[-1]] == char:
                stack.pop()

    total = 0
    while len(stack) > 0:
        total *= 5
        total += values[parens[stack.pop()]]

    return total

def main():
    with open('input') as f:
        nav = [line.strip() for line in f]

    print(sum(parse_line(line) for line in nav))

    totals = []
    for line in nav:
        if parse_line(line) == 0:
            totals.append(fix_line(line))
    print(sorted(totals)[len(totals) // 2])

if __name__ == "__main__":
    main()
