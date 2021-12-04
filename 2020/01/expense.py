#!/usr/bin/python3
from itertools import combinations
from functools import reduce

def fix(expenses, number):
    for numbers in combinations(expenses, number):
        if sum(numbers) == 2020:
            return reduce((lambda x, y: x * y), numbers)

def main():
    expenses = []
    with open('input') as f:
        expenses = [int(line.strip()) for line in f]

    print(fix(expenses, 2))
    print(fix(expenses, 3))

if __name__ == "__main__":
    main()
