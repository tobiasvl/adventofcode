#!/usr/bin/python3
import re
def main():
    with open('input') as f:
        m = re.findall('mul\((\d+),(\d+)\)', f.read().strip())
        print(sum([int(mul[0]) * int(mul[1]) for mul in m]))

    with open('input') as f:
        final = 0
        for enabled_section in f.read().split('do()'):
            # gung ho assumption: do() and don't() alternate cleanly
            enabled_section = enabled_section.split('don\'t()')[0]
            m = re.findall('mul\((\d+),(\d+)\)', enabled_section)
            final += sum([int(mul[0]) * int(mul[1]) for mul in m])
        print(final)

if __name__ == "__main__":
    main()
