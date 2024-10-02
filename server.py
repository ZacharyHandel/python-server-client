import socket

# Server setup
def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Accept a connection from the client
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        # Receive data from the client
        data = conn.recv(1024)
        if not data:
            break  # Exit if no data is received

        # Print received data
        print(f"Received from client: {data.decode()}")

        # Echo back the data to the client
        conn.sendall(data)

    # Close the connection
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
