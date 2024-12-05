#!/usr/bin/python3
from collections import defaultdict

class Rule(int):
    rulebook = defaultdict(set)

    def __init__(self, num):
        self.num = int(num)

    def __lt__(self, b):
        return b.num in self.rulebook[self.num]

def main():
    with open('input') as f:
        rules, updates = f.read().split('\n\n')

        rules = [[int(page) for page in rule] for rule in [rule.split('|') for rule in rules.split()]]
        for r in rules:
            Rule.rulebook[r[0]].add(r[1])

        updates = [[Rule(update) for update in updates] for updates in [update.split(',') for update in updates.split()]]

        print(sum([update[(len(update) - 1)//2] for update in updates if update == sorted(update)]))
        print(sum([sorted(update)[(len(update) - 1)//2] for update in updates if update != sorted(update)]))

if __name__ == "__main__":
    main()
