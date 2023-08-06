import random
import socket
import time
import threading
from TheSilent.clear import clear

CYAN = "\033[1;36m"

def dolphin_scanner(host, delay=15):
    port_list = []
    clear()
    host = host.replace("https://", "")
    host = host.replace("http://", "")

    # most common 1,000 ports according to nmap
    init_port_list = [20, # ftp
                      21, # ftp
                      22, # ssh
                      23, # telnet
                      25, # smtp
                      53, # dns
                      80, # http
                      109, # pop2
                      110, # pop3
                      139, # smb
                      143, # imap
                      220, # imap
                      443, # https
                      445, # smb
                      585, # imap over tls
                      853, # dns over tls
                      989, # ftp over tls
                      990, # ftp over tls
                      992, # telnet over tls
                      993, # imap over tls
                      995, # pop3 over tls
                      1241, # nessus
                      1433, # mssql
                      1434, # mssql
                      3306, # mysql
                      3389, # rdp
                      3471, # moveit
                      3472, # moveit
                      3473, # moveit
                      5432, # postgresql
                      8080, # http alt
                      8443, # https alt
                      8834, # nessus
                      9050, # tor
                      9051, # tor
                      11443, # xbox developer mode
                      19132, # minecraft ipv4
                      19133, # minecraft ipv6
                      ]

    init_port_list = random.sample(init_port_list[:], len(init_port_list[:]))

    print(CYAN + "dolphin is scanning")
    for port in init_port_list:
        time.sleep(delay)
        try:
            print(f"checking port: {port}/tcp")
            my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            my_socket.settimeout(15)
            my_socket.connect((host,port))
            my_socket.close()
            port_list.append(port)

        except:
            my_socket.close()

    port_list.sort()
    port_list = list(set(port_list[:]))

    return port_list
