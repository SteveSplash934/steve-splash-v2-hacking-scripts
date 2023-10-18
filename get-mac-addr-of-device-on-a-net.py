from scapy.all import ARP, Ether, srp

# Specify the target IP address
target_ip = "192.168.0.1"  # Replace with the IP address you want to look up

# Create an ARP request packet
arp = ARP(pdst=target_ip)

# Create an Ethernet frame to contain the ARP packet
eth = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address

# Combine the Ethernet frame and ARP packet
packet = eth / arp

# Send the packet and capture the response
result = srp(packet, timeout=3, verbose=0)[0]

# Extract the MAC address from the response
mac = result[0][1].hwsrc

# Print the MAC address
print(f"MAC address for {target_ip}: {mac}")
