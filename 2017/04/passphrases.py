import itertools

with open('input.txt') as f:
    passphrases = [line.strip().split() for line in f if line != '\n']

def contains_anagram(passphrase):
    for w1, w2 in itertools.combinations(passphrase, 2):
        if sorted(w1) == sorted(w2):
            return True
    return False


passphrases_without_repeats = 0
passphrases_without_anagrams = 0

for passphrase in passphrases:
    if len(passphrase) != len(set(passphrase)):
        continue
    passphrases_without_repeats += 1
    if contains_anagram(passphrase):
        continue
    passphrases_without_anagrams += 1

print "%s passphrases without duplicate words" % passphrases_without_repeats
print "%s passphrases without anagrams" % passphrases_without_anagrams
