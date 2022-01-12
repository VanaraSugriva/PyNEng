#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
ip type:
1. ask user for ip address
2. ip type ident
3. print out for any type :
   'unicast' - if first byte in range 1-223
   'multicast' - if first byte in range 224-239
   'local broadcast' - if ip equal 255.255.255.255
   'unassigned' - if ip equal 0.0.0.0
   'unused' - if other cases
'''

ip = input('ip: ')

oct_1 = int(ip.split('.')[0])
if oct_1 in range(1, 223): print('unicast')
elif oct_1 in range(224, 239): print('multicast')
elif ip == '255.255.255.255': print('local broadcast')
elif ip == '0.0.0.0': print('unassigned')
else: print('unused')