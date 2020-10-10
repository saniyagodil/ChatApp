import socket

def client_program():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 1000
    server_address = (host, port)
    print('starting up on %s port %s' % server_address)
    s.connect(server_address)
    message = input("Enter Message")
    while message.lower() != 'bye':
        s.send(message.encode())
        resp = s.recv(1024).decode()
        print('Recieved from server', resp)
        message = input("Enter Message: ")


if __name__ == '__main__':
    client_program()
