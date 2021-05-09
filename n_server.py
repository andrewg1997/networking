# import scoketserver for the server and Fernet for the cryptography
import socketserver
from cryptography.fernet import Fernet

HOST= "localhost"
PORT = 9999
# set key to a random generated key that will stayt the same until the server is terminated
KEY = Fernet.generate_key()
# Create a Fernet object with the key
fernet = Fernet(KEY)

class MyTCPHandler(socketserver.BaseRequestHandler):
    # This is the handle method that we need to write to override the the BaseRequestHandler class's method
    def handle(self):
        global fernet
        global KEY
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote1:".format(self.client_address[0]))
        #print(self.data)

        # Process what the client has sent.
        '''
        We need to grab 2 parts from the string that was sent and throw away 2 parts.
        Each part is seperated by a '#' and so we use split() with the deliminator of '#'.
        We then use an if-else statement to execute the correcnt code for the client.
        '''
        msgDiv = str(self.data.decode()).split("#", 3)
        # This is from testing, but I think it is nice to have 
        message = ("NOTSET").encode()
        if msgDiv[1] == "en":
            message = fernet.encrypt(msgDiv[2].encode())
        elif msgDiv[1] == "de":
            message = fernet.decrypt(msgDiv[2].encode())
        elif msgDiv[1] == "gk":
            message = KEY
        elif msgDiv[1] == "sk":
            KEY = msgDiv[2]
            fernet = Fernet(KEY)
            message = ("[Key has been set]").encode()
        print(message)
        self.request.sendall(message)

def start():
    # Lets tell who ever might be looking at the server console that it is started
    print(f"[STARTING SERVER] on {HOST}")
    # We needed a server class to pass the our IP address, port number and our new handler class (MyTCPHandler)
    # Here we have the socketserver class
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # The server will be open until we press ctr+c or close the terminal. We could also call shutdown() which is a built in method.
        server.serve_forever()

# Our main method where we call start()
# A bit plain, but I plan on adding things later to this program and I think it will scale better leaving it like this
if __name__ == "__main__":
    start()