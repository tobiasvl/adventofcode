import hashlib

input = 'iwrupvqb'

counter = 0
hash_found = False

while True:
    md5 = hashlib.md5('%s%d' % (input, counter)).hexdigest()
    if md5.startswith('00000') and not hash_found:
        print "First AdventCoin at %d" % counter
        hash_found = True
    if md5.startswith('000000'):
        print "Second AdventCoin at %d" % counter
        break
    counter += 1
