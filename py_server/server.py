import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socke to the port
server_addr = ('localhost', 1234)
print 'starting server on %s port %s' % server_addr
sock.bind(server_addr)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_addr = sock.accept()
    try:
        while connection:
            print >>sys.stderr, 'connection from ', client_addr

            data  = connection.recv(16)
            print >>sys.stderr, 'recieved %s' % data
    finally:
        # Clean up the connection
        connection.close()
