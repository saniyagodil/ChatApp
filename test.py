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
# client_two = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_two.connect(SERVER_ADDRESS)

def send_test_message(message):
    """
    Sends test message
    :param message: str
    :return None
    """
    client_one.send(message.encode('utf-8'))
    print(message)
    if message == QUIT_MESSAGE:
        client_one.close()


def recieve_test_message():
    """
    Recieve messages
    :param None
    :return None
    """
    while True:
        try:
            message = client_one.recv(BUFFER_SIZE).decode('utf-8')
            send_everyone_message()
            print(message)
        except:
            print("didn't recieve")


threading.Thread(target = recieve_test_message).start()
send_test_message("message 1")
send_test_message("hello")
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
