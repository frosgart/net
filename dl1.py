import pexpect
import re

'''
TELNET mac-address query script for DLINK switches. 
Takes a list of addresses (or just one) and list of mac's (or just one)
then makes a telnet connection to the switches and return the command results. 
If the switch is NOT DLINK (has a different CLI commands) or just not responding to the telnet - it is ignored. 
'''

username = 'master'
password = 'kj[fyrf'

#ip_address = '10.0.255.235'
ip_address = input('Enter the ip-address of the switch:\n')
ip_list = ip_address.split(' ')

mac_list = input('Enter the mac addresses (space as delimiter):\n')
#mac_list = ('0C-80-63-A6-42-8B')
mac = mac_list.split(' ')

def telnet_connection(ip_address, macaddres):
    telnet = pexpect.spawn('telnet {}'.format(ip_address), timeout=2)
    telnet.expect([r'User[N-n]ame[:\s]+'])
    telnet.sendline('{}'.format(username))
    telnet.expect([r'Pass[W-w]ord[:\s]+'])
    telnet.sendline('{}'.format(password))
    telnet.expect('#')
    telnet.sendline('disable clipaging')
    telnet.expect('#')
    telnet.sendline('sh fdb mac {}'.format(macaddres))
    telnet.expect('#')
    telnet.close()
    output = telnet.before.decode('utf-8')
    return output

# for list of IP's and list of mac's
match = re.compile(r'[0-9A-Fa-f]{2}')
for ip in ip_list:
    for item in mac:
        try:
            macaddres = ':'.join(match.findall(item))
            result = telnet_connection(ip,macaddres)
            print('For ip {} and mac {} the result is: \n'.format(ip,macaddres))
            print(result)
        except pexpect.exceptions.TIMEOUT:
            print("Oops, timeout or it is not a dlink switch")
            continue







