import socket

server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_client.connect(('localhost', 3254))

data = server_client.recv(1024)

print('Server:',data.decode())

server_client.close()