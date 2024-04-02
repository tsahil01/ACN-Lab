import socket
import threading

def receive_messages(conn):
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print('Msg from Client:', data)
        except socket.error as e:
            print("Error receiving data:", e)
            break

def send_messages(conn):
    while True:
        try:
            msg = input('Send your msg:\n')
            conn.send(msg.encode())
            if msg.lower().strip() == "bye":
                break
        except socket.error as e:
            print("Error sending data:", e)
            break

def main():
    server_socket = socket.socket()

    hostname = socket.gethostname()
    print('Server hostname:', hostname)

    ipAddr = socket.gethostbyname(hostname)
    port = 5001

    server_socket.bind((hostname, port))
    server_socket.listen(2)

    print('Server listening on', ipAddr, 'port', port)

    conn, addr = server_socket.accept()
    print('Connected to:', addr)

    receive_thread = threading.Thread(target=receive_messages, args=(conn,))
    send_thread = threading.Thread(target=send_messages, args=(conn,))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
