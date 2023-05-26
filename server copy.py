# DO NOT USE

import socket
from threading import Thread
import json
import random

# variables
_debug = False
max_connected = 0


# server's IP address and port
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002
separator_token = "<SEP>"

# initialize list/set of all connected client's sockets
client_sockets = set()
# create a TCP socket
s = socket.socket()
# make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
s.bind((SERVER_HOST, SERVER_PORT))
# listen for upcoming connections
s.listen(5)
print(f"[-] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
    while True:
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error! Did the client disconnect or crash?")
            if _debug:
                print(f"[!] Error:\n{e}")
            else:
                print("[-] Debug mode disabled, not printing error.")
            print(f"[-] Removing client from connection.")
            client_sockets.remove(cs)
        else:
            try:
                msg = json.loads(msg)
            except Exception as e:
                print("[!] Client sent a unrecognized message. Is the client outdated?")
                if _debug:
                    print(f"Error:\n{e}")
                else:
                    print("[-] Debug mode disabled, not printing error.")
            if msg["mode"] == "1":
                msgf = '{"mode":"2", "allowed":"true", "uid":"' + random.randint(1000,9999) + '"}'
            elif msg["mode"] == "3":
                pass
            elif 
        # iterate over all connected sockets
        for client_socket in client_sockets:
            # and send the message
            client_socket.send(msgf.encode())


while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} {client_username} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()

# close client sockets
print("[-] Server stopping...")
for cs in client_sockets:
    cs.close()
# close server socket
s.close()