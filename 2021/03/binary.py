#!/usr/bin/python3
def diagnose(report):
    gamma = ""
    epsilon = ""
    for bit in range(len(report[0])):
        if sum([int(number[bit]) for number in report]) > len(report) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma, 2) * int(epsilon, 2)

def filter_report(report, step=0, oxygen=True):
    if step >= len(report[0]) or len(report) == 1:
        assert(len(report) == 1)
        return report[0]
    filtered_sum = 0
    for i in report:
        filtered_sum += int(i[step])
    if filtered_sum >= len(report) / 2.0:
        criterion = oxygen
    else:
        criterion = not oxygen
    filtered_report = []
    for i in report:
        if int(i[step]) == int(criterion):
            filtered_report.append(i)
    return filter_report(filtered_report, step + 1, oxygen)

def diagnose2(report):
    oxygen_rating = filter_report(report, oxygen=True)
    co2_rating = filter_report(report, oxygen=False)
    return int(oxygen_rating, 2) * int(filter_report(report, oxygen=False), 2)

def main():
    with open('input') as f:
        report = [number.strip() for number in f]
    print(diagnose(report))
    print(diagnose2(report))

if __name__ == "__main__":
    main()
