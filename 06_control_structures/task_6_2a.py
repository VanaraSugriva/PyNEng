#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
ip type with check ip:

1. ask user for ip

2. check inputed ip. Address is correct if it:
   - 4 integer splited by '.',
   - any byte in range from 0 to 255.
   If inputed ip is not correct: print:
   'ip is not correct.'

3. print out for any type :
      'unicast' - if first byte in range 1-223
      'multicast' - if first byte in range 224-239
      'local broadcast' - if ip equal 255.255.255.255
      'unassigned' - if ip equal 0.0.0.0
      'unused' - if other cases
'''

ip = input('ip: ')
octets = ip.split('.')

check_ip = len(octets) == 4
for oct in octets:
   check_ip = (check_ip and oct.isdigit() and int(oct) in range(256))
if check_ip == False:
   print('ip is not correct')

else:
   oct_1 = int(octets[0])
   if oct_1 in range(1, 223): print('unicast')
   elif oct_1 in range(224, 239): print('multicast')
   elif ip == '255.255.255.255': print('local broadcast')
   elif ip == '0.0.0.0': print('unassigned')
   else: print('unused')
