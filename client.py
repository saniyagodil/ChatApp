import socket
import threading


def client_program():
    HOST = 'localhost'
    PORT = 1000
    user_name = input('Enter name: ')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    print('starting up on %s port %s' % server_address)
    client.connect(server_address)
    client.send(user_name.encode())
    threading.Thread(target = recieve_message, args = (client, "")).start()
    threading.Thread(target = send_message, args = (client, "")).start()

def recieve_message(connection, x):
    while True:
        message = connection.recv(4096).decode()
        if not message:
            break
        print(message)


def send_message(connection, x):
    while True:
        message = input("Enter Message: ")
        if message.lower() != 'bye':
            connection.send(message.encode())
        else:
            break

if __name__ == '__main__':
    client_program()
