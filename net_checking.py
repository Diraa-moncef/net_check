print("|###|   ###|     |######|      |######|")
print("|###|\#\###|     |#|             |##|  ")
print("|###| \#\##|     |###|           |##|  ")
print("|###|  \#\#|     |#|             |##|  ")
print("|###|   \#\|     |######|        |##|  ")
print("|######|   |##|  |##|   |######|   |######|   |###|   /##/")
print("|#|        |##|--|##|   |#|        |#|        |###|  /##/ ")
print("|#|        |##|##|##|   |#|        |#|        |###| /##/")
print("|#|        |##|##|##|   |###|      |#|        |###|/##/")
print("|#|        |##|  |##|   |#|        |#|        |###|\##\ ")
print("|#|        |##|  |##|   |#|        |#|        |###| \##\ ")
print("|######|   |##|  |##|   |######|   |######|   |###|  \##\ ")

print("1) find an IP address from the domain name\n2) find a domain name from an IP address\n3) find the port name from its number\n4) find the port number from its name\n\t!!!!!!!!!!you must enter the number of the service that suits you!!!!!!!!!!")
import socket
while True:
    num_serv=int(input("please enter the operation number=>"))
    if num_serv == 1:
        ip =input(" please enter the domain name=>")
        ip_addr = socket.gethostbyname(str(ip))
        print(ip_addr)
    elif num_serv == 2:
        domain = input(" please enter your IPV4 address =>")
        dn = socket.gethostbyaddr(str(domain))
        print(dn)
    elif num_serv == 3:
        name_port=int(input("please enter the port number =>"))
        port = socket.getservbyport(name_port)
        print(port)
    elif num_serv == 4:
        num_port = input("please enter the port number =>")
        name = socket.getservbyname(num_port)
        print(name)
        rep = input(" if you want to repeat the operation enter (yes/no)")
    else:
        print("try again this parameter does not exist!!!")
