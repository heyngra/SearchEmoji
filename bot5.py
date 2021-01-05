import time
import os
import discord
from TOKEN_FILE import token #if you want to import TOKEN from different file then create file named TOKEN.FILE.py and write in it token='YOUR_TOKEN'
#token = "" #If you want to use TOKEN inside then remove the '#' and just insert TOKEN.
from discord.ext import commands
messagesslownik = []
punkty = []
global osoby
osoby = []
ilosc = []
client = commands.Bot(command_prefix = '-')

def checkmessage(id1, id2):
    for emojis in range(len(id1.reactions)):
        if "<:slownik:701787316662042644>" == str(id1.reactions[emojis]): #If you want to change the chosen emoji then write: <:emoji_name:emoji_id>
            messagesslownik.append(id2)
        else:
            pass
@client.event
async def on_ready():
    print("bot on")
    global ids
    ids = [795412287908347905, 791417428546420747] # Here you need to put ids of channels to check, separated by commas.
    for aaa in range(len(ids)):
        channel = await client.fetch_channel(ids[aaa])
        messages = await channel.history(limit=1000000).flatten()
        a = len(messages)
        i = 0
        while i < a:
            message2 = messages[i]
            messagee = await channel.fetch_message(message2.id)
            checkmessage(messagee, message2.id)
            i += 1
    print("Done!")
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

client.run(token)
