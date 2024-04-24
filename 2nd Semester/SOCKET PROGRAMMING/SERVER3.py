import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 10000))

server_socket.listen(5)
print('Server is listening...')
client, addr = server_socket.accept()
print('Connection from:', addr)
server_socket.send('Welcome to GlA University'.encode())

server_socket.close()