import socket
from queue import Queue
from chat.protocol import unparcel

msg_queue = Queue()
clients = []


def gateway(host: str = "0.0.0.0", port: int = 8888, max_clients_pending: int = 10):
    with socket.socket() as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(max_clients_pending)
        while True:
            conn, addr = sock.accept()
            clients.append((conn, addr))


def incoming():
    global msg_queue, clients
    while True:
        for conn, addr in list(clients):
            msg = None
            while True:
                try:
                    data = conn.recv(4096)
                except socket.error as e:
                    err = e.args[0]
                    if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                        break
                    else:
                        raise
                else:
                    msg = data if msg is None else msg + data
            msg_queue.put(msg)


def publish():
    global msg_queue, clients
    while True:
        msg = msg_queue.get()
        surviving_clients = []
        for conn, addr in list(clients):
            try:
                conn.sendall(msg)
            except socket.timeout:
                continue
            else:
                surviving_clients.append((conn, addr))
        clients = surviving_clients
