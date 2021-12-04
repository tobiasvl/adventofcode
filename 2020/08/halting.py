#!/usr/bin/python3
def debug(code):
    for pc in range(0, len(code)):
        operation, argument = code[pc]
        if operation == 'nop':
            code[pc][0] = 'jmp'
        elif operation == 'jmp':
            code[pc][0] = 'nop'
        return_value = execute(code, halt=True, debug=True)
        if return_value:
            return return_value
        else:
            code[pc][0] = operation

def execute(code, halt=False, debug=False):
    accumulator = 0
    pc = 0
    executed = set()

    while True:
        if halt:
            if pc in executed:
                if debug:
                    return False
                break
            executed.add(pc)

        if pc == len(code):
            break

        operation, argument = code[pc]

        if operation == 'acc':
            accumulator += int(argument)
            pc += 1
        elif operation == 'jmp':
            pc += int(argument)
        else:
            pc += 1

    return accumulator

def main():
    with open('input') as f:
        code = [line.strip().split(' ') for line in f]

    print(execute(code, halt=True))
    print(debug(code))

if __name__ == "__main__":
    main()
