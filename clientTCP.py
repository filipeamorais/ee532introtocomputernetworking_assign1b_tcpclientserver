import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('67.9.1.190', 5001)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = bytes(input("Please Enter Message : "), 'utf8')
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(2048)
        amount_received += len(data)
        print('received ', str(data.decode("utf-8")))

finally:
    print('closing socket')
    sock.close()