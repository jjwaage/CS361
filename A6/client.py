import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '127.0.0.1'  # Replace with the server's IP address
    server_port = 12345       # Use the same port number as in the server

    try:
        client_socket.connect((server_host, server_port))
        message = client_socket.recv(1024).decode()
        print("Received message from server:", message)
    except ConnectionRefusedError:
        print("Server is not available.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
