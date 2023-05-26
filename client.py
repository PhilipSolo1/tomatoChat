# This is tomatoChat client.
# Written and maintained by @PhilipSolo1 on github

import socket
import random
from threading import Thread
from datetime import datetime

log = open("log.txt", "r+")

# server's IP address
# if the server is not on this machine, 
# put the private (network) IP address (e.g 192.168.1.2)
SERVER_HOST = input("[*] Please Enter IP Adress for tomatoChat: ")
SERVER_PORT = int(input("[*] Please Enter a port  for tomatoChat: ")) # server's port
separator_token = "<SEPTOKEN>" # we will use this to separate the client name & message

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print(f"[*] Connected to {SERVER_HOST}:{SERVER_PORT}")
# prompt the client for a name
name = input("[*] Enter a Username: ")

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print(message)
def send_msg(msginput):
    s.send(msginput.encode())

# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

while True:
    # input message we want to send to the server
    to_send = input()
    # a way to exit the program
    if to_send.lower() == 'q':
        print("[*] Closing Connection...")
        break
    # add the datetime, name & the color of the sender
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"[{date_now}] {name}: {to_send}"
    # finally, send the message
    send_msg(to_send)

# close the socket
s.close()
p = input("Press enter to close...")