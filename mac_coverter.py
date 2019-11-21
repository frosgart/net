import re

macs = ['12cd:ffed:ad78', 'FE-AD-20-78-11-EF', 'EFEE123456FE', 'abcd.ffee.1234', '11:78:DD:AB:EF:F8', 'some other shit']

six_group_mac = re.compile(r'[0-9A-Fa-f]{2}(?:[:-][0-9A-Fa-f]{2}){5}')
four_group_mac = re.compile(r'[0-9A-Fa-f]{4}(?:[:.][0-9A-Fa-f]{4}){2}')
one_group_mac = re.compile(r'[0-9A-Fa-f]{12}')

for item in macs:
    if six_group_mac.findall(item):
        result = six_group_mac.findall(item)
        print(result)
    elif four_group_mac.findall(item):
        result2 = four_group_mac.findall(item)
        print(result2)
    elif one_group_mac.findall(item):
        result3 = one_group_mac.findall(item)
        print(result3)
    else:
        print(item)
