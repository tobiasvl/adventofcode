#import aocd
import re
import collections

with open('input.txt') as f:
    input_lines = f.readlines()

input_lines = sorted(input_lines)

events = []
guards = {}

for line in input_lines:
    record = re.match(r"\[1518-\d\d-(?P<day>\d\d) (?P<hour>\d\d):(?P<minute>\d\d)\] (?P<event>.*)$", line).groupdict()
    record.update({k: int(v) for k, v in record.iteritems() if k != 'event'})
    try:
        current_guard = int(re.match(r"Guard #(\d+)", record['event']).groups(0)[0])
        if not current_guard in guards:
            guards[current_guard] = [0, collections.defaultdict(lambda: 0)]
    except AttributeError:
        if re.match(r"falls asleep", record['event']):
            sleep_start = record['minute']
        elif re.match(r"wakes up", record['event']):
            guards[current_guard][0] += record['minute'] - sleep_start
            for i in range(sleep_start, record['minute']):
                guards[current_guard][1][i] += 1

max_sleep = {'total_sleep': 0}
max_overall = {'length': 0}

for guard, sleep in guards.iteritems():
    if sleep[0] > max_sleep['total_sleep']:
        max_sleep = {'guard': guard, 'total_sleep': sleep[0], 'minute': 0, 'length': 0}
        for k, v in sleep[1].iteritems():
            if v > max_sleep['length']:
                max_sleep['minute'] = k
                max_sleep['length'] = v
    for k, v in sleep[1].iteritems():
        if v > max_overall['length']:
            max_overall = {'guard': guard, 'minute': k, 'length': v}

print max_sleep['guard'] * max_sleep['minute']
print max_overall['guard'] * max_overall['minute']
