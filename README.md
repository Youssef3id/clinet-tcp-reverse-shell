Simple Client-Server Communication in Python

This project demonstrates a basic client-server communication setup using Python's socket module. The server listens for incoming connections and the client connects to the server. Commands can be sent from the server to the client, and the client responds back.
Files

    server.py: Contains the server code.
    client.py: Contains the client code.

Prerequisites

    Python 3.x

How to Run
Step 1: Run the Server

    Open a terminal window.

    Navigate to the directory where server.py is located.

    Run the server script using the command:

    bash

python server.py

You should see the output:

arduino

    Server is listening...

Step 2: Run the Client

    Open another terminal window.

    Navigate to the directory where client.py is located.

    Run the client script using the command:

    bash

python client.py

The client will connect to the server, and you should see the output:

yaml

    Command received: 

Usage

    After starting both the server and the client, you can send commands from the server to the client.

    In the server terminal, type a command and press Enter. For example:

    markdown

> hello

The client will receive the command and you will be prompted to enter a response. For example:

yaml

    Command received: hello
    Response:

    Type the response and press Enter. The server will display the client's response.

    To exit, type exit in the server terminal.

Example
Server Terminal

vbnet

Server is listening...
Connection established with: ('127.0.0.1', 53744)
> hello
hello
> exit

Client Terminal

yaml

Command received: hello
Response: hi there

Troubleshooting

    Ensure both the server and client scripts are running on the same machine or within the same network.
    If running on different machines, replace '127.0.0.1' in the client code with the server's IP address.
    Ensure no firewall or network settings are blocking the connection.

