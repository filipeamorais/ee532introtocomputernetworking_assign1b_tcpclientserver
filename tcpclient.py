import socket
import sys

host = '172.24.186.52'
port = 1024

# create socket
print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

# print('# Getting remote IP address') 
# try:
#     remote_ip = socket.gethostbyname( host )
# except socket.gaierror:
#     print('Hostname could not be resolved. Exiting')
#     sys.exit()

# Connect to remote server
#print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
print('# Connecting to server, ' + host)
s.connect((host , port))

# Get text input from the user
sentence = input('Input lowercase sentence:')


# Send data to remote server
print('# Sending data to server')
request = (sentence.encode())

try:
    s.sendall(request)
except socket.error:
    print ('Send failed')
    sys.exit()

# Receive data
print('# Receiving data from server')
full_reply = ''

 # Look for the response
amount_received = 0
amount_expected = len(sentence)

while amount_received < amount_expected:
    data = s
    .recv(2048)
    amount_received += len(data)
    print('received ', str(data.decode("utf-8")))
# while True:
#     reply = s.recv(8)
#     if len(reply) == 0:
#         break
#     full_reply += reply.decode()
    

print (full_reply)

print('# Finished!')