import socket
import threading

HOST = 'localhost'
PORT = 1000
list_of_clients = []
server = None

def server_program():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    print('starting up on %s port %s' % server_address)
    server.bind(server_address)
    server.listen(10)
    threading.Thread(target = accept_clients, args = (server, "")).start()

def accept_clients(this_server, x):
    while True:
        client, client_address = this_server.accept()
        print('Got connection from', client_address)
        client_name = client.recv(4096).decode()
        client.send((f"Welcome {client_name}").encode())
        list_of_clients.append((client_name, client))
        threading.Thread(target = client_message, args = (client, client_address)).start()

def client_message(client, address):
    while True:
        data = client.recv(4096).decode()
        if not data or data.lower() == 'bye':
            break
        sender_name = get_name_given_connection(client)
        message = (sender_name + ": " + data).encode()
        send_everyone_message(message, client)

    index = get_client_index(client)
    del list_of_clients[index]
    client.close()

def send_everyone_message(message, sender):
    for client_name, client in list_of_clients:
        if client != sender:
            client.send(message)

def get_name_given_connection(connection):
    for client_name, client in list_of_clients:
        if client == connection:
            return client_name

def get_client_index(connection):
    for index, client_name, client in enumerate(list_of_clients):
        if client == connection:
            return index

if __name__ == '__main__':
    server_program()
