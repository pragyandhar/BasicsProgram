#Question: Chat Application
#Language: Python
#Creation Date: 10-Oct-2021
#Last Modified: 10-Oct-2021
#Question Description: Implement a basic chat application using Python's socket module where multiple clients can connect to a server and communicate with each other. Clients should be able to send messages to the server, which will broadcast them to all other connected clients. Additional features like joining and leaving notifications can be included to enhance the functionality.
#Expected Output: The server should accept multiple clients and broadcast messages to all connected clients.
#This is client file

import socket as st

s = st.socket(st.AF_INET, st.SOCK_STREAM) # create a socket object

s.connect(('localhost', 1234)) # connect to the server
while 1:
    data = input('Client: ') # input data
    s.send(data.encode()) # send the data to the server

    res = s.recv(1024) # receive data from the server
    print('Server:', res.decode()) # print the data

s.close() # close the connection