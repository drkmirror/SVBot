import textwrap


def format_chat_msg(name, msg, name_width=20, chat_width=90, prefix="[    ]"):
    name = name[:name_width]
    name = f"{prefix}{name.rjust(name_width)} : "
    indent = len(name)
    pad = " " * (indent - 3)
    msg = textwrap.wrap(msg, chat_width - indent)

    for index, item in enumerate(msg):
        if index > 0:
            msg[index] = f"{pad}   {msg[index]}"
    msg = "\n".join(msg)
    return (f"{name}{msg}")


class Buffered_Log:
    def __init__(self, flush_interval_i=30):
        self.buffer = []
        self.flush_interval = flush_interval_i

    def add(self, what):
        self.buffer.append(what)
        if len(self.buffer) > self.flush_interval:
            self.flushbuffer()

    def flushbuffer(self):
        for line in self.buffer:
            with open("history", 'a') as f:
                f.write("\n".join(self.buffer) + '\n')
                self.buffer.clear()
