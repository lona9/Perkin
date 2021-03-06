
"""
COPYRIGHT INFORMATION
---------------------

Some code in this file is licensed under the Apache License, Version 2.0.
    http://aws.amazon.com/apache2.0/

"""

from irc.bot import SingleServerIRCBot
from requests import get

from lib import cmds

NAME = "pececitobot"
OWNER = "blvebetta"

class Bot(SingleServerIRCBot):
    def __init__(self):
        self.HOST = "irc.chat.twitch.tv"
        self.PORT = 6667
        self.USERNAME = NAME.lower()
        self.CLIENT_ID = "csfc7k2i8fp1lkptj5b1nwms98bcfq"
        self.TOKEN = "wi2su1arv0nm50oggrigvu039uqbpy"
        self.CHANNEL = f"#{OWNER}"

        url = f"https://api.twitch.tv/kraken/users?login={self.USERNAME}"
        headers = {"Client-ID": self.CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json"}
        resp = get(url, headers=headers).json()
        self.channel_id = resp["users"][0]["_id"]

        super().__init__([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")], self.USERNAME, self.USERNAME)

    def on_welcome(self, cxn, event):
        print("starting on welcome")
        for req in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")
            cxn.join(self.CHANNEL)

        self.send_message("Conectado!")
        print("conectado!")

    def on_pubmsg(self, cxn, event):
        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        user = {"name": tags["display-name"], "id": tags["user-id"]}
        message = event.arguments[0]

        cmds.process(bot, user, message)

    def send_message(self, message):
        self.connection.privmsg(self.CHANNEL, message)

if __name__ == "__main__":
    bot = Bot()
    bot.start()
