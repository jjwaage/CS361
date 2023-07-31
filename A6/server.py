import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '127.0.0.1'  # Replace with your server's IP address if necessary
    server_port = 12345       # Choose a port number (make sure it's not in use)

    server_socket.bind((server_host, server_port))
    server_socket.listen(1)  # Allow only one connection

    print("Server listening on {}:{}".format(server_host, server_port))

    while True:
        conn, addr = server_socket.accept()
        print("Connected to client at {}:{}".format(addr[0], addr[1]))
        message = "A message from CS361"
        conn.sendall(message.encode())
        conn.close()

if __name__ == "__main__":
    start_server()
