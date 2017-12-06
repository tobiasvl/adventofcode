import collections

with open("input.txt") as f:
    messages = [line.strip() for line in f if line != '\n']

decoded_messages = [''] * len(messages[0])
combined_message = ''
modified_message = ''

for message in messages:
    decoded_messages = map(lambda x: x[0] + x[1], zip(decoded_messages, message))

for decoded_message in decoded_messages:
    common_letters = collections.Counter(decoded_message).most_common()
    combined_message += common_letters[0][0]
    modified_message += common_letters[-1][0]

print "The error corrected message is %s" % combined_message
print "The modified error corrected message is %s" % modified_message
