# Question: ECHO SERVER
# Language: Python
# Creation Date: 10-Oct-2021
# Last Modified: 10-Oct-2021
# Question description: Create a simple server using Python's socket module that echoes back any message received from a client. Upon connection, the server should accept messages from the client and send the same message back to the client. This is a fundamental exercise to understand the basic communication between a client and a server using sockets.
# Expected Output: The server should echo back any message received from the client.

import socket as st

s = st.socket(st.AF_INET, st.SOCK_STREAM)

address = ('localhost', 1234)
s.bind(address) # undesirable port number: 0-1024 (reserved ports)

s.listen(1)
while 1: 
    client, addr = s.accept()
    print('Connection Estabilished', addr)
    data = client.recv(1024)
    print('Client:', data)
    client.send(data)
    print('Echo Sent')
    client.close()