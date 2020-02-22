from chat.protocol import parcel
from chat.color import green


def user_input(host, port):
    """
    You need to take input from user and
    send it to the server.

    This needs to be an infinite loop.

    Use
    s.sendall(parcel(message,
    myself=myname,
    to=toname))

    to send messages.
    """
    while True:
        msg = input()
        with socket.socket() as s:
            s.connect((host, port))
            s.sendall(parcel(msg, myself="example"))


def show_message(msg: str, sender: str, myself="example") -> str:
    if sender == myself:
        sender = green(sender)
    return f"{sender:>15}: {msg}"
