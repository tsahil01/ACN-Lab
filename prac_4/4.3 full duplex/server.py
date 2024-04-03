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
            broadcast(data.encode(), conn)
    except Exception as e:
        print("Error handling client {}: {}".format(addr, e))

    print('Disconnected from:', addr)
    conn.close()
    remove_connection(conn)

def broadcast(message, sender_conn):
    for client_conn in clients:
        if client_conn != sender_conn:  # Don't send the message back to the sender
            try:
                client_conn.sendall(message)
            except:
                remove_connection(client_conn)

def remove_connection(conn):
    if conn in clients:
        clients.remove(conn)

def send_server_message(message):
    for client_conn in clients:
        try:
            client_conn.sendall(message.encode())
        except:
            remove_connection(client_conn)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    hostname = socket.gethostname()
    ipAddr = "192.168.226.13"
    port = 5003

    server_socket.bind((ipAddr, port))
    server_socket.listen(5)  # Increase the queue size for more clients

    print('Server listening on', ipAddr, 'port', port)

    try:
        while True:
            conn, addr = server_socket.accept()
            clients.append(conn)
            client_handler = threading.Thread(target=handle_client, args=(conn, addr))
            client_handler.start()

            # Start a new thread to handle server messages
            server_thread = threading.Thread(target=send_server_message, args=("Welcome to the chat room!",))
            server_thread.start()

            # Allow server to send messages
            server_input_thread = threading.Thread(target=send_server_input)
            server_input_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()

def send_server_input():
    while True:
        try:
            msg = input("Server: ")  # Server inputs its message here
            if msg.lower().strip() == "exit":  # To exit server input
                break
            send_server_message(msg)
        except Exception as e:
            print("Error sending server message:", e)

if __name__ == "__main__":
    clients = []
    main()
