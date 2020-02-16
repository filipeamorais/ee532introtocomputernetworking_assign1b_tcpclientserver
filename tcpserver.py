import socket
import sys

serverPort = 1024

# create socket
print('# Creating socket')
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

# create socket
print('# Setting up the server')
try:
    serverSocket.bind(('',serverPort))
except socket.error:
    print('Failed to create socket')
    sys.exit()

# create socket
print('# Starting to listen')
serverSocket.listen(1)
print ('# The server is ready to receive')

# establish the connection, receive, process and send data
while True:
     connectionSocket, addr = serverSocket.accept()
     
     sentence = connectionSocket.recv(1024).decode()
     capitalizedSentence = sentence.upper()
     connectionSocket.send(capitalizedSentence.encode())
     print ('# Data sent')
     connectionSocket.close()
