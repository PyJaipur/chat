import socket
import time
from chat.protocol import unparcel


def build_client(name, host="localhost", port=8888):
    g = {}
    exec(f"from chat.clients.{name} import user_input, show_message", g)

    def watch_client():
        with socket.socket() as sock:
            sock.connect((host, port))
            msg = None
            while True:
                data = sock.recv(4096)
                if not data:
                    print(g["show_message"](**unparcel(msg)))
                    msg = None
                    time.sleep(1)
                msg = data if msg is None else msg + data

    def input_client():
        g["user_input"](host, port)

    return input_client, watch_client
