import socket

    def client_program():

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 1000)
        print 'starting up on %s port %s' % server_address
        s.connect(server_address)
        print 'enter message'
        message = input()
        while message.lower() != 'bye':
            s.send(message)
            resp = s.recv()
            print 'Recieved from server', resp
            message = input("Enter Message")


if __name__ == '__main__':
    client_program()
