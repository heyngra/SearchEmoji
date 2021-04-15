import time
import os
import time
import json
import sys
try:
    import discord
    import datetime
    import yaml
    import colorama
    from discord.ext import commands
except:
    os.system("start installpackages.py\nstart bot5.py")
    exit()
punkty = []
global users
global messagesemoji
global datajson
messagesemoji = []
users = []
append = []
client = commandclient = commands.Bot(command_prefix = '-')
if os.name == "nt":
    colorama.init()
#--------
if os.path.isfile("config.yml") == False:
    print("Creating config file in your file location!")
    cfg = open("config.yml", 'w',encoding="utf-8")
    cfg.write("#Welcome to the config! Please read every line about config lines, because editing something wrong can harm this program!\n\n\n#Put your discord token bot right here:\nTOKEN: \"\"\n\n#Please here put your channel list. Each channel you should put in layout\"- ID\" every each line.\nids:\n - FirstID\n\n\n#Please put here your emoji. Format: <:emoji:emoji_id>\nemoji: \"<>\"\n\nOutputMessage: \"This is a simple message. Edit it in config:\" # Provide here message the bot will send when posting ranking. NOTE: You should only use characters from English Alphabet, because of possiblity to \"artifact\" those characters.\nautorun: False #Provide True if you want to check run by auto. When False, most of settings above DON'T MATTER. You provide them using command.\noffline: False #Should bot be marked as Offline or Online (in status). Writing True will turn it to offline. Anything else will disable this.\n###################\n#Credit by heyngra#\n###################")
    cfg.close()
    print("Done!\nPlease, now fill the configuration file with things and start this program again!")
    time.sleep(3)
    exit()
elif os.path.isfile("config.yml") == True:
    global TOKEN, ids, emoji, autorun, offline, messagetext
    with open("config.yml", "r",encoding="utf-8") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        TOKEN = cfg["TOKEN"]
        ids = cfg["ids"]
        emoji = cfg["emoji"]
        print(emoji)
        messagetext = cfg["OutputMessage"]
        autorun = cfg["autorun"]
        offline = cfg["offline"]
if os.path.isfile("data.json") == False:
    print("Creating json file!")
    dt = open("data.json", "w",encoding="utf-8")
    temp = {"channellast":{}, "useremojis":{emoji: {}}}
    dt.write("{\"channellast\":{}, \"useremojis\":{\"%s\":{}}}" % emoji)
    datajson = {"channellast":{},"useremojis":{emoji:{}}}
    dt.close()
else:
    f = open("data.json", "r",encoding="utf-8")
    datajson = json.load(f)
    f.close()
    try:
        datajson["useremojis"][emoji]
    except:
        temp = {emoji:{}}
        datajson["useremojis"].update(temp)
    else:
        pass
    for i in datajson["useremojis"][emoji]:
        for _i in range(datajson["useremojis"][emoji][i]):
            messagesemoji.append(int(i))
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def jsonupdate():
    f = open("data.json", "w",encoding="utf-8")
    print(datajson)
    json.dump(datajson, f, ensure_ascii=False)
    f.close()
def returnmessage(channel, nm):
    clear()
    print("Currently scanning: %s. Progress: %i/???" % (channel.name, nm))
    
try:
    datajson["useremojis"][emoji]
except:
    temp = {emoji:{}}
    datajson["useremojis"].update(temp)
else:
    pass
print(datajson["useremojis"][emoji])
def transform(message):
    for emojis in message.reactions:
        print(emojis.emoji)
        if emoji == emojis.emoji:
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
            try:
                datajson["channellast"][str(aaa)]
            except Exception as e:
                print(e)
                timech = None
            else:
                timech = datajson["channellast"][str(aaa)]
            if timech == None:
                rp = 1
                async for content in channel.history(limit=None).map(transform):
                    returnmessage(channel, rp)
                    if content == None:
                        pass
                    else:
                        f = open("users.list", "a",encoding="utf-8")
                        f.write(content)
                        f.close()
                    rp += 1
                temp = {str(aaa): time.time()}
                datajson["channellast"].update(temp)
                del temp
            else:
                async for content in channel.history(limit=None, after=datetime.datetime.utcfromtimestamp(int(timech))).map(transform):
                    rp = 1
                    returnmessage(channel, rp)
                    if content == None:
                        pass
                    else:
                        f = open("users.list", "a",encoding="utf-8")
                        f.write(content)
                        f.close()
                    rp += 1
                datajson["channellast"][str(aaa)] = time.time()
        jsonupdate()
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
    #print(users)
    users = list(users)
    if times > 0:
        users = users[:times]
    append3 = []
    for y in users:
        osoba = y
        append3.append("<@%s>: %i" % (osoba, globals()[osoba]))
        temp = {osoba: globals()[osoba]}
        try:
            datajson["useremojis"][emoji][str(osoba)]
        except Exception as e:
            print(e)
            datajson["useremojis"][emoji].update(temp)
        else:
            datajson["useremojis"][emoji][str(osoba)] = globals()[osoba]
    jsonupdate()
    append2 = '\n'.join(append3)
    x1 = len(append2)
    if x1 < 2001:
        await ctx.send("%s\n%s" % (messagetext, append2))
    else:
        print("%s\n%s" % (messagetext, append2))
    del users, users2, sorted_keys, times, append3, append2
    try:
        del osoba
    except Exception:
        pass
    for x in users3:
        del globals()[x]
client.run(TOKEN)
