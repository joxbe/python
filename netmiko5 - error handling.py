#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

menu = {}
menu['1']="Make Boise Active" 
menu['2']="Make MV Active"
menu['3']="Exit"

while True: 
    options = menu.keys()
    "options.sort()"

    for entry in options:
        print(entry, menu[entry])

    datacenter = input("Please Select: ")

    username = input('Enter your SSH username: ')
    password = getpass()

    "Here we are opening our files"

    with open('enable_command') as f:
        enable_command = f.read().splitlines()

    with open('disable_command') as f:
        disable_command = f.read().splitlines()

    with open('Boise') as f:
        Boise = f.read().splitlines()

    with open('MV') as f:
        MV = f.read().splitlines()


    if datacenter == "1":
        for devices in MV:
            print ('Connecting to device and disabling Vlan ' + devices)
            ip_address_of_device = devices
            ios_device = {
                'device_type': 'cisco_ios',
                'ip': ip_address_of_device, 
                'username': username,
                'password': password
            }

            try:
                net_connect = ConnectHandler(**ios_device)
            except AuthenticationException:
                print ('Authentication failure: ' + ip_address_of_device)
                continue
            except NetMikoTimeoutException:
                print ('Timeout to device: ' + ip_address_of_device)
                continue
            except EOFError:
                print ('End of file while attempting device ' + ip_address_of_device)
                continue
            except SSHException:
                print ('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
                continue
            except Exception as unknown_error:
                print ('Some other error: ' + str(unknown_error))
                continue

            output = net_connect.send_config_set(disable_command)
            print (output)

        """This uses the enable_devices_list of devices that we want to enable
        and performs the vlan enable commands from enable_command file"""

        for devices in Boise:
            print ('Connecting to device and enabling Vlan ' + devices)
            ip_address_of_device = devices
            ios_device = {
                'device_type': 'cisco_ios',
                'ip': ip_address_of_device, 
                'username': username,
                'password': password
            }

            try:
                net_connect = ConnectHandler(**ios_device)
            except AuthenticationException:
                print ('Authentication failure: ' + ip_address_of_device)
                continue
            except NetMikoTimeoutException:
                print ('Timeout to device: ' + ip_address_of_device)
                continue
            except EOFError:
                print ('End of file while attempting device ' + ip_address_of_device)
                continue
            except SSHException:
                print ('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
                continue
            except Exception as unknown_error:
                print ('Some other error: ' + str(unknown_error))
                continue

            output = net_connect.send_config_set(enable_command)
            print (output)

    elif datacenter == "2":
        for devices in Boise:
            print ('Connecting to device and disabling Vlan ' + devices)
            ip_address_of_device = devices
            ios_device = {
                'device_type': 'cisco_ios',
                'ip': ip_address_of_device, 
                'username': username,
                'password': password
            }

            try:
                net_connect = ConnectHandler(**ios_device)
            except AuthenticationException:
                print ('Authentication failure: ' + ip_address_of_device)
                continue
            except NetMikoTimeoutException:
                print ('Timeout to device: ' + ip_address_of_device)
                continue
            except EOFError:
                print ('End of file while attempting device ' + ip_address_of_device)
                continue
            except SSHException:
                print ('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
                continue
            except Exception as unknown_error:
                print ('Some other error: ' + str(unknown_error))
                continue

            output = net_connect.send_config_set(disable_command)
            print (output)

        """This uses the enable_devices_list of devices that we want to enable
        and performs the vlan enable commands from enable_command file"""

        for devices in MV:
            print ('Connecting to device and enabling Vlan ' + devices)
            ip_address_of_device = devices
            ios_device = {
                'device_type': 'cisco_ios',
                'ip': ip_address_of_device, 
                'username': username,
                'password': password
            }

            try:
                net_connect = ConnectHandler(**ios_device)
            except AuthenticationException:
                print ('Authentication failure: ' + ip_address_of_device)
                continue
            except NetMikoTimeoutException:
                print ('Timeout to device: ' + ip_address_of_device)
                continue
            except EOFError:
                print ('End of file while attempting device ' + ip_address_of_device)
                continue
            except SSHException:
                print ('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
                continue
            except Exception as unknown_error:
                print ('Some other error: ' + str(unknown_error))
                continue

            output = net_connect.send_config_set(enable_command)
            print (output)

    elif datacenter == "3":
        break
    else:
        print("Not a valid selection")
        break
