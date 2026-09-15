#Handling low level socket communication by recieving raw data up to 1024 bytes and converting it to string
def handle_connection(socket, address):
    request = socket.recv(1024).decode()
    return request