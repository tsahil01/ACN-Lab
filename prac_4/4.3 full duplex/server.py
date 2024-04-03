import socket
import threading

def handle_client(conn, addr):
    print('Connected to:', addr)

    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print('Msg from Client {}: {}'.format(addr, data))
            if data.lower().strip() == "bye":
                break
            conn.sendall("Message received".encode())
    except Exception as e:
        print("Error handling client {}: {}".format(addr, e))

    print('Disconnected from:', addr)
    conn.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    hostname = socket.gethostname()
    ipAddr = "192.168.226.13"
    port = 5002

    server_socket.bind((ipAddr, port))
    server_socket.listen(2)  # Allow up to 2 clients to wait in the queue

    print('Server listening on', ipAddr, 'port', port)

    try:
        while True:
            conn, addr = server_socket.accept()
            client_handler = threading.Thread(target=handle_client, args=(conn, addr))
            client_handler.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
