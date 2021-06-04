from . import misc
from . import random
from time import time

PREFIX = "&"

class Cmd(object):
    def __init__(self, callables, func, cooldown=0):
        self.callables = callables
        self.func = func
        self.cooldown = cooldown
        self.next_use = time()


cmds = [
    Cmd(["hola", "hi", "hello"], misc.hola, cooldown=0),
    Cmd(["rank", "ranking"], misc.rank, cooldown=0),
    Cmd(["rrss", "social"], misc.social, cooldown=0),
    Cmd(["rol"], random.rol, cooldown=0),
    Cmd(["jg"], random.jg, cooldown=0),
    Cmd(["mid"], random.mid, cooldown=0),
    Cmd(["top"], random.top, cooldown=0),
    Cmd(["supp"], random.supp, cooldown=0),
    Cmd(["adc"], random.adc, cooldown=0),
    Cmd(["suerte", "8ball"], random.suerte, cooldown=0),
    Cmd(["check"], misc.check, cooldown=0),
    Cmd(["so", "shoutout"], misc.shoutout, cooldown=0),
    Cmd(["aery"], misc.aery, cooldown=0)
]

def process(bot, user, message):
    if message.startswith(PREFIX):
        cmd = message.split(" ")[0][len(PREFIX):]
        args = message.split(" ")[1:]
        perform(bot, user, cmd, *args)

def perform(bot, user, call, *args):
    if call in ("help", "commands", "cmds"):
        misc.help(bot, PREFIX, cmds)

    else:
        for cmd in cmds:
            if call in cmd.callables:
                if time() > cmd.next_use:
                    cmd.func(bot, user, *args)
                    cmd.next_use = time() + cmd.cooldown

                    return

                else:
                    bot.send_message(f"el comando está en cooldown, intenta de nuevo en unos segundos.")
                    return

        bot.send_message(f"{user['name']}, \"{call}\" no está registrado como comando.")
