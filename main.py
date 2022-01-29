from sv_bot import SV_Bot

bot = SV_Bot()
bot.run()

cmd = ""
while cmd != 'exit':
    cmd = input('>')
    print(cmd)
