# Question: ECHO SERVER
# Language: Python
# Creation Date: 10-Oct-2021
# Last Modified: 10-Oct-2021
# Question description: Create a simple server using Python's socket module that echoes back any message received from a client. Upon connection, the server should accept messages from the client and send the same message back to the client. This is a fundamental exercise to understand the basic communication between a client and a server using sockets.
# Expected Output: The server should echo back any message received from the client.

import socket as st

s = st.socket(st.AF_INET, st.SOCK_STREAM)

s.connect(('localhost', 1234))

data = input('Client: ')
s.send(data.encode())

res = s.recv(1024)
print('Server:', res.decode())
s.close()