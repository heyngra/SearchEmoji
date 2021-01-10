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
messagesslownik = []
punkty = []
global osoby
osoby = []
ilosc = []
client = commands.Bot(command_prefix = '-')
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
@client.event
async def on_ready():
    print("bot on")
    global ids
    global atime
    global atime2
    global atimepass
    atime = int(time.time())
    for aaa in range(len(ids)):
        channel = await client.fetch_channel(ids[aaa])
        messages = await channel.history(limit=None).flatten()
        a = len(messages)
        for test in range(a):
            a1 = a - 1
            message2 = messages[test]
            messagee = await channel.fetch_message(message2.id)
            checkmessage(messagee, message2.id)
            print("Checked message %i/%i" % (test, a1))

    atime2 = int(time.time())
    atimepass = atime2 - atime
    print("Done in %s!" % str(datetime.timedelta(seconds=atimepass)))
@client.command()
async def reactions(ctx):
    osoby = []
    for aaa in range(len(ids)):
        channel = await client.fetch_channel(ids[aaa])
        for x in range(len(messagesslownik)):
            try:
                message = await channel.fetch_message(messagesslownik[x])
                osoby.append(message.author.id)
                try:
                    globals()[message.author.id]
                except:
                    globals()[message.author.id] = 0
                    globals()[message.author.id] += 1
                else:
                    globals()[message.author.id] += 1
            except:
                pass
    osobyy = osoby
    osoby = list(dict.fromkeys(osoby))
    for y in range(len(osoby)):
        osoba = osoby[y]
        ilosc.append("<@%s>: %i" % (osoba, globals()[osoba]))
    ilosc2 = '\n'.join(ilosc)
    await ctx.send("Topka osób ze słownikami na serwerze!\n%s" % ilosc2)
client.run(TOKEN)
