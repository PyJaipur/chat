import argparse
from threading import Thread


parser = argparse.ArgumentParser()

parser.add_argument("cmd")
parser.add_argument("--client", default="example")


args = parser.parse_args()

if args.cmd == "watch":
    from chat.client import build_client

    _, watch_client = build_client(args.client)
    watch_client()
elif args.cmd == "type":
    from chat.client import build_client

    input_client, _ = build_client(args.client)
    input_client()
else:
    from chat.server import gateway, incoming, publish

    threads = [Thread(target=incoming), Thread(target=publish)]
    for t in threads:
        t.start()
    gateway()
