import nmap
scanner = nmap.PortScanner()

print("Welcome to Scanner!")
print(30*"-")
ip = input("Enter IP or URL: ")
print("The IP entered was:", ip)
type(ip)

menu = input("""\n Choose the type of scan to be performed:
      1 - SYN Scan type scan
      2 - UDP Scan type scan
      3- Intense type scan
      Enter the number corresponding to the desired option: """)

print("The chosen option was:", menu)  

if menu == "1":
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())

    if ip in scanner.all_hosts():
        print("IP Status: ", scanner[ip].state())
        print(scanner[ip].all_protocols())
        print(" ")
        print("Open doors: ", scanner[ip]['tcp'].keys())
    else:
        print("❌ Host not found or did not respond to the scan.")
   
elif menu == "2":
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    if ip in scanner.all_hosts():
        print("IP Status: ", scanner[ip].state())
        print(scanner[ip].all_protocols())
        print(" ")
        print("Open doors: ", scanner[ip]['udp'].keys())
    else:
        print("❌ Host not found or did not respond to the scan.")
    
elif menu == "3":
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip,'1-1024', '-v -sC -sV')
    print(scanner.scaninfo())
    if ip in scanner.all_hosts():
        print("IP Status: ", scanner[ip].state())
        print(scanner[ip].all_protocols())
        print(" ")
        print("Open doors: ", scanner[ip]['tcp'].keys())
    else:
        print("❌ Host not found or did not respond to the scan.")
else:
    print("Invalid option!")
    print("Please, try again.")
    exit(0)

