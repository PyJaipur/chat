import argparse


parser = argparse.ArgumentParser()

parser.add_argument("cmd")
parser.add_argument("--client", default="example")


args = parser.parse_args()

if args.cmd == "client":
    s = "from chat.clients.{args.client} import client_input, show_message"
    exec(s)
    # run client with these functions
else:
    # run server with parse/unparse functions
