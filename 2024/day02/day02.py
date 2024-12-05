#!/usr/bin/python3
def judge_safety(report):
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False

    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if diff > 0 and diff < 4:
            pass
        else:
            return False

    return True

def main():
    with open('input') as f:
        lines = [line.strip() for line in f]
        reports = [level.split() for level in lines]
        reports = [[int(level) for level in report] for report in reports]

    print(sum([judge_safety(report) for report in reports]))

    dampened_safe_reports = 0

    for report in reports:
        if judge_safety(report):
            dampened_safe_reports += 1
        else:
            for i in range(len(report)):
                report_dampened = report[::]
                report_dampened.pop(i)
                if judge_safety(report_dampened):
                    dampened_safe_reports += 1
                    break
    print(dampened_safe_reports)

if __name__ == "__main__":
    main()
