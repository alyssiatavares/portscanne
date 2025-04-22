
##  Port Scanner - Python Project

This project is a *port scanner* built with Python using the `python-nmap` library. It allows users to scan hosts (IP addresses or URLs) using three different types of scans to detect open ports and gather network information.

---

## Features:

- User can input a target IP or URL.
- Offers three types of scans:
  1. **SYN Scan** (`-sS`)
  2. **UDP Scan** (`-sU`)
  3. **Intense Scan** (`-sC -sV`)
- Uses the `python-nmap` library to interact with Nmap.
- Validates whether the host was successfully scanned.
- Displays open ports and detected protocols.

## How to Use?

1. *Clone the repository:*

      
        git clone https://github.com/your-username/portscanner.git
        cd portscanner


2. *Install dependencies:*
 
        pip install python-nmap


3. *Install Nmap on your machine:*

- Download and install Nmap for your system:  
   https://nmap.org/download.html

> Make sure the Nmap executable is added to your system's PATH.

4. *Run the scanner:*


       python scanner.py


##  Example Output:


    Welcome to Scanner!
    ------------------------------
    Enter IP or URL: www.google.com
    Choose the type of scan to be performed:
      1 - SYN Scan type scan
      2 - UDP Scan type scan
      3 - Intense type scan
    Enter the number corresponding to the desired option: 1
    
    Nmap version: (7, 94)
    Open doors: dict_keys([80, 443])


## Technologies Used:

- Python 3.x
- [python-nmap](https://pypi.org/project/python-nmap/)
- [Nmap](https://nmap.org/)

---

## License:

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

