#Question: Chat Application
#Language: Python
#Creation Date: 10-Oct-2021
#Last Modified: 10-Oct-2021
#Question Description: Implement a basic chat application using Python's socket module where multiple clients can connect to a server and communicate with each other. Clients should be able to send messages to the server, which will broadcast them to all other connected clients. Additional features like joining and leaving notifications can be included to enhance the functionality.
#Expected Output: The server should accept multiple clients and broadcast messages to all connected clients.
#This is server file

import socket as st

s = st.socket(st.AF_INET, st.SOCK_STREAM) # create a socket object

s.bind(('localhost', 1234)) # bind the socket to the address and port

s.listen(5) # listen for incoming connections
print('Server is waiting for connections...')

client, addr = s.accept() # accept the connection
print('Connection established')

while True:
    data = client.recv(1024) # receive data from the client
    print('Client:', data.decode()) # print the data
    res = input('Server: ') # input data
    client.send(res.encode()) # send the data to the client

client.close() # close the connection