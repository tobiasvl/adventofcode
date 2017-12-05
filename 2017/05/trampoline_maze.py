def jump(strange=False):
    with open('input.txt') as f:
        maze = [int(line.strip()) for line in f if line != '\n']
    try:
        current_instruction = 0
        step = 0
        while True:
            old_instruction = current_instruction
            current_instruction += maze[current_instruction]
            if strange and current_instruction - old_instruction >= 3:
                maze[old_instruction] -= 1
            else:
                maze[old_instruction] += 1
            step += 1
    except IndexError:
        return step


print "%d steps" % jump()
print "%d steps with strange jumps" % jump(strange=True)
