import socket

server_socket = socket.socket()

hostname = socket.gethostname()
print(hostname)

ipAddr = socket.gethostbyname(hostname)
port = 5002

server_socket.bind((hostname, port))
server_socket.listen(2)

conn, addr = server_socket.accept()
print('Connection from: ' + str(addr))

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print('Msg from Client : ' + str(data))
    response = input('Send your response: \n')
    conn.send(response.encode())  # Send response to client

    # Receive client's message
    data = conn.recv(1024).decode()
    if not data:
        break
    print('Msg from Client : ' + str(data))

conn.close()
server_socket.close()
