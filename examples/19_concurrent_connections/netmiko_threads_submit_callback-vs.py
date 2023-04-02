#!/usr/bin/env python3

import concurrent.futures
import logging
import netmiko
import datetime
import yaml

def send_mono(cmd, dev):
	pass

def send_stereo(cmd, dev):
	pass

if __name__ == '__main__':
	with open('devices.yaml') as f:
		devs_configs = yaml.safe_load(f)

