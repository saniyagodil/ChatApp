import socket
import threading

HOST = 'localhost'
PORT = 1000
list_of_clients = []

def server_program():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('starting up on %s port %s' % server_address)
    server.bind(server_address)
    server.listen(20)
    threading.Thread(target = accept_clients, args = (server, )).start()

def accept_clients(this_server):
    while True:
        client, client_address = this_server.accept()
        print('Got connection from', client_address)
        client_name = client.recv(4096).decode()
        client.send((f"Welcome {client_name}").encode())
        list_of_clients.append((client_name, client))
        threading.Thread(target = client_message, args = (client, )).start()

def client_message(client):
    while True:
        data = client.recv(4096).decode()
        if not data or data.lower() == 'bye':
            break
        sender_name = get_name_given_connection(client)
        message = (sender_name + ": " + data).encode()
        send_everyone_message(message, client)

    clean_up_conn(client)

def send_everyone_message(message, sender):
    for client_name, client in list_of_clients:
        if client != sender:
            try:
                client.send(message)
            except:
                continue

def get_name_given_connection(connection):
    for client_name, client in list_of_clients:
        if client == connection:
            return client_name

def get_client_index(connection):
    for index, client_name, client in enumerate(list_of_clients):
        if client == connection:
            return index

def clean_up_conn(connection):
    index = get_client_index(connection)
    print(index)
    del list_of_clients[index]
    connection.close()

if __name__ == '__main__':
    server_program()
