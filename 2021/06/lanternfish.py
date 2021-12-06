#!/usr/bin/python3
def naive_breed(fish, days):
    for _ in range(0, days):
        new_fish = []
        for f in fish:
            if f > 0:
                new_fish.append(f - 1)
            else:
                new_fish.append(6)
                new_fish.append(8)
        fish = new_fish
    return len(fish)

def breed(fish, num_days):
    days = [0 for i in range(0, 9)]
    for f in fish:
        days[f] += 1

    for _ in range(0, num_days):
        new_days = [0 for i in range(0, 9)]
        for d in range(0, len(days)):
            if d == 0:
                new_days[8] += days[0]
                new_days[6] += days[0]
            else:
                new_days[d - 1] += days[d]
        days = new_days
    return sum(days)

def main():
    with open('input') as f:
        line = f.readline()
        fish = [int(fish) for fish in line.strip().split(',')]

    print(breed(fish, 80))
    print(breed(fish, 256))

if __name__ == "__main__":
    main()
