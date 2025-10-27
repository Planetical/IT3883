# Program Name: Assignment4Send.py
# Course: IT3883/Section W02
# Student Name: Adam Hutcheson
# Assignment Number: Lab4
# Due Date: 10/26/2025
# Purpose: Create a program that sends a string over a socket, and a second that receives, changes string to uppercase,
# and retransmits

import socket

HOST = '72.195.184.191'
PORT = 40001

# we are using ipv4 (af_inet) and TCP (sock_stream)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # taking in and sending data
    message = input('Enter a message: ')
    s.sendall(message.encode('utf-8'))

    # waiting for response
    data = s.recv(1024)

    print(data)
