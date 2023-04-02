#/usr/bin/env python3

import netmiko, yaml

def read_cmd(params, cmd):
	result = ""
	try:
		with netmiko.ConnectHandler(**params) as ssh:
			ssh.enable()
			ssh.send_command('terminal length 100')
			prompt = ssh.find_prompt()
			ssh.write_channel(f"{cmd}\n")
			while True:
				page = ssh.read_until_pattern(f"More|{prompt}")
				result += page
				if 'More' in page:
					ssh.write_channel(" ")
				elif prompt in page:
					break
	
	except netmiko.NetMikoTimeoutException:
		print(f'connection: {params["host"]}, failed - timeout')
	except netmiko.NetmikoAuthenticationException:
		print(f'connection: {params["host"]}, failed - authentication')

	return result

if __name__ == '__main__':
	with open('devices.yaml') as f:
		hosts = yaml.safe_load(f)
	print(read_cmd(hosts[0], 'sh run'))