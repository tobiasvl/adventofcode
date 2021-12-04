#!/usr/bin/python3
def seat_id(boarding_pass):
    boarding_pass = boarding_pass.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    boarding_pass = int(boarding_pass, 2)
    row = boarding_pass >> 3
    seat = boarding_pass & 7
    return (row * 8) + seat

def main():
    passes = []
    with open('input') as f:
        passes = [line.strip() for line in f]

    seat_ids = sorted([seat_id(boarding_pass) for boarding_pass in passes])
    highest_id = max(seat_ids)
    print(highest_id)

    lowest_id = min(seat_ids)
    for seat in range(lowest_id, highest_id):
        if seat not in seat_ids:
            print(seat)

if __name__ == "__main__":
    main()
