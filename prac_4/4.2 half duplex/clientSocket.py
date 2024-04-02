import socket

client_socket = socket.socket()
hostname = socket.gethostname()
print(hostname)

ipAddr = socket.gethostbyname(hostname) 
port = 5002

client_socket.connect((ipAddr, port)) 
msg = input('Send your msg: \n') # take input

while msg.lower().strip() != "bye":
    client_socket.send(msg.encode()) # send msg
    data = client_socket.recv(1024).decode()

    print("Msg from Server : "+ data)
    msg = input('Send your response: \n')

client_socket.close()



