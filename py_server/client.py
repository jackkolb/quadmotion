import socket
import sys

while True:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_addr = ('localhost', 1234)
    print >>sys.stderr, 'connection to %s port %s' % server_addr
    sock.connect(server_addr)

    try:
        while sock:
            # Prompt for message
            msg = raw_input('Enter a message: ')
            sock.sendall(msg)

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()

