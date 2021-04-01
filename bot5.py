import time
import os
import time
try:
    import discord
    import datetime
    import yaml
    from discord.ext import commands
except:
    os.system("start installpackages.py\nstart bot5.py")
    exit()
punkty = []
global users
global messagesemoji
messagesemoji = []
users = []
append = []
client = commandclient = commands.Bot(command_prefix = '-')
#--------
if os.path.isfile("config.yml") == False:
    print("Creating config file in your file location!")
    cfg = open("config.yml", 'w')
    cfg.write("#Welcome to the config! Please read every line about config lines, because editing something wrong can harm this program!\n\n\n#Put your discord token bot right here:\nTOKEN: \"\"\n\n#Please here put your channel list. Each channel you should put in layout\"- ID\" every each line.\nIDs:\n - FirstID\n\n\n#Please put here your emoji. Format: <:emoji:emoji_id>\nemoji: \"<>\"\n\nOutputMessage:\"This is a simple message. Edit it in config:\" # Provide here message the bot will send when posting ranking. NOTE: You should only use characters from English Alphabet, because of possiblity to \"artifact\" those characters.\nautorun: False #Provide True if you want to check run by auto. When False, most of settings above DON'T MATTER. You provide them using command.\noffline: False #Should bot be marked as Offline or Online (in status). Writing True will turn it to offline. Anything else will disable this.\n###################\n#Credit by heyngra#\n###################")
    cfg.close()
    print("Done!\nPlease, now fill the configuration file with things and start this program again!")
    time.sleep(3)
    exit()
elif os.path.isfile("config.yml") == True:
    global TOKEN, ids, emoji, autorun, offline, messagetext
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        TOKEN = cfg["TOKEN"]
        ids = cfg["ids"]
        emoji = cfg["emoji"]
        messagetext = cfg["OutputMessage"]
        autorun = cfg["autorun"]
        offline = cfg["offline"]
def transform(message):
    for emojis in message.reactions:
        if emoji == str(emojis):
            global messagesemoji
            messagesemoji.append(message.author.id)
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
                    f = open("users.list", "a")
                    #print(content)
                    f.write(content)
                    f.close()
        atime2 = int(time.time())
        atimepass = atime2 - atime
        print("Done in %s!" % str(datetime.timedelta(seconds=atimepass)))
@client.command()
async def reactions(ctx, *amount):
    times = 0
    if len(amount) >= 1:
        times = int(amount[0])
    print(times)
    users = []
    for x in messagesemoji:
        try:
            users.append(x)
            print(users)
            try:
                globals()[x]
            except:
                globals()[x] = 0
                globals()[x] += 1
            else:
                globals()[x] += 1
        except:
            pass
    users = list(dict.fromkeys(users))
    users3 = users
    users2 = {}
    for d in users:
        users2[d] = globals()[d]
    sorted_keys = sorted(users2, key=users2.get, reverse=True)
    users = {}
    for a in sorted_keys:
        users[a] = users2[a]
    print(users)
    users = list(users)
    if times > 0:
        users = users[:times]
    append3 = []
    for y in users:
        osoba = y
        append3.append("<@%s>: %i" % (osoba, globals()[osoba]))
    append2 = '\n'.join(append3)
    x1 = len(append2)
    if x1 < 2001:
        await ctx.send("%s\n%s" % (messagetext, append2))
    else:
        print("%s\n%s" % (messagetext, append2))
    del users, users2, sorted_keys, times, osoba, append3, append2
    for x in users3:
        del globals()[x]
client.run(TOKEN)
