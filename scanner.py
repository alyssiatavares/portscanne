import nmap
scanner = nmap.PortScanner()

print("Seja bem vindo ao Scanner!")
print(30*"-")
ip = input("Digite o IP ou URL: ")
print("O ip digitado foi: ", ip)
type(ip)

menu = input("""\n Escolha o tipo de scan a ser realizado:
      1 - Varredura do tipo SYN Scan
      2 - Varredura do tipo UDP Scan
      3- Varredura do tipo intensa
      Digite o número correspondente a opção desejada: """)

print("A opção escolhida foi: ", menu)  

if menu == "1":
    print("Versao do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print(" ")
    print("Portas abertas: ", scanner[ip]['tcp'].keys())
   
elif menu == "2":
    print("Versao do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print(" ")
    print("Portas abertas: ", scanner[ip]['udp'].keys())
    
elif menu == "3":
    print("Vesao do Nmap: ", scanner.nmap_version())
    scanner.scan(ip,'1-1024', '-v -sC')
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print(" ")
    print("Portas abertas: ", scanner[ip]['tcp'].keys())

else:
    print("Opção inválida!")
    print("Tente novamente.")
    exit(0)
