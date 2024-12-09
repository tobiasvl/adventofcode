#!/usr/bin/python3

def calibrate(answer, total, tail, concatenate=False):
    #print('answer: %d, total: %d, tail: %s' % (answer, total, tail))
    if answer < total:
        return False
    if not tail:
        return answer == total
    return calibrate(answer, total + tail[0], tail[1:], concatenate) or calibrate(answer, total * tail[0], tail[1:], concatenate) or (concatenate and calibrate(answer, int('%d%d' % (total, tail[0])), tail[1:], concatenate))

def main():
    with open('input') as f:
        calibrations = [line.split(': ') for line in f.readlines()]
        calibrations = {int(line[0]): [int(num) for num in line[1].split()] for line in calibrations}

        print(sum([calibration for calibration in calibrations.keys() if calibrate(calibration, 0, calibrations[calibration], False)]))
        print(sum([calibration for calibration in calibrations.keys() if calibrate(calibration, 0, calibrations[calibration], True)]))

if __name__ == "__main__":
    main()
