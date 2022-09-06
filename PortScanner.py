from fileinput import close
from re import S
import sys 
import socket
from unittest import result
print()
print(" _  _ ___   ___              _ _       ")
print("| || |__ \ / _ \            (_) |      ")
print("| || |_ ) | | | | __ ___   ___| | __ _ ")
print("|__   _/ /| | | |/ _` \ \ / / | |/ _` |")
print("   | |/ /_| |_| | (_| |\ V /| | | (_| |")
print("   |_|____|\___/ \__,_| \_/ |_|_|\__,_|")
print()
print() 
objetivo = socket.gethostbyname(input("Insertar la dirección IP: "))

print("Escaneando Objetivo: " + objetivo)

try:
    for port in range(65,535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket,socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print ("El puerto {} está abierto".format(port))
        s.close()
except:
    print("\n Saliendo...")
    sys.exit(0)
