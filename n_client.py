import socket
import sys

HOST, PORT = "localhost", 9999

# ----------- This is option one for the user interface ---------#
# Uncomment this if you want to use arguments form the command line. You will need to comment the while loop below as well.

rtype = sys.argv[1]
msg = " ".join(sys.argv[2:])
if  not (rtype == 'en' or rtype == 'de' or rtype == 'gk'):
    print("Wrong arguments. Correct arguments: 'en' for encrypt, 'de' for decrypt, or 'gk' for get key")

'''
# --------- This is option two for the user interface ----------#
# Comment this while loop if you want the command line to take arguments
is_valid = False
while not is_valid:
    print("Please enter 'en' for encrypt, 'de' for decrypt or 'gk' to get the key: ")
    rtype = input()
    if rtype == 'en':
        print("Please enter a message for the server to encrypt: ")
        msg = input()
        is_valid = True
    elif rtype == 'de':
        print("Please enter a message for the server to decrypt: ")
        msg = input()
        is_valid = True
    elif rtype == 'gk':
        msg = ''
        is_valid = True
'''

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Make a socket connection to our server. This socket will terminate at the end of the program.
    sock.connect((HOST, PORT))
    # We use sendall() to send everything to the server. We will need to convert it to utf-8 first
    # We also add our '#' in order for the server to process the requests and message
    sock.sendall(bytes('#' + rtype + '#' + msg + '#' + "\n", "utf-8"))
    # Receive data from the server
    received = str(sock.recv(1024))

# Print what we sent and what we recieved
print("Sent: ", msg)
print("Received: ", received)