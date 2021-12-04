#!/usr/bin/python3
def check_win(board, draw):
    for board_view in [board, list(map(list, zip(*board)))]:
        for line in board_view:
            skip = False
            for num in line:
                if not num[1]:
                    skip = True
                    break
            if skip:
                continue
            return (draw, board)
    return False

def play(boards, draws):
    for draw in draws:
        for board in boards:
            for line in board:
                for num in line:
                    if num[0] == draw:
                        num[1] = True
                        win = check_win(board, draw)
                        if win:
                            return win

def find_total(board):
    total = 0
    for line in board:
        for num in line:
            if not num[1]:
                total += num[0]
    return total

def win(boards, draws):
    win = play(boards, draws)
    return find_total(win[1]) * win[0]

def lose(boards, draws):
    win = None
    while True:
        temp_win = play(boards, draws)
        if not temp_win:
            break
        boards.remove(temp_win[1])
        win = temp_win
    return find_total(win[1]) * win[0]

def parse_boards(lines):
    boards = []
    board = None
    for i in range(1, len(lines)):
        if lines[i] == '':
            board = []
            boards.append(board)
            continue
        board.append([[int(num), False] for num in lines[i].split()])
    return boards

def main():
    lines = []
    with open('input') as f:
        lines = [line.strip() for line in f]
    draws = [int(num) for num in lines[0].split(',')]

    print(win(parse_boards(lines), draws))
    print(lose(parse_boards(lines), draws))

if __name__ == "__main__":
    main()
