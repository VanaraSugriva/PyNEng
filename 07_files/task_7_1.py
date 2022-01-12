#!/usr/bin/env python
# # -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
output_template = '\n{:24} {}' * 6
with open('C:/git/repo/vs/07_files/ospf.txt') as src:
    for line in src:
        if line:
            proto, pref, ad_metr, next_hop, _, upd, intf = line.replace(',','').replace('[','').replace(']','').split()
            print(output_template.format(
                'Protocol:', 'OSPF',
                'Pref:', pref,
                'AD/Metr:', ad_metr,
                'Next-Hop:', next_hop,
                'Last Update:', upd,
                'Interface:', intf,
            ))