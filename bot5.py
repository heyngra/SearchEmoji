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
    cfg.write("#Welcome to the config! Please read every line about config lines, because editing something wrong can harm this program!\n\n\n#Put your discord token bot right here:\nTOKEN: \"\"\n\n#Please here put your channel list. Each channel you should put in layout\"- ID\" every each line.\nIDs:\n - FirstID\n\n\n#Please put here your emoji. Format: <:emojiname:emoji_id>\nemoji: \"<>\"\n\n\n###################\n#Credit by heyngra#\n###################")
    cfg.close()
    print("Done!\nPlease, now fill the configuration file with things and start this program again!")
    time.sleep(3)
    exit()
elif os.path.isfile("config.yml") == True:
    global TOKEN
    global ids
    global emojiname
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        TOKEN = cfg["TOKEN"]
        ids = cfg["IDs"]
        emojiname = cfg["emoji"]

def checkmessage(id1, id2):
    for emojis in range(len(id1.reactions)):
        if emojiname == str(id1.reactions[emojis]):
            messagesslownik.append(id2)
        else:
            pass
def transform(message):
    for emojis in range(len(message.reactions)):
        if emojiname == str(message.reactions[emojis]):
            global messagesslownik
            messagesslownik.append(message.author.id)
            #return str(message.reactions[emojis])
            return str(message.author.name)
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    print("bot on")
    global ids
    global atime
    global atime2
    global atimepass
    atime = int(time.time())
    for aaa in range(len(ids)):
        channel = await client.fetch_channel(ids[aaa])
        print(channel.name)
        async for content in channel.history(limit=None, after=datetime.datetime(2020, 4, 19)).map(transform):
            if content == None:
                pass
            else:
                f = open("osoby.list", "a")
                print(content)
                f.write(content)
                f.close()
    atime2 = int(time.time())
    atimepass = atime2 - atime
    print("Done in %s!" % str(datetime.timedelta(seconds=atimepass)))
@client.command()
async def reactions(ctx):
    osoby = []
    print("zaczynam obliczać")
    for x in range(len(messagesslownik)):
        try:
            osoby.append(messagesslownik[x])
            print(osoby)
            try:
                globals()[messagesslownik[x]]
            except:
                globals()[messagesslownik[x]] = 0
                globals()[messagesslownik[x]] += 1
            else:
                globals()[messagesslownik[x]] += 1
        except:
            pass
    osoby = list(dict.fromkeys(osoby))
    osobysorted = {}
    for a in range(len(osoby)):
        osobysorted[osoby[a]] = globals()[osoby[a]]
    print(osobysorted)
    osoby = sorted(osobysorted)
    print(osoby)
    for y in range(len(osoby)):
        osoba = osoby[y]
        ilosc.append("<@%s>: %i" % (osoba, globals()[osoba]))
    ilosc2 = '\n'.join(ilosc)
    x1 = len(ilosc2)
    if x1 < 2001:
        await ctx.send("Topka osób ze słownikami na serwerze!\n%s" % ilosc2)
    else:
        print("Topka osób ze słownikami na serwerze!\n%s" % ilosc2)
client.run(TOKEN)
