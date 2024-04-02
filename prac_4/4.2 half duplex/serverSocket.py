import socket

server_socket = socket.socket()

hostname = socket.gethostname()
print(hostname)

ipAddr = socket.gethostbyname(hostname) # gets the ipAddr using the hostname like "www.google.com"
# print(ipAddr)

port = 5002

server_socket.bind((hostname, port)) # binds host addr and port together
server_socket.listen(2)

conn, addr = server_socket.accept()

print('Connection from: '+ str(addr))

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    print('Msg from Client : '+ str(data))

    data = input('Send your response: \n')

    conn.send(data.encode()) # send data to client

conn.close()



