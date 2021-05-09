# Overview

I wrote a small networking programming using python. I wrote it in ordr to try to get a better understanding of how servers and the internet work and to learn the programming side of servers.

The program I wrote it very basic. I made a server program to connect to a client. I didn't know what I wanted it to do and so I had it use AES encryption to encrypt and decrypt the messages a client would send to it. The server then would reply with the encrypted or decrypted message.

To start the server, all you need to do is start it. I just started it in VS code, but you can also start it from the command line. The client can't be started in VS code while another programming is running in VS code and so I used the command line for it.

For the client, you have commented out code that you can uncomment and comment out another piece to switch which interface you want. You can pass arguments through the command prompt when you call the program or have the program start and enter the two arguments seperatly when prompted. The second option is more user friendly. The instructions are found in comments in the client code.

[Software Demo Video](https://youtu.be/4dzZSuxMPF8)

# Network Communication

This is a client/server achitecture. I used TCP because it is more reliable. I used port 8000.

The format of the messages are: b'#en#message#'
The b' ... ' is added on with encoding and I added the #s so I could have a delimiter to seperate it out.
The 'en' is for encrypt (tells the server to encrypt the message) and you can enter 'de' for decrypt or 'gk' for get key in its place.
The message is the message to encrypt/decrypt and can be left blank when you are useing 'gk'

The ends are not used (b' ... ').

# Development Environment

{Describe the tools that you used to develop the software}
* I used Visual Studios Code for the IDE.
* I used Python for the language.

#### Libraries
* I used socketserver to build the server part.
* I used the Fernet library for the cryptography.

# Useful Websites

* [Python.org - socketserver](https://docs.python.org/3.6/library/socketserver.html)
* [Python.org - sockets](https://docs.python.org/3.6/library/socket.html)
* [YouTube.com - Simple Python Webserver](https://www.youtube.com/watch?v=hFNZ6kdBgO0)
* [geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/)
* [howtogeek.com](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
* [wikipedia.org](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)


# Future Work

* RSA encryption instead of AES.
* Better user interface, but still keep a terminal option.
* Have the server do more, like transfer files.