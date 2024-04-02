import socket

client_socket = socket.socket()
hostname = socket.gethostname()
print(hostname)

ipAddr = socket.gethostbyname(hostname)
port = 5001

client_socket.connect((ipAddr, port))
msg = input('Send your msg: \n')

while msg.lower().strip() != "bye":
    client_socket.send(msg.encode())
    msg = input('Send your msg: \n')

client_socket.send("bye".encode())
client_socket.close()
