import sys, serial, socket, thread

# Create serial port
ser_port = "/dev/ttyACM0"
baud = 9600

ser = serial.Serial(ser_port, baud, timeout=1)

if ser.isOpen():
    print(ser.name + ' is open...')

def onNewClient(clientSock, addr):
    while True:
        try:
            msg = clientSock.recv(1)
            if msg == '':
                raise RuntimeError('socket connection broken')
            else:
                print 'Message recieved: %s' % msg
                ser.write(msg)
        finally:
            clientSock.close()
    clientSock.shutdown()
    clientSock.close()


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_addr = ('10.120.46.32', 1234)
print 'starting server on %s port %s' % server_addr
sock.bind(server_addr)

print 'Waiting for clients...'

# Listen for incoming connections
sock.listen(2)
print 'Connection Established'

while True:
    try:
        c, addr = s.accept()
        thread.start_new_thread(onNewClient, (c, addr))
    finally:
        s.close()
s.close()
