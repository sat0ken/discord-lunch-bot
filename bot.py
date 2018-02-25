import discord
import random
import tabelog
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if  message.content.startswith("ランチ"):
        if client.user != message.author:
            say = message.content
            words = say.split("、")
            lunch = tabelog.get_shop_list(words[1], words[2])
            await client.send_message(message.channel, lunch)

client.run("TOKEN")
