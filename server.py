import socket

def server_program():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 1000
    server_address = (host, port)
    print('starting up on %s port %s' % server_address)
    s.bind(server_address)
    print('waiting for a connection')
    s.listen(3)

    while True:
        connection, client_address = s.accept()
        print('Got connection from', client_address)

        while True:
            data = connection.recv(1024).decode()
            print('User:', client_address, 'Sent:', str(data))
            connection.sendall(data.encode())

if __name__ == '__main__':
    server_program()
