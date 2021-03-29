import time
import os
import time
try:
    import discord
    import datetime #!
    import yaml
    from discord.ext import commands
except:
    os.system("start installpackages.py\nstart bot5.py")
    exit()
punkty = []
global osoby
global messagesslownik
messagesslownik = []
osoby = []
ilosc = []
client = commandclient = commands.Bot(command_prefix = '-')
#--------
if os.path.isfile("config.yml") == False:
    print("Creating config file in your file location!")
    cfg = open("config.yml", 'w')
    cfg.write("#Welcome to the config! Please read every line about config lines, because editing something wrong can harm this program!\n\n\n#Put your discord token bot right here:\nTOKEN: \"\"\n\n#Please here put your channel list. Each channel you should put in layout\"- ID\" every each line.\nIDs:\n - FirstID\n\n\n#Please put here your emoji. Format: <:emoji:emoji_id>\nemoji: \"<>\"\n\nautorun: False #Provide True if you want to check run by auto. When False, most of settings above DON'T MATTER. You provide them using command.\noffline: False #Should bot be marked as Offline or Online (in status). Writing True will turn it to offline. Anything else will disable this.\n###################\n#Credit by heyngra#\n###################")
    cfg.close()
    print("Done!\nPlease, now fill the configuration file with things and start this program again!")
    time.sleep(3)
    exit()
elif os.path.isfile("config.yml") == True:
    global TOKEN, ids, emoji, autorun, offline
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        TOKEN = cfg["TOKEN"]
        ids = cfg["ids"]
        emoji = cfg["emoji"]
        autorun = cfg["autorun"]
        offline = cfg["offline"]
def transform(message):
    for emojis in message.reactions:
        if emoji == str(emojis):
            global messagesslownik
            messagesslownik.append(message.author.id)
            return str(message.author.name)
@client.event
async def on_ready():
    if offline == True:
        await client.change_presence(status=discord.Status.offline)
    print("bot on")
    if autorun == True:
        global atime, atime2, atimepass
        atime = int(time.time())
        for aaa in ids:
            channel = await client.fetch_channel(aaa)
            print(channel.name)
            async for content in channel.history(limit=None).map(transform):
                if content == None:
                    pass
                else:
                    f = open("osoby.list", "a")
                    #print(content)
                    f.write(content)
                    f.close()
        atime2 = int(time.time())
        atimepass = atime2 - atime
        print("Done in %s!" % str(datetime.timedelta(seconds=atimepass)))
@client.command()
async def reactions(ctx):
    osoby = []
    for x in messagesslownik:
        try:
            osoby.append(x)
            print(osoby)
            try:
                globals()[x]
            except:
                globals()[x] = 0
                globals()[x] += 1
            else:
                globals()[x] += 1
        except:
            pass
    osoby = list(dict.fromkeys(osoby))
    osobysorted = {}
    for a in osoby:
        osobysorted[a] = globals()[a]
    print(osobysorted)
    osoby = sorted(osobysorted)
    print(osoby)
    for y in osoby:
        osoba = y
        ilosc.append("<@%s>: %i" % (osoba, globals()[osoba]))
    ilosc2 = '\n'.join(ilosc)
    x1 = len(ilosc2)
    if x1 < 2001:
        await ctx.send("Topka osób ze słownikami na serwerze!\n%s" % ilosc2)
    else:
        print("Topka osób ze słownikami na serwerze!\n%s" % ilosc2)
client.run(TOKEN)
