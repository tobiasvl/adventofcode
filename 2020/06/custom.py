#!/usr/bin/python3
def main():
    with open('input') as f:
        answers = [p.strip().split('\n') for p in f.read().split('\n\n')]

    print(sum(len(set(''.join(group))) for group in answers))

    count = 0
    for group in answers:
        checked = []
        for answer in group:
            for char in answer:
                if char not in checked and all(char in answer for answer in group):
                    count += 1
                    checked.append(char)
    print(count)

if __name__ == "__main__":
    main()
