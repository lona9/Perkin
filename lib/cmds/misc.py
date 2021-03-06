import requests
from bs4 import BeautifulSoup

def help(bot, prefix, cmds):
    bot.send_message("Comandos registrados: " + ", ".join([f"{prefix}{cmd}" for cmd in sorted(cmds.keys())]))

def hola(bot, user, *args):
    bot.send_message(f"Hola, {user['name']}!")

def check(bot, user, *args):
    bot.send_message("¡Aquí estoy!")

def shoutout(bot, user, *args):
    args = str(args[0])
    print(args)
    link = str(args[1:])
    print(link)
    bot.send_message(f"sigan a @{link}!!! twitch.tv/{link}")

def social(bot, user, *args):
  bot.send_message("Tik Tok: @blvebetta")

def aery(bot, user, *args):
  bot.send_message("Puedes invitar a Aery a tu server de Discord con el siguiente link: https://discord.com/oauth2/authorize?client_id=804475973579833374&permissions=1074121728&scope=bot")

def rank(bot, user, *args):
    if args == ():
        bot.send_message("Debes escribir un nombre de usuario válido para usar este comando.")

    else:
        username = str("".join(args))
        url = f"https://las.op.gg/summoner/userName={username}"
        response = requests.get(url)
        code = response.content

        soup = BeautifulSoup(code, features='html5lib')
        try:
            rank = soup.find('div', attrs="TierRank").contents[0]
            lp = soup.find('span', attrs="LeaguePoints").contents[0]
            lp = lp.replace("\n", "")
            lp = lp.replace("\t", "")

            winlose = soup.find('span', attrs="winratio").contents[0]

            final_str = rank + ' // ' + lp + ' // ' + winlose

            bot.send_message(final_str)

        except:
            bot.send_message("No existe ese usuario o no tiene nivel de clasificatoria.")
