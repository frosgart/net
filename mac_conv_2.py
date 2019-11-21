import re
switch = '10.10.1.1'

#mac = '12cd:ffed:ad78'
macs = ['12cd:ffed:ad78', 'FE-AD-20-78-11-EF', 'EFEE123456FE', 'abcd.ffee.1234', '11:78:DD:AB:EF:F8', 'FF-FF-FF-FE-EE-FF']
match = re.compile(r'[0-9A-Fa-f]{2}')

for item in macs:
    out = ':'.join(match.findall(item))
    print('telnet to {} and issue - show fdb mac {}'.format(switch,out))

