#!/usr/bin/python3
def count_valid(batch, verify_data=False):
    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]

    validate_fields = {
        'byr': lambda year: len(year) == 4 and int(year) >= 1920 and int(year) <= 2002,
        'iyr': lambda year: len(year) == 4 and int(year) >= 2010 and int(year) <= 2020,
        'eyr': lambda year: len(year) == 4 and int(year) >= 2020 and int(year) <= 2030,
        'hgt': lambda height: (int(height[:-2]) >= 150 and int(height[:-2]) <= 193 and height[-2:] == 'cm') or (int(height[:-2]) >= 59 and int(height[:-2]) <= 76 and height[-2:] == 'in'),
        'hcl': lambda color: color[0] == '#' and int(color[1:5], 16),
        'ecl': lambda color: color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda pid: len(pid) == 9 and int(pid),
        'cid': lambda cid: True,
    }

    counter = 0
    for passport in batch:
        if all(field in passport for field in required_fields):
            if verify_data:
                try:
                    if not all(validate_fields[field](value) for field, value in passport.items()):
                        continue
                except:
                    continue
            counter += 1
    return counter

def main():
    passports = []
    with open('input') as f:
        batch = [p.strip().replace('\n', ' ') for p in f.read().split('\n\n')]
        for line in batch:
            passport = {}
            for pair in line.split(' '):
                key, value = pair.split(':')
                passport[key] = value
            passports.append(passport)

    print(count_valid(passports))
    print(count_valid(passports, verify_data=True))

if __name__ == "__main__":
    main()
