import socket

def connect_to_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'Hello, server')
        data = s.recv(1024)
    print(f'Received from server: {data.decode()}')

if __name__ == "__main__":
    connect_to_server()
