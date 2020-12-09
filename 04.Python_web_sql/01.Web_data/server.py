import socket
import threading # allows simultaneous processes

PORT = 5050
# enter local IPv4 address 
# SERVER = "192.168.1.74"

# authomatically gets the local IP address
SERVER = socket.gethostbyname(socket.gethostname())

# local IPv4 address
# print(SERVER)

# get machine's name
# print(socket.gethostname())
