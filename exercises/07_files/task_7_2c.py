#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from sys import argv
ignore = ['duplex', 'alias', 'Current configuration']

with open(argv[1]) as src, open(argv[2], 'w') as dst:
    for line in src:
        words = line.split()
        if not line.startswith('!') and not set(words) & set(ignore):
            dst.write(line)
