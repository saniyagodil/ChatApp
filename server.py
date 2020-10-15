import socket
import threading
from user import User

# Global constants
HOST = 'localhost'
PORT = 1000
SERVER_ADDRESS = (HOST, PORT)
MAX_CONNECTIONS = 20
BUFFER_SIZE = 4096
QUIT_MESSAGE = 'bye'

# Global variables
users = []

def server_program():
    """
    Starts server
    :param None
    :return None
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(f'Starting up on {SERVER_ADDRESS}')
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
        print(f'Got connection from {client_address}')
        client_name = client.recv(BUFFER_SIZE).decode('utf-8')
        new_user = User(client, client_address, client_name)
        users.append(new_user)
        client.send((f'Welcome {client_name}').encode('utf-8'))
        threading.Thread(target = recieve_client_messages, args = (new_user, )).start()

    print('Server Crashed')

def recieve_client_messages(user):
    """
    Recieve message from client and send other users
    :param user: user
    :return None
    """
    while True:
        data = user.client.recv(BUFFER_SIZE).decode('utf-8')
        try:
            if data.lower() == QUIT_MESSAGE:
                message = (f'{user.name} left the chat').encode('utf-8')
            else:
                message = (f'{user.name}: {data}').encode('utf-8')
            send_everyone_message(message, user)
        except:
            print('Failed')
            break
    clean_up_conn(user)


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
                print(f'Failed to send {currUser} message')
                continue


def clean_up_conn(user_to_remove):
    """
    Handles user ending connection by removing them from list of users
    and closing their socket
    :param user_to_remove: user
    :return None
    """
    users.remove(user_to_remove)
    print(users)

if __name__ == '__main__':
    server_program()
