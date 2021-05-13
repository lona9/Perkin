from time import time

from . import misc

PREFIX = "!"

cmds = {
    "hola": misc.hola,
    "rank": misc.rank,
}

def process(bot, user, message):
    if message.startswith(PREFIX):
        cmd = message.split(" ")[0][len(PREFIX):]
        args = message.split(" ")[1:]
        perform(bot, user, cmd, *args)

def perform(bot, user, cmd, *args):
    for name, func in cmds.items():
        if cmd == name:
            func(bot, user, *args)
            return
    if cmd == "help":
        misc.help(bot, PREFIX, cmds)

    else:
        bot.send_message(f"{user['name']}, \"{cmd}\" no es un comando registrado.")
