#!/usr/bin/env python3

import yaml
import netmiko
from pprint import pprint

def send_cfg(params, cmds):
    result = ""
    if type(cmds) == 'str':
        cmds = [cmds]
    try:
        with netmiko.ConnectHandler(**params) as ssh:
            result += ssh.config_mode()
            for cmd in cmds:
                out = ssh.send_config_set(cmd, exit_config_mode=False)
                if "%" in out:
                    raise ValueError(f'error, when executing cmd, {cmd}!')
                result += out
            result += ssh.exit_config_mode()				
            return result.replace("\r\n", "\n")
    except netmiko.NetMikoTimeoutException:
        print(f'connect to {params["host"]} failed: timeout')
    except netmiko.NetmikoAuthenticationException:
        print(f'connect to {params["host"]} failed: authentication')

if __name__ == '__main__':
    cmds = {
        "192.168.100.1": ["int lo9", "ipaddress 10.90.90.1 255.255.255.255"],
        "192.168.100.2": ["int lo9"],
        "192.168.100.3": ["int lo9"]
        }
    with open('devices.yaml') as f:
            devices = yaml.safe_load(f)
            for device in devices:
                try:
                    out = send_cfg(device, cmds[device['host']])
                    pprint(out)
                except ValueError as error:
                    print(error)