import socket
import threading

# Global constants
HOST = 'localhost'
PORT = 1000
SERVER_ADDRESS = (HOST, PORT)
MAX_CONNECTIONS = 20
BUFFER_SIZE = 4096
QUIT_MESSAGE = 'bye'

# Global variables
list_of_clients = []
users = []

def server_program():
    """
    Starts server
    :param None
    :return None
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('starting up on %s port %s' % server_address)
    server.bind(SERVER_ADDRESS)
    server.listen(MAX_CONNECTIONS)
    threading.Thread(target = accept_clients, args = (server, )).start()


def accept_clients(this_server):
    """
    Accepts new clients and create a new thread for each
    :param this_server : socket
    :return None
    """
    while True:
        client, client_address = this_server.accept()
        print('Got connection from', client_address)
        client_name = client.recv(BUFFER_SIZE).decode()

        new_user = User(client, client_address, client_name)
        users.append(new_user)

        client.send((f"Welcome {client_name}").encode())
        list_of_clients.append((client_name, client))
        threading.Thread(target = recieve_client_messages, args = (user, )).start()

    print("Server Crashed")

def recieve_client_messages(user):
    """
    Recieve message from client and send other users
    :param user: user
    :return None
    """
    while True:
        data = user.client.recv(BUFFER_SIZE).decode()
        if not data:
            break
        print(data)
        sender_name = user.name
        if data.lower() == QUIT_MESSAGE:
            message = (sender_name + "left the chat").encode()
        else:
            message = (sender_name + ": " + data).encode()
        send_everyone_message(message, client)
    clean_up_conn(client)


def send_everyone_message(message, user):
    """
    Sends message to all clients except for Sender
    :param message : str
    :param user : user
    :return: None
    """
    for currUser in users:
        if currUser.client != user.client:
            try:
                currUser.client.send(message)
            except:
                continue


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
