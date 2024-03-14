from os import system
import socket
def clear():
    system("cls || clear")

HOST = "127.0.0.1"
PORT = 65432
clear()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #AF_INET: ip v4
    #SOCK_STREAM: conexión tipo TCP
    s.bind((HOST,PORT))
    s.listen()

    conn, addr = s.accept() #Devuelve una tupla con dos elementos: conexión e ip del comunicante
    with conn:
        print(f"Conectado con {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)