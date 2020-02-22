def parcel(msg, *, myself, to="common"):
    return f"{myself}\n{to}\n{msg}".encode()


def unparcel(data):
    strings = data.decode()
    sender, myself, *msg_lines = data.decode().split("\n")
    return dict(sender=sender, myself=myself, msg="\n".join(msg_lines))
