import socket
import sys
import threading
from user import User

# Global constants
HOST = 'localhost'
PORT = 1000
SERVER_ADDRESS = (HOST, PORT)
BUFFER_SIZE = 4096
QUIT_MESSAGE = 'bye'


def client_program():
    """
    Sets up client socket and creates two threads
    One for sending messages and one for recieving messages
    :param None
    :return None
    """
    print(f'{"Welcome to the Chat App!": ^50}')
    user_name = input(f'{"Enter name: ": ^15}')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(SERVER_ADDRESS)
    client.send(user_name.encode('utf-8'))
    threading.Thread(target = recieve_message, args = (client, )).start()
    threading.Thread(target = send_message, args = (client, )).start()


def recieve_message(connection):
    """
    Listens for messages and prints them
    :param connection: socket
    return: None
    """
    while True:
        message = connection.recv(BUFFER_SIZE).decode('utf-8')
        if not message:
            break
        print(message)


def send_message(connection):
    """
    Sends client messages to Server & quits chat if client enters QUIT_MESSAGE
    :param connection: socket
    :return None
    """
    while True:
        print('Enter Message: ')
        message = input()
        connection.send(message.encode('utf-8'))
        if message == QUIT_MESSAGE:
            print('You are leaving the chat. Bye!')
            connection.close()
            sys.exit(0)


if __name__ == '__main__':
    client_program()
