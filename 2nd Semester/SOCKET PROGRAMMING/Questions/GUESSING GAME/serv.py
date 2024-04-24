#Question: GUESSING GAME
#Language: Python
#Creation Date: 10-Oct-2021
#Last Modified: 10-Oct-2021
#Question: Description: Develop a server-client guessing game using Python's socket module. The server generates a random number, and the client tries to guess it by sending guesses to the server. The server provides hints (higher or lower) until the client guesses the correct number. This exercise helps in understanding how to handle communication between client and server for interactive games.
#Expected Output: The server should generate a random number and provide hints to the client until the client guesses the correct number.
#This is server file

import socket as st
import random

s = st.socket(st.AF_INET, st.SOCK_STREAM) # create a socket object

address = ('localhost', 1234) # address of the server

s.bind(address) # undesirable port number: 0-1024 (reserved ports)

s.listen(1) # number of clients that can connect to the server

num = random.randint(1, 100) # random number between 1 and 100

while 1:
    client, addr = s.accept() # accept the connection
    print('Connection Estabilished', addr) # print the address of the client
    while 1: # infinite loop
        data = client.recv(1024).decode() # receive data from the client
        data = int(data) # convert the data to integer
        print('Client:', data) # print the data
        if data == num: # if the data is equal to the random number
            client.send(b'Correct!') # send 'Correct!' to the client
            print('Correct!') # print 'Correct!'
            break # break the loop
        elif data < num: # if the data is less than the random number
            client.send(b'Higher') # send 'Higher' to the client
            print('Higher') # print 'Higher'
        else: # if the data is greater than the random number
            client.send(b'Lower') # send 'Lower' to the client
            print('Lower') # print 'Lower'
    client.close() # close the connection