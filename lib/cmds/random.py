import random

def rol(bot, user, *args):
  roles = ["jungla", "adc", "supp", "top", "mid"]

  bot.send_message(f"Te toca jugar: {random.choice(roles)}")

def jg(bot, user, *args):
  jg = ["Amumu", "Dr. Mundo", "Ekko", "Elise", "Evelynn", "Fiddlesticks", "Gragas", "Graves", "Hecarim", "Ivern", "Jarvan IV", "Jax", "Karthus", "Kayn", "Kha'Zix", "Kindred", "Kled", "Lee Sin", "Lillia", "Maestro Yi", "Nidalee", "Nocturne", "Nunu", "Olaf", "Rammus", "Rek'Sai", "Rengar", "Sejuani", "Sett", "Shaco", "Shyvana", "Skarner", "Sylas", "Taliyah", "Trundle", "Udyr", "Vi", "Viego", "Volibear", "Warwick", "Wukong", "Xin Zhao", "Zac"]

  bot.send_message(f"Te toca jugar jungla con: {random.choice(jg)}")

def supp(bot, user, *args):
  supp = ["Alistar", "Bardo", "Blitzcrank", "Brand", "Braum", "Galio", "Janna", "Karma", "Leona", "Lulu", "Lux", "Malphite", "Maokai", "Morgana", "Nami", "Nautilus", "Pantheon", "Pyke", "Rakan", "Senna", "Sett", "Shaco", "Shen", "Sona", "Soraka", "Swain", "Tahm Kench", "Taric", "Thresh", "Vel'Koz", "Xerath", "Yuumi", "Zac", "Zilean", "Zyra"]

  bot.send_message(f"Te toca jugar support con: {random.choice(supp)}")

def adc(bot, user, *args):
  adc = ["Aphelios", "Ashe", "Caitlyn", "Cassiopeia", "Draven", "Ezreal", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Kog'Maw", "Lucian", "Miss Fortune", "Senna", "Sivir", "Tristana", "Twitch", "Varus", "Vayne", "Xayah", "Yasuo"]

  bot.send_message(f"Te toca jugar ADC con: {random.choice(adc)}")

def top(bot, user, *args):
  top = ["Aatrox", "Akali", "Camille", "Cho'Gath", "Darius", "Dr. Mundo", "Fiora", "Gangplank", "Garen", "Gnar", "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Jax", "Jayce", "Karma", "Kayle", "Kennen", "Kled", "Lillia", "Malphite", "Maokai", "Mordekaiser", "Nasus", "Nocturne", "Olaf", "Ornn", "Pantheon", "Poppy", "Quinn", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Sett", "Shen", "Singed", "Sion", "Sylas", "Teemo", "Tryndamere", "Urgot", "Vayne", "Vladimir", "Volibear", "Wukong", "Yorick", "Zac"]

  bot.send_message(f"Te toca jugar top con: {random.choice(top)}")

def mid(bot, user, *args):
  mid = ["Aatrox", "Ahri", "Akali", "Anivia", "Annie", "Aurelion Sol", "Azir", "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Diana", "Ekko", "Fizz", "Galio", "Garen", "Heimerdinger", "Irelia", "Ivern", "Jayce", "Kassadin", "Katarina", "LeBlanc", "Lillia", "Lissandra", "Lucian", "Lux", "Malphite", "Malzahar", "Neeko", "Nocturne", "Nunu", "Orianna", "Pantheon", "Qiyana", "Renekton", "Rumble", "Ryze", "Swain", "Sylas", "Syndra", "Talon", "Twisted Fate", "Veigar", "Vel'Koz", "Viktor", "Vladimir", "Xerath", "Yasuo", "Zed", "Ziggs", "Zilean", "Zoe"]

  bot.send_message(f"Te toca jugar mid con: {random.choice(mid)}")

def suerte(bot, user, *args):
    suerte = ["yeah", "no", "don't bet on it", "ja", "no.", "ken sabe realmente", "aaaAª secreto", "paciencia chiquite", "puede ser que si, puede ser que no", "no sé si te gustaría saber", "difícil oye", "mis fuentes dicen que sí", "lo que diga tu corazón", "eso no se pregunta", "quizá", "puaj", "nononoooo", "*música de circo*", "malaya", "a perder!", "a manquear!", "yiaaaaaaa shao shao", "pero qué pasa poto loco?", "hay que ser positivxs menos para el cobik", "ff15", "/surrender", "remake o me electrocuto"]
    if args == ():
        bot.send_message("Debes escribir una pregunta antes!")
    else:
        bot.send_message(random.choice(suerte))
