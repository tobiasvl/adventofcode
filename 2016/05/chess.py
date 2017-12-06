import hashlib

input = 'reyedfim'

index = 0
password = ''
password_length = 0
real_password = ['', '', '', '', '', '', '', '']
real_password_length = 0

while True:
    md5 = hashlib.md5('%s%d' % (input, index)).hexdigest()
    if md5.startswith('00000'):
        if password_length < 8:
            password += md5[5]
            password_length += 1
        if real_password_length < 8:
            try:
                if real_password[int(md5[5])] == '':
                    real_password[int(md5[5])] = md5[6]
                    real_password_length += 1
            except (ValueError, IndexError) as e:
                pass
    index += 1
    if password_length >= 8 and real_password_length >= 8:
        break

print "The password for door 1 is %s" % password
print "The password for door 2 is %s" % ("".join(real_password))
