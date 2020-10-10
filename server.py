import socket

def server_program():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 10000
    server_address = (host, port)
    print 'starting up on %s port %s' % server_address
    s.bind(server_address)
#Binds to specific ip and port, can now listen to incoming connections
    print 'waiting for a connection'
    s.listen(2)

    while True:

        connection, client_address = s.accept()
        print 'Got connection from', client_address
        data = conn.recv()
        conn.sendall(data)

if __name__ == '__main__':
    server_program()
