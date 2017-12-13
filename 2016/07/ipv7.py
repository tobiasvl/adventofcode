import re

with open('input.txt') as f:
    ips = [line.strip() for line in f if line != '\n']


def abba(ip):
    ip_main = re.sub('\[[a-z]*\]', '-', ip)
    ip_hypernet = re.sub('--', '-', re.sub('([^\]]*\[|\][^\[]*)', '-', ip))
    for quad in zip(ip_main, ip_main[1:], ip_main[2:], ip_main[3:]):
        if quad[0] == quad[3] and quad[1] == quad[2] and quad[0] != quad[1]:
            for quad in zip(ip_hypernet, ip_hypernet[1:], ip_hypernet[2:], ip_hypernet[3:]):
                if quad[0] == quad[3] and quad[1] == quad[2] and quad[0] != quad[1]:
                    return False
            return True


def aba(ip):
    ip_main = re.sub('\[[a-z]*\]', '-', ip)
    ip_hypernet = re.sub('--', '-', re.sub('([^\]]*\[|\][^\[]*)', '-', ip))
    for trio in zip(ip_main, ip_main[1:], ip_main[2:]):
        if trio[0] == trio[2] and trio[0] != trio[1]:
            for trio2 in zip(ip_hypernet, ip_hypernet[1:], ip_hypernet[2:]):
                if trio2[0] == trio2[2] and trio2[0] != trio2[1] and trio[0] == trio2[1] and trio[1] == trio2[0]:
                    return True
    return False


ssl_support = 0
tls_support = 0

for ip in ips:
    if abba(ip):
        tls_support += 1
    if aba(ip):
        ssl_support += 1

print "%d IPs support TLS" % tls_support
print "%d IPs support SSL" % ssl_support
