#!/usr/bin/env python3

import netmiko
from pprint import pprint
import yaml

def send_sh_cmd(devs, cmds):
	result = {}
	try:
		with netmiko.ConnectHandler(**devs) as t:
			print(f"Connected to {devs['host']}")
			t.enable()
			for cmd in cmds:
				result[cmd] = t.send_command(cmd)
		return result
	except(netmiko.NetMikoTimeoutException):
		print(f"Connection to {devs['host']} failed")
	except(netmiko.NetmikoAuthenticationException):
		print(f"Authentication to {devs['host']} failed")


if __name__ == '__main__':
	with open('devices-telnet.yaml') as f:
		devs = yaml.safe_load(f)
		for dev in devs:
			pprint(send_sh_cmd(devs[0], ['sh clock', 'sh ip int br']), width=120)