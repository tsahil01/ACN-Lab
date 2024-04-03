import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print('Msg from Server:', data)
        except socket.error as e:
            print("Error receiving data:", e)
            break

def send_messages(client_socket):
    while True:
        try:
            msg = input('Send your msg (type "bye" to quit):\n')
            client_socket.send(msg.encode())
            if msg.lower().strip() == "bye":
                break
        except socket.error as e:
            print("Error sending data:", e)
            break

def main():
    server_ip = "192.168.226.13"  # Replace with the server's IP address
    port = 5001

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, port))
        print("Connected to server.")

        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        send_thread = threading.Thread(target=send_messages, args=(client_socket,))

        receive_thread.start()
        send_thread.start()

        receive_thread.join()
        send_thread.join()

        client_socket.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
