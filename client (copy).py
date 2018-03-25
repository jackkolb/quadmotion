import socket
import sys
import subprocess
s2_out = subprocess.check_output([sys.executable, "leaptest2.py", "27"])
while True:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_addr = ('10.120.46.32', 1234)
    print >>sys.stderr, 'connection to %s port %s' % server_addr
    sock.connect(server_addr)

    try:
        while sock:
            # Prompt for message
            #msg = raw_input('Enter a message: ')
            sock.sendall(s2_out)

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()

