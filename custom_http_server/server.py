import socket
import multiprocessing

# Function to handle client requests
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    data = conn.recv(1024)
    if data:
        response = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello from your custom server!"
        conn.sendall(response)
    conn.close()

# Define host and port
HOST = '127.0.0.1'
PORT = 8080

# Create the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Server started on {HOST}:{PORT}...")

    while True:
        # Accept a connection from the client
        conn, addr = s.accept()
        # Start a new process to handle the client
        process = multiprocessing.Process(target=handle_client, args=(conn, addr))
        process.start()



