#!/usr/bin/env python

from turtle import width
import netmiko
from pprint import pprint

def send_sh_cmd(ip, user, passw, enable, cmds):
	pprint(f'Connect to {ip}')
	result = {}
	try:
		with netmiko.ConnectHandler(
			device_type = 'cisco_ios', timeout = 6,
			host = ip, username = user, password = passw, secret = enable) as ssh:
			ssh.enable()
			for cmd in cmds:
				result[cmd] = ssh.send_command(cmd)
		return result
	except(netmiko.NetmikoTimeoutException, netmiko.NetmikoAuthenticationException) as error:
		print(error)		

if __name__ == '__main__':
	devices = ['192.168.100.1', '192.168.100.2', '192.168.100.3']
	cmd = ['sh clock', 'sh ip int br']
	for dev in devices:
		result = send_sh_cmd(dev, 'cisco', 'cisco', 'cisco', cmd)
		if result:
			pprint(result, width=120)
		else: continue