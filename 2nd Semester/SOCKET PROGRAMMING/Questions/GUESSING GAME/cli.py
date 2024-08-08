#Question: GUESSING GAME
#Language: Python
#Creation Date: 10-Oct-2021
#Last Modified: 10-Oct-2021
#Question: Description: Develop a server-client guessing game using Python's socket module. The server generates a random number, and the client tries to guess it by sending guesses to the server. The server provides hints (higher or lower) until the client guesses the correct number. This exercise helps in understanding how to handle communication between client and server for interactive games.
#Expected Output: The server should generate a random number and provide hints to the client until the client guesses the correct number.
#This is client file

import socket as st
import random

s = st.socket(st.AF_INET, st.SOCK_STREAM) # create a socket object

s.connect(('localhost', 1234)) # connect to the server
while 1:
    data = input('Choose a random number: ') # input a random number
    s.send(data.encode()) # send the random number to the server

    res = s.recv(1023) # receive data from the server
    print("Server:", res.decode()) # print the data
s.close() # close the connection