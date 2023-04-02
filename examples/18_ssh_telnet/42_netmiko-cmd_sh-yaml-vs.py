#!/usr/bin/env python

import netmiko
import yaml
from pprint import pprint

def send_sh_cmd(dev_params, cmds):
	result = {}
	try:
		with netmiko.ConnectHandler(**dev_params) as ssh:
			print(f'Connected to {dev_params["host"]}')
			ssh.enable()
			for cmd in cmds:
				out = ssh.send_command(cmd)
				result[cmd] = out
		return result
	except(netmiko.NetmikoTimeoutException):
		print(f"Connection to {dev_params['host']} failed")
	except(netmiko.NetmikoAuthenticationException):
		print(f"Authentication to {dev_params['host']} failed")

if __name__ == '__main__':
	with open('devices.yaml') as f:
		devices = yaml.safe_load(f)
		for device in devices:
			result = send_sh_cmd(device, ['sh clock', 'sh ip int br'])
			if result:
				pprint(result, width=120)
			else:
				continue