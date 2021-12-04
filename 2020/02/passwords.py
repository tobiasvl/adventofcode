#!/usr/bin/python3
import re

def count_policy(passwords):
    num_passwords = 0
    for (password, letter, min, max) in passwords:
        counter = 0
        for character in password:
            if character == letter:
                counter += 1
        if counter >= min and counter <= max:
            num_passwords += 1
    return num_passwords

def position_policy(passwords):
    num_passwords = 0
    for (password, letter, pos1, pos2) in passwords:
        if (password[pos1 - 1] == letter) + (password[pos2 - 1] == letter) == 1:
            num_passwords += 1
    return num_passwords

def main():
    passwords = []
    with open('input') as f:
        for line in f:
            match = re.match(r"(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<password>\w+)", line)
            passwords.append((match.groupdict()['password'], match.groupdict()['letter'], int(match.groupdict()['min']), int(match.groupdict()['max'])))


    print(count_policy(passwords))
    print(position_policy(passwords))

if __name__ == "__main__":
    main()
