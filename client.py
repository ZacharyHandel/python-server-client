import socket

# Client setup
def start_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        # Send data to the server
        while True:
            message = input("Enter message to send to server (type 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode())

            # Receive echo from the server
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
