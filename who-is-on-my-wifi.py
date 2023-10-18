from who_is_on_my_wifi import *
import pandas as pd
from tabulate import tabulate


def get_device_info():
    dev = device()
    print(f"""
    PC Name:            {dev[0]}
    PC Product-Name:    {dev[1]}
    MAC Address:        {dev[2]}
    IP Address (host):  {dev[3]}
    IP Address:         {dev[4]}
    Public IP:          {dev[5]}
    PC HostName:        {dev[6]}
    WiFi Name:          {dev[7]}
    Gateway:            {dev[8]}
    DNS 1:              {dev[9]}
    DNS 2:              {dev[10]}
    Password:           {dev[11]}
    Security:           {dev[12]}
    Interface:          {dev[13]}
    Frequency:          {dev[14]}
    Signal:             {dev[15]}
    Channel:            {dev[16]}


    Country:            {dev[17]}
    Region:             {dev[18]}
    City:               {dev[19]}
    Zip Code:           {dev[20]}
    Latitude:           {dev[21]}
    Longitude:          {dev[22]}
    Map:                {dev[23]}
    ISP:                {dev[24]}
    """)

def get_all_devices():
    WHO = who()
    return WHO

def tabulate_data(dev_list: list):
    ip_addresses = []
    mac_addresses = []
    devices = []
    for sublist in dev_list:
    # Check if the sublist contains 'IP Address:' (as it is in your example)
        if 'IP Address:' in sublist:
            # Find the index of 'IP Address:' and extract the IP address
            ip_index = sublist.index('IP Address:')
            ip_address = sublist[ip_index + 1]
            ip_addresses.append(ip_address)

        if 'Mac Address:' in sublist:
            # Find the index of 'IP Address:' and extract the IP address
            mac_index = sublist.index('Mac Address:')
            mac_address = sublist[mac_index + 1]
            mac_addresses.append(mac_address)

        if 'Device:' in sublist:
            # Find the index of 'IP Address:' and extract the IP address
            devices_index = sublist.index('Device:')
            devices_name = sublist[devices_index + 1]
            devices.append(devices_name)
        
    data = {
        "IP Adresses" : ip_addresses,
        "Devices": devices,
        "MAC Address": mac_addresses
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Convert DataFrame to a tabular string with borders
    table = tabulate(df, headers='keys', tablefmt='pretty', showindex=True)

    # Display the formatted table
    print(table)

all_devices = get_all_devices()
tabulate_data(all_devices)