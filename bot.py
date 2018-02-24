import discord
import tabelogu
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
            tabelogu.shop_list = []
            say = message.content
            words = say.split("、")
            lunch = tabelogu.get_shop_list(words[1], words[2])
            await client.send_message(message.channel, lunch)

client.run("TOKEN")
