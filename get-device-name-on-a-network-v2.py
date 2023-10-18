import nmap
from scapy.all import ARP, Ether, srp

# Define the target IP range or subnet of your local network
# target_ip = str(input("[?] Enter your IP: ")) or "192.168.0.1/24"  # Adjust for your network
# if target_ip.split("/") and target_ip[1] != "":
#     pass
# else: 
#     target_ip = target_ip + "24"
#     exit()

target_ip = "192.168.0.1/24"

# Perform an ARP scan to discover devices
def scan_devices(target_ip):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []
    
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

# Perform a network scan to get device details
def get_device_details(devices):
    scanner = nmap.PortScanner()
    for device in devices:
        scanner.scan(hosts=device['ip'], arguments='-T4 -F')  # Adjust scan options as needed

    for device in devices:
        try:
            device['hostname'] = scanner[device['ip']].hostname()
        except KeyError:
            device['hostname'] = "N/A"
    
    return devices

# Main function
def main():
    devices = scan_devices(target_ip)
    devices_with_details = get_device_details(devices)

    for device in devices_with_details:
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Hostname: {device['hostname']}")

if __name__ == "__main__":
    main()
