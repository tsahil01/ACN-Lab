# Practical no. 4


## Implement socket programming to show the half duplex communication in a single terminal usng three way tcp handshaking protocol.

**Fuctions:**

```py
socket()            # to create socket
bind()              # associate socket with port
listen()            # allows the server machine to get the request from client machine
connect()           # works with client machine to connect server
accept()            # server machine will accept that connection
send()              # send data to server
recv()              # to recve data
close()             # to close connection
```

![img](https://miro.medium.com/v2/resize:fit:543/1*dw4cFoQ2OL2SjybxzU1DHA.jpeg)

```sh
sahil@HP-laptop-15s:/SEM6/ANC/ACN-Lab/prac_4$ python3 clientSocket.py 
HP-laptop-15s
Send your msg: 
Hello from Client
Msg from Server : Hi Client, This is your Server
Send your response: 
Bye
sahil@HP-laptop-15s:/SEM6/ANC/ACN-Lab/prac_4$
```

```sh
sahil@HP-laptop-15s:/SEM6/ANC/ACN-Lab/prac_4$ python3 serverSocket.py 
HP-laptop-15s
Connection from: ('127.0.0.1', 38230)
Msg from Client : Hello from Client
Send your response: 
Hi Client, This is your Server
sahil@HP-laptop-15s:/SEM6/ANC/ACN-Lab/prac_4$
```