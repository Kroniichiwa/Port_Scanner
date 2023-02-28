import pyfiglet
import sys
import socket
from datetime import datetime

ip_port=[]

def get_ip(my_list):
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print (ascii_banner)

    target = input(str("Target IP: "))

    #banner
    print("_"*50)
    print("Scanning target: " + target)
    print("Scanning startd at: " + str(datetime.now()))
    print("_"*50)
    return scanner(target,my_list)

def scanner(target, my_list):
    print("------target is :", target ,"----------------")
    try:
        # Scan every port on the target ip
        for port in range(1, 20000):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            # Return open port
            result = s.connect_ex((target, port))
            if result == 0:
                print("[*] Port {} is open".format(port))
                my_list.append(str(port))
        return my_list
    except KeyboardInterrupt:
        print("In Exiting")
        sys.exit()
    except socket.error:
        print("\ Host not responding")
        sys.exit()


if __name__ == '__main__': 
    print(get_ip(ip_port))
    #print("Here what in the list: ",ip_port)