#!/usr/bin/env python3

# for submit module work explore:

from itertools import repeat
import netmiko
import concurrent.futures
import logging
import time
import random
import yaml
from datetime import datetime

logging.getLogger('paramiko').setLevel(logging.WARNING)
logging.basicConfig(format='%(levename)s: %(message)s', level=logging.INFO)

connect_msg = '===> {} connect: {}'
receive_msg = '<=== {} receive: {}'

def send_mono(cmd, dev_dict):
	time.sleep(random.random() * 12)
	host = dev_dict['host']
	logging.info(connect_msg.format(datetime.now().time, host))
	try:
		with netmiko.ConnectHandler(**dev_dict) as ssh:
			ssh.enable()
			result = ssh.send_command(cmd)
			logging.info(receive_msg.format(datetime.now().time, host))
		return result
	except netmiko.NetMikoTimeoutException:
		return "time out"
	except netmiko.NetMikoAuthenticationException:
		return "auth err"


def function1(cmd, dev):
	logging.info(f'Func1 running {dev["host"]}, command: {cmd}')
	return send_mono(cmd, dev)


def function2(cmd, dev):
	logging.info(f'Func2 running {dev["host"]}, command: {cmd}')
	return send_mono(cmd, dev)


def send_stereo(cmds, devs_dict, limit=5):
	with concurrent.futures.ThreadPoolExecutor(max_workers=limit) as executor:
		future1_output = []
		future2_output = []
		for dev in devs_dict:
			for cmd in cmds:
				future1 = executor.submit(function1, cmd, dev)
				future1_output.append(future1)
			for cmd in cmds:
				future2 = executor.submit(function2, cmd, dev)
				future2_output.append(future2)
		for future in concurrent.futures.as_completed(future1_output + future2_output):
			future.result()


commands = ["sh ip int br", "sh arp", "sh version", "sh ip int br | ex un", "sh run | i interface", "sh vers | i IOS"]


if __name__ == '__main__':
	with open('devices.yaml') as f:
		devices = yaml.safe_load(f)
	send_stereo(commands, devices, limit=3)