import socket
from connection import handle_connection
from response import response

server_host = '0.0.0.0'
server_port = 5000

# Initialize an IPv4 TCP socket and allow address reuse
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Binding the server to a host and port, then allowing up to 5 pending connections in the connection queue
server_socket.bind((server_host, server_port))
server_socket.listen(5)
print(f'Listening on port {server_port}')

#Client socket will be used to send and recieve data to the connection that we accepted through the server socket
while True:
    client_socket, client_address = server_socket.accept()
    req = handle_connection(client_socket, client_address)
    res = response(req)
    print(req)
    print(res)
    client_socket.sendall(res.encode())
    client_socket.close()