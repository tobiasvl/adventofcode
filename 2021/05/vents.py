#!/usr/bin/python3
def main():
    vents = []
    with open('input') as f:
        for line in f:
            line = line.strip('\n').split(' -> ')
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
