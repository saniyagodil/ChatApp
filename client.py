import socket
import threading

HOST = 'localhost'
PORT = 1000

def client_program():
    print(f'{"Welcome to the Chat App!": ^50}')
    user_name = input(f'{"Enter name: ": ^15}')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    client.connect(server_address)
    client.send(user_name.encode())
    threading.Thread(target = recieve_message, args = (client, )).start()
    threading.Thread(target = send_message, args = (client, )).start()

def recieve_message(connection):
    while True:
        message = connection.recv(4096).decode()
        if not message:
            break
        print(message)

def send_message(connection):
    while True:
        print("Enter Message: ")
        message = input()
        connection.send(message.encode())
        if message == 'bye':
            print("You are leaving the chat. Bye!")
            break

if __name__ == '__main__':
    client_program()
