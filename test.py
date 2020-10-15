import socket
import threading
from user import User

# Global constants
HOST = 'localhost'
PORT = 1000
SERVER_ADDRESS = (HOST, PORT)
BUFFER_SIZE = 4096
QUIT_MESSAGE = 'bye'

# Global variables
client_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_one.connect(SERVER_ADDRESS)
client_one.send('ChatBot'.encode('utf-8'))
client_two = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_two.connect(SERVER_ADDRESS)
client_two.send('User1'.encode('utf-8'))

def send_test_message(message, connection):
    """
    Sends test message
    :param message: str
    :param connection: socket
    :return None
    """
    connection.send(message.encode('utf-8'))
    if message == QUIT_MESSAGE:
        connection.close()


def recieve_test_message(connection):
    """
    Recieve messages
    :param connection: Socket
    :return None
    """
    while True:
        message = connection.recv(BUFFER_SIZE).decode('utf-8')
        if not message:
            break
        print(message)


threading.Thread(target = recieve_test_message, args = (client_one, )).start()
threading.Thread(target = recieve_test_message, args = (client_two, )).start()
send_test_message("message 1", client_one)
send_test_message("hello", client_one)
send_test_message("hello", client_two)
# threading.Thread(target = recieve_test_message, args = (client_two, )).start()


# def send_test_message(message, sender_socket):
#     while True:
#         sender_socket.send(message.encode('utf8'))


# def recieve_test_message(message, sender_socket):
#     while True:
#         if client_one == sender_socket:
#             client_two.recv(BUFFER_SIZE).decode('utf8')
#
#         else:
#             client_one.recv(BUFFER_SIZE).decode('utf8')
#         print(message)
