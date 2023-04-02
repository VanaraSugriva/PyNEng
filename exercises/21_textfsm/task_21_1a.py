# -*- coding: utf-8 -*-
"""
Задание 21.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM.
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt
и шаблоне templates/sh_ip_int_br.template.
"""
import textfsm
from pprint import pprint

def parse_cmd_out(template, output):
    with open(template) as template:
        fsm = textfsm.TextFSM(template)
    return fsm.ParseTextToDicts(output)

if __name__ == '__main__':
    with open('output/sh_ip_int_br.txt') as src:
        dst = parse_cmd_out('templates/sh_ip_int_br.template', src.read())
    pprint(dst)