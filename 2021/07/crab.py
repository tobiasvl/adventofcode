#!/usr/bin/python3
import statistics

def main():
    with open('input') as f:
        line = f.readline()
        crabs = [int(crab) for crab in line.strip().split(',')]

    median = int(statistics.median(crabs))
    print(sum(abs(c - median) for c in crabs))
    mean = int(statistics.mean(crabs))
    print(sum(sum(range(abs(mean - c) + 1)) for c in crabs))

if __name__ == "__main__":
    main()
