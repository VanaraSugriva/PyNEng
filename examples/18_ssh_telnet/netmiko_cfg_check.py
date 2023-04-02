#!/usr/bin/env python

import netmiko
import yaml
import re


def cfg_cmd(session, section, cmd):
    cfg = session.send_command('sh run')
    regex = "{}\n( .*\n*) {}".format(section, cmd)
    match = re.search(regex, cfg)
    if match:
        print(f'settings: {cmd} are already exist in config')
        return
    
    result = session.send_config_set([section, cmd])
    return result

def send_cfg(device, section, cmd):
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            output = cfg_cmd(ssh, section, cmd)
            if output:
                print(output)
    except netmiko.NetMikoTimeoutException:
        print(f'connect to {device["host"]} failed: timeout')
    except netmiko.NetmikoAuthenticationException:
        print(f'connect to {device["host"]} failed: authentication')

if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        for device in devices:
            send_cfg(device, "interface Loopback45", "ip address 5.5.5.5 255.255.255.255")
