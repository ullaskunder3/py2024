import socket

def start_server(host='127.0.0.1', port=65432):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the address and port
        s.bind((host, port))
        print(f"Server started and listening on {host}:{port}")

        # Enable the server to accept connections (backlog of 5)
        s.listen(5)

        while True:
            # Accept a connection from a client
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    # Receive data from the client (buffer size of 1024 bytes)
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received from {addr}: {data.decode()}")
                    
                    # Send a response back to the client
                    response = b"Hello, client"
                    conn.sendall(response)

if __name__ == "__main__":
    start_server()
