#!/usr/bin/python3
def find_bag(bag, target_bag, bags):
    count = 0
    for (number, inner_bag) in bags[bag]:
        if target_bag == inner_bag:
            print(bag)
            return 1
        count += find_bag(inner_bag, target_bag, bags)
    return count > 0

def count_bags(bag, bags):
    count = 0
    for (number, inner_bag) in bags[bag]:
        count += number
        count += number * count_bags(inner_bag, bags)
    return count

def main():
    bags = {}
    with open('input') as f:
        for line in f:
            line = line.strip('.\n').split(' bags contain ')
            bag = line[0]
            _bags = line[1].split(', ')
            contents = []
            for content in _bags:
                content = content.split(' ')
                if content[0] != 'no':
                    contents.append((int(content[0]), ' '.join(content[1:-1])))
            bags[bag] = contents

    print(sum(find_bag(bag, "shiny gold", bags) for bag in bags))
    print(count_bags("shiny gold", bags))

if __name__ == "__main__":
    main()
