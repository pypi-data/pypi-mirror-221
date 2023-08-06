# Reverse shell server for unbureaucratic server/client connections with file transfer / screenshots 

## pip install reverseshellserver 

#### Tested against Windows 10 / Python 3.10 / Anaconda 

Shell Server: A simple server-side application that allows multiple clients to connect, execute shell-like commands,
taking screenshots, and exchange files over a network using sockets.

To install the client: https://pypi.org/project/reverseshellclient/

This server application implements a basic command shell that listens for client connections, executes user commands,
and responds to the client with appropriate outputs or actions.
Clients can connect to the server using a TCP/IP socket

The server and client communicate using a custom command encoding format to handle large data transmissions.
The server can send data to the client, and the client can send data to the server.


Usage:
1. Instantiate the ShellServer class with desired configurations (port, buffer size, commands, etc.).
2. Start the server using the `do_actions()` method, which listens for incoming client connections and allows communication with clients.
3. Clients can connect to the server using a TCP/IP socket.

Note:
- The server can handle multiple clients simultaneously through multi-threading.
- When a client sends the 'quit' command, the client remains connected.
- When a client sends the 'exit' command, the client is disconnected from the server.
- The server supports the 'putfile' and 'getfile' commands to send and receive files between the server and clients.
- Screenshots can be taken using command_screenshot

```python

from reverseshellserver import ShellServer
se = ShellServer(
    port=12345,
    listen=5,
    byte_len=32768,
    command_quit="quit",
    command_disconnect="disconnect",
    command_exit="exit",
    command_putfile="putfile",
    command_getfile="getfile",
    command_screenshot="screenshot",
    command_getcwd="getcwd",
    command_putfile_sep=b"FILESEP",
    command_start=b"START_START_START",
    command_end=b"END_END_END",
)
se.do_actions()
		
```