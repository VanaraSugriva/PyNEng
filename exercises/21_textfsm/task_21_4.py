# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""

from textfsm import clitable
from pprint import pprint
from datetime import datetime
import netmiko
import yaml
import logging
import os

logging.basicConfig(
     format = '%(levelname)s: %(message)s', level=logging.INFO)
start_msg = '===> {} Connected: {}'
finish_msg = '<=== {} Received: {}'

def parse_command_dynamic(output_src, attributes, template_path='templates', index='index'):
    cli_table = clitable.CliTable(index, template_path)
    cli_table.ParseCmd(output_src, attributes)
    headers = list(cli_table.header)
    return [dict(zip(headers, row)) for row in cli_table]


def send_show_command(device_dict, command):
    logging.getLogger('paramiko').setLevel(logging.WARN)
    logging.info(start_msg.format(datetime.now().time(), device_dict['host']))
    result = ''
    try:
        with netmiko.ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
    except netmiko.NetMikoTimeoutException:
        # print(f'{device_dict["host"]}: Connection failed')
        logging.info(f'{datetime.now().time()}, {device_dict["host"]}: Failed connection')
    except netmiko.NetMikoAuthenticationException:
        # print(f'{device_dict["host"]}: Authentication fail')
        logging.info(f'{datetime.now().time()}, {device_dict["host"]}: Failed authentication')
    logging.info(finish_msg.format(datetime.now().time(), device_dict['host']))
    if result != '':
        return result


def send_and_parse_show_command(device_dict, command, template_path='templates', index='index'):
    attributes = {"Command": command, "Vendor": device_dict["device_type"]}
    output = send_show_command(device_dict, command)
    return parse_command_dynamic(output, attributes, template_path, index)


if __name__ == '__main__':
    full_path = os.path.join(os.getcwd(), "templates")
    with open('devices.yaml') as devices_yaml:
        devices = yaml.safe_load(devices_yaml)
        for device in devices:
            pprint(send_and_parse_show_command(device, 'sh ip int br'), width=120)

