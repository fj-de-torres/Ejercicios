from os import system
import socket,  threading
from colorama import Fore, Style

HOST_IP = socket.gethostbyname(socket.gethostname()) #me da la IP pública de la máquina

HOST_PORT = 12345
ENCODER = 'utf-8'
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

client_name_list = list()
client_socket_list = list()

def clear():
    system("cls || clear")

def connect_client():
    '''Connect an incoming client to the server'''
    while True:
        #Accept any incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}...")

        #Send a NAME flag to prompt the client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BUFFER_SIZE).decode(ENCODER)

        #Add new client socket and client name to appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        #Update the server, individual client, and ALL clients
        print(f"Name of new client is {client_name}\n") #server
        client_socket.send(f"{client_name}, you have connected to the server!".encode(ENCODER)) #Individual client
        broadcast_message(f"{client_name} has joined the chat!".encode(ENCODER)) #Comunicación activa con todos y cada uno de los clientes con los que está contectado.

        #Now that a new client has connected, start a thread (porque si no, se daría la secuencialidad; es decir, hasta que un cliente no termine su chat, no podría conectarse el siguiente)
        recieve_thread = threading.Thread(target=recieve_message, args=(client_socket,))
        recieve_thread.start()

def recieve_message(client_socket):
    '''Recieve an incoming message from a specific client and forward the message to be broadcast'''
    while True:
        try:
            #Get the name of the given client
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]
            
            #Recieve message from the client
            message = client_socket.recv(BUFFER_SIZE).decode(ENCODER)
            message = f"\033[1;92m\t{name}: {message}\033[0m".encode(ENCODER)
            broadcast_message(message)
        except:
            #Find the index of the client socket in our list
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            #Remove the client socket and name from lists
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            #Close the client socket
            client_socket.close()

            #Broadcast that the client has left the chat.
            broadcast_message(f"\033[5;91m\t{name} has left the chat!\033[0m".encode(ENCODER))
            break

def broadcast_message(message):
    '''Send a message to ALL clients connected to the server'''
    for client_socket in client_socket_list:
        client_socket.send(message)

#Start the server
try:
    print(f"Server is listening on {HOST_IP}:{HOST_PORT}...")
    connect_client()
except KeyboardInterrupt as ex:
    clear()
    print()
    print(Fore.YELLOW + "KeyboardInterruptus" + Fore.WHITE)
    print()