#!/usr/bin/python3
def dive(moves, aiming=False):
    x, y, aim = 0, 0, 0
    movement = {
        'forward': lambda x, y, aim, steps: (x + steps, y + (aim * steps), aim) if aiming else (x + steps, y, aim),
        'backward': lambda x, y, aim, steps: (x - steps, y, aim),
        'down': lambda x, y, aim, steps: (x, y, aim + steps) if aiming else (x, y + steps, aim),
        'up': lambda x, y, aim, steps: (x, y, aim - steps) if aiming else (x, y - steps, aim),
    }
    for (direction, steps) in moves:
        (x, y, aim) = movement[direction](x, y, aim, steps)
    return x * y

def main():
    with open('input') as f:
        moves = [(direction, int(steps)) for direction, steps in (tuple(instruction.strip().split(" ")) for instruction in f)]
    print(dive(moves))
    print(dive(moves, aiming=True))

if __name__ == "__main__":
    main()
