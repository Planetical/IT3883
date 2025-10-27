# Program Name: Assignment4Recieve.py
# Course: IT3883/Section W02
# Student Name: Adam Hutcheson
# Assignment Number: Lab4
# Due Date: 10/26/2025
# Purpose: Create a program that sends a string over a socket, and a second that receives, changes string to uppercase,
# and retransmits

import socket

HOST = '72.195.184.191'
PORT = 40001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()

conn, addr = s.accept()

with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        response = data.decode('utf-8').upper()
        conn.sendall(response.encode('utf-8'))