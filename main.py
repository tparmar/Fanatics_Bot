import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

#Create Discord Client
client = discord.Client()

#Set prefix
bot = commands.Bot(command_prefix = '.')
bot.remove_command('help') #Remove inbuilt help command in discord.py

#List of words that the discord client will read so that they can send a meme of encouragement
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "terrible", "sucks", "depressing", "unfair"]

#List of memes
starter_encouragements = [
    "Always remember: Wigan 1-0 Manchester City", 
    "At least you didn't lose 8-2....",
    "At least you're not Ishan", 
    "Think about Barca 6-1 PSG", 
    "Don't be sad, look at Arsenal!", 
    "Did you lose 4-0 against Liverpool and Divock? Did you lose 3-0 against Roma and Manolas? Did you lose 8-2 to Bayern? Than life is good. Unless you're an Arsenal Fan.", 
    "Never forget: West Brom 5-2 Chelsea", "As long as you don't wear baggy pants and tighty whities at the same time, you'll be fine in life. Just ask Ishan!", 
    "Chapathis, jigglying in my belly! - Ishan Mungikar", 
    "Fun Fact: Ishan and Goaters had a phase called Style, where they would pull up the pants where high, and tuck in their shirt. They looked those basketball players from the 1980s.", 
    "Fun Fact: Once, Goaters had a tap in on the goal line but defied physics and hit the crossbar.", 
    "Nipun in rocket league: NippinDots has left the party. NippinDots lost connection", 
    "Fun Fact: One time at a party at Nipun's house, Ishan sat on Nihaal's head and gave him another concussion right after Nihaal healed from his last one. Smart right?", 
    "Fun Fact: In eigth grade, Nihaal broke one of his arms. The day he got his brace off, he broke his other arm. Talk about stupid.", 
    "Ishan in the group chat: Ill come at 3:30. Ishan at the soccer field: *comes at 4:30", 
    "Nipun: It's so fun to play with my belly!"
    "Never let Nipun near your garage"
]

#Choose a random quote from a database
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

#Send the 6-1 story
def send_story():
  story = "It was March 8, 2017, and the weather was beautiful. Everyone felt it. The vibe. Although Barca were down 4-0 against PSG, there was just a feeling that Barca was still in it. As Sriboy once said: I smell a comeback! The game had an impressive attendance of 96,290 despite the home side's heavy defeat in the first game. Barcelona's Luis Suárez scored the first goal of the game in the 3rd minute after heading the ball over the line before it was cleared by Thomas Meunier. In the 40th minute, Paris Saint-Germain's Layvin Kurzawa scored an own goal in an attempt to block a shot by Andrés Iniesta. The third goal came in the 50th minute via a penalty scored by Lionel Messi after Neymar was fouled by Thomas Meunier. Barcelona's hopes were seemingly brought down after Edinson Cavani scored Paris Saint-Germain's only goal in the 62nd minute, leaving them requiring three more to win due to the away goals rule now favouring PSG. Neymar scored two goals in the closing stages – a free kick in the 88th minute and a penalty kick in the 91st – to make it 5–1. In the final seconds of the match, Neymar delivered a cross into the penalty area, and Sergi Roberto scored their sixth and final goal in the 95th minute thus winning the game 6–1 and advancing to the quarter finals 6–5 on aggregate. WHAT A GAME I SAY, WHAT A GAME. Also, I miss Suarez. That guy had huge teeth."
  return story

#Set discord rich presence of discord bot
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game(name="Soccer | Made by Goaters", type = "2"))
    print('We have logged in as {0.user}'.format(client))

cooldown = True
@client.event
#When message sent
async def on_message(message):
    global cooldown
    if message.author == client.user:
        return
    msg = message.content
    # '$quote' command
    if msg.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)
    # '$meme' command
    if msg.startswith('$meme'):
        await message.channel.send(random.choice(starter_encouragements))
    # '$greatestmatch' command
    if msg.startswith('$greatestmatch'):
      await message.channel.send(send_story())

    if msg.startswith('$pic'):
      with open('pics/messi_2.jpeg', 'rb') as f:
        picture = discord.File(f)
        await message.channel.send(file = picture)
    if msg.startswith('$messi'):
      with open('pics/messi_pic.jpeg', 'rb') as f:
        picture = discord.File(f)
        await message.channel.send(file = picture)
    #check each message if in sad_words so we can send a meme:
    if any(word in msg.lower() for word in sad_words):
        if cooldown == True:
            await message.channel.send(random.choice(starter_encouragements))
            cooldown = False
        else:
            time.sleep(60)
            cooldown = True
        
    
    #help command
    if message.content.startswith("$help"):
        embedVar = discord.Embed(title="Commands of Fanatics Bot", description="Here are all of the commands of the Fanatics bot right now.", color=0x00ff00)
        embedVar.add_field(name = '$quote', value = 'Returns a random quote', inline = False)
        embedVar.add_field(name = "$meme", value = "Returns a soccer meme", inline = False)
        embedVar.add_field(name = "$greatestmatch", value = "Returns the greatest match in soccer history", inline = False)
        await message.channel.send(embed=embedVar)


keep_alive()
client.run("ODE5NTc4NDM0OTc1ODI1OTcx.YEop5Q.FH_SQwXhfqghw7pFTe5eGOaRXYw")
