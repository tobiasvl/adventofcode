import hashlib
import re

def find(input, stretch=False):
    index = 0
    three = re.compile(r'(\w)\1{2}')
    five = re.compile(r'(\w)\1{4}')
    potential_keys = dict()
    keys = set()
    while True:
        md5 = hashlib.md5('%s%d' % (input, index)).hexdigest()
        if stretch:
            for i in range(2016):
                md5 = hashlib.md5(md5).hexdigest()
        result = re.search(five, md5)
        if result:
            for k, v in potential_keys.iteritems():
                if index - k <= 1000 and v == result.group(1):
                    keys.add(k)
                    if len(keys) == 100:
                        return sorted(list(keys))[63]
        result = re.search(three, md5)
        if result:
            potential_keys[index] = result.group(1)
        index += 1

print "This index produces the 64th key: %s" % find('ngcjuoqr')
print "With stretching, this index produces the 64th key: %s" % find('ngcjuoqr', True)
