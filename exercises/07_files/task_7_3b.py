#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan_table = []
user_choice = input('vlan: ')
with open('CAM_table.txt') as f:
    for line in f:
        line = line.split()
        if line and line[0].isdigit and line[0] == user_choice:
            vlan, mac, _, intf = line
            vlan_table.append([vlan, mac, intf])
for vlan, mac, intf in sorted(vlan_table):
    print(f'{vlan:<12} {mac:20} {intf}')

