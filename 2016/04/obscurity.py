import collections
import re

with open('input.txt') as f:
    rooms = [re.match('^(?P<name>[a-z\-]*)(?P<id>[0-9]*)\[(?P<checksum>[a-z]*)\]$',
                      line.strip()).groupdict()
             for line in f if line != '\n']

sector_ids = 0

for room in rooms:
    common_letters = collections.Counter(room['name'].replace('-', '')).most_common()
    common_letters = sorted(common_letters, key=lambda x: (-x[1], x[0]))
    common_letters = common_letters[:5]
    common_letters = ''.join('%s' % q[0] for q in common_letters)
    if room['checksum'] == common_letters:
        room_id = int(room['id'])
        sector_ids += room_id
        decrypted_name = ''
        for letter in room['name']:
            if letter == '-':
                decrypted_name += ' '
                continue
            letter_number = ord(letter) - 97
            letter_number = (letter_number + room_id) % 26
            decrypted_name += chr(letter_number + 97)
        if 'pole' in decrypted_name:
            north_pole_room = room['id']

print "The sum of the real sector IDs is %s" % sector_ids
print "The North Pole objects are stored in sector ID %s" % north_pole_room
