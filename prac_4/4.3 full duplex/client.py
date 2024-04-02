import socket

client_socket = socket.socket()
hostname = socket.gethostname()
print(hostname)

ipAddr = socket.gethostbyname(hostname)
port = 5002

client_socket.connect((ipAddr, port))

while True:
    msg = input('Send your msg: \n')  # take input
    client_socket.send(msg.encode())  # send msg

    # Receive server's response
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print("Msg from Server : " + data)

    # If the sent message is "bye", break the loop
    if msg.lower().strip() == "bye":
        break

client_socket.close()
