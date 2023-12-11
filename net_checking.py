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
print("1) trouver une adresse IP a partir du nom de domaine\n2) trouver un nom de domaine apartir d'une adresse IP\n3) trouver le nom du port a partir de son numero\n4)trouver le numero du port a partir de son nom\n\t!!!!!!!!!!vous devez entrez le numero du service qui vous convient!!!!!!!!!!")
import socket
while True:
    num_serv=int(input("veuillez entrer le numero d'operation =>"))
    if num_serv == 1:
        ip = input("veuillez entrer le nom de domain =>")
        ip_addr = socket.gethostbyname(str(ip))
        print(ip_addr)
    elif num_serv == 2:
        domain = input("veuillez entrer votre adresse IPV4 =>")
        dn = socket.gethostbyaddr(domain)
        print(dn)
    elif num_serv == 3:
        name_port=int(input("veuillez entrer le numero du port =>"))
        port = socket.getservbyport(name_port)
        print(port)
    elif num_serv == 4:
        num_port = input("veuillez entrer le nom du port =>")
        name = socket.getservbyname(num_port)
        print(name)
        rep = input("si vous voulez repeter l'operation entrer (yes/non) :")
    else:
        print("esseyer une autre fois ce parametre n'existe pas!!!")
