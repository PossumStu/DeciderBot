#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?")
TOKEN = "NDQxOTgxMzg3NzAxMjIzNDM1.Dc4KxQ.VdhdLEFG57iBTIyR06CtSlgcFZU"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)



@client.command(name='die',
               description='Roll a 6 sided die',
                brief='Roll a 6 sided die',
               aliases=['d6'])
async def die():
    die = ['1','2','3','4','5','6']
    await client.say(random.choice(die))
    
@client.command(name='dice',
               description='Roll a pair of 6 sided dice',
                brief='Roll a pair of 6 sided dice')
async def dice():
    die = ['1','2','3','4','5','6']
    die1 = random.choice(die)
    die2 = random.choice(die)
    await client.say(die1 + " and " + die2 + '\nTotal: ' + str(int(die1)+int(die2)))

@client.command(name='d4',
               description='Roll a 4 sided die',
                brief='Roll a 4 sided die')
async def d4():
    await client.say(random.choice(range(1,4)))
    
@client.command(name='d8',
               description='Roll an 8 sided die',
                brief='Roll an 8 sided die')
async def d8():
    await client.say(random.choice(range(1,8)))
    
@client.command(name='d10',
               description='Roll a 10 sided die',
                brief='Roll a 10 sided die')
async def d10():
    await client.say(random.choice(range(1,10)))
    
@client.command(name='d12',
               description='Roll a 12 sided die',
                brief='Roll a 12 sided die')
async def d12():
    await client.say(random.choice(range(1,12)))
    
@client.command(name='d20',
               description='Roll a 20 sided die',
                brief='Roll a 20 sided die'
               )
async def d20():
    await client.say(random.choice(range(1,20)))
    
@client.command(name='flip',
               description='Flip a coin',
                brief='Flip a coin',
               aliases=['coinflip','coin'])
async def flip():
    coin = ['Heads','Tails']
    await client.say(random.choice(coin))

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
            'It is certain','It is decidedly so','Without a doubt','Yes definitely','You may rely on it',
            'As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again',
            'Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again',
            'Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful'
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.event
async def on_ready():
    await client.change_presence(game=Game(type=3,name="you trying to decide"))
    print("Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)


# In[ ]:





# In[ ]:




