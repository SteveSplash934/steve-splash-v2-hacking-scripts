import nmap

# Create an nmap scanner object
try:
    nm = nmap.PortScanner()
    # Specify the target IP range or subnet
    target = "192.168.1.0/24"  # Replace with your network range

    # Perform a ping scan to identify live hosts
    nm.scan(hosts=target, arguments='-sn')

    # Iterate through the scan results
    for host in nm.all_hosts():
        print(f"Host: {host}")
        print(f"State: {nm[host].state()}")
        try:
            print(f"Hostname: {nm[host].hostname()}")
            print(f"Vendor: {nm[host]['vendor']}")
        except Exception as e:
            print("Unable to retrieve additional details.")
        print("\n")

except Exception as e:
    print("An error has occurred: ", e)

