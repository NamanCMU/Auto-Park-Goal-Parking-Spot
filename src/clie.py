import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = (sys.argv[1], 10000)
server_address2 = (sys.argv[1], 20000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
sock2.connect(server_address2)
 
f1=open ("Parking_Info.txt", "w") 

l1 = sock.recv(1024)
while (l1):
    f1.write(l1)
    l1 = sock.recv(1024)
f1.close()
sock.close()

f2=open ("goalCoordinatePark.txt", "w") 
l2 = sock2.recv(1024)
while (l2):
    f2.write(l2)
    l2 = sock2.recv(1024)
f2.close()
sock2.close()

