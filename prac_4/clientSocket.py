import socket

client_socket = socket.socket()

hostname = socket.gethostname()
print(hostname)

ipAddr = socket.gethostbyname(hostname) # gets the ipAddr using the hostname like "www.google.com"
# print(ipAddr)

port = 5001

client_socket.connect((ipAddr, port)) 

msg = input('Send your msg: \n') # take input

while msg.lower().strip() != "bye":
    client_socket.send(msg.encode()) # send msg
    data = client_socket.recv(1024).decode()

    print("Msg from Server : "+ data)

    msg = input('Send your response: \n')

client_socket.close()
