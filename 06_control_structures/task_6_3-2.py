#/usr/bin/env python
# -*- coding: utf-8 -*-

'''
trunk ports config generator like access ports config generator
there can be a lot of vlans and actions to do with its in trunk 

so in according with any port there is list
1st item (0 element) is action with vlans:
	add - for add vlans (switchport trunk allowed vlan add 10,20)
	del - for delete vlans from allowed list (switchport trunk allowed vlan remove 17)
	only - for only the specified vlans should remain (switchport trunk allowed vlan 11,30)

for ports 0/1, 0/2, 0/4 task:
- generate a configuration based on the trunk_template template
- taking into account keywords: add, del, only

script ignore other ports number if its are there.

'''

access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}
trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }

for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

