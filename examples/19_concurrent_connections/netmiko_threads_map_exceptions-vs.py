#!/usr/bin/env python3

import logging
import concurrent.futures
import netmiko
import yaml
from pprint import pprint
from datetime import datetime
from itertools import repeat


logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.basicConfig(format="%(threadName)s: %(name)s: %(levelname)s: %(message)s", level=logging.INFO)


def send_cmd(dev_dict, cmd):
	start_msg = "===> {} Connection: {}"
	received_msg = "<=== {} Received: {}"
	host = dev_dict["host"]
	logging.info(start_msg.format(datetime.now().time(), host))

	try:
		with netmiko.ConnectHandler(**dev_dict) as ssh:
			ssh.enable()
			result = ssh.send_command(cmd)
			logging.info(received_msg.format(datetime.now().time(), host))
		return result

	except netmiko.NetMikoTimeoutException:
		print(f"{host}: timeout")
	except netmiko.NetMikoAuthenticationException:
		print(f"{host}: auth failed")

def send_concurrent_cmds(devs_dict, cmd):
	data = {}
	with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
		result = executor.map(send_cmd, devs_dict, repeat(cmd))
		for device, output in zip(devs_dict, result):
			data[device["host"]] = output
	return data


if __name__ == "__main__":
	with open("devices.yaml") as f:
		devices = yaml.safe_load(f)
	pprint(send_concurrent_cmds(devices, "sh ip int br"))

