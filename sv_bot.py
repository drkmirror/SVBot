import os
from twitchio.ext import commands
from utilities import format_chat_msg


def secret(what, prefix='TWITCH_BOT_'):
    return os.environ[prefix + what]


class SV_Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=secret('TOKEN'),
                         prefix='!',
                         initial_channels=['#drkmirror'])

    async def event_ready(self):
        print(
            format_chat_msg("", f'Logged in as: {self.nick}', prefix="[>>>>]"))

    async def event_usernotice_subscription(metadata):
        print("sub event", metadata.user, metadata.channel)

    async def event_command_error(self, ctx, error):
        print(
            format_chat_msg(f'<ERROR>',
                            f'{error} from {ctx.message.author.name}',
                            prefix="<Error>"))

    async def event_message(self, message):
        if message.echo:
            return
        pre = ['[', ' ', ' ', ' ', ' ', ']']

        if message.author.is_subscriber: pre[2] = '*'
        if message.author.is_mod: pre[1] = '+'
        pre = "".join(pre)

        msg = message.content

        if msg.find('ACTION') == 1:
            msg = msg.replace("ACTION", message.author.name)

            print(format_chat_msg(" ", msg, prefix=pre))
        else:

            print(format_chat_msg(message.author.name, msg, prefix=pre))

        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name

        msg = f'Hello {ctx.author.name}!'
        print(format_chat_msg(self.nick, msg, prefix='[>>>>]'))

        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(msg)
