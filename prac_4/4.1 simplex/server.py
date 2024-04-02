import socket

server_socket = socket.socket()
hostname = socket.gethostname()
print(hostname)

ipAddr = socket.gethostbyname(hostname)
port = 5001

server_socket.bind((hostname, port))
server_socket.listen(2)

print("Server is listening...")
conn, addr = server_socket.accept()
print('Connection from: ' + str(addr))

while True:
    data = conn.recv(1024).decode()
    if data.lower().strip() == "bye":
        break
    print('Msg from Client : ' + str(data))

conn.close()
server_socket.close()
