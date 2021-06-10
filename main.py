import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import google
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from datetime import datetime


#Create Discord Client
client = discord.Client()

#Set prefix
bot = commands.Bot(command_prefix = '.')
bot.remove_command('help') #Remove inbuilt help command in discord.py

#List of words that the discord client will read so that they can send a meme of encouragement
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "terrible", "sucks", "depressing", "unfair"]

#List of memes
memes = [
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
    "Nipun: It's so fun to play with my belly! :flushed:",
    "Never let Nipun near your garage",
    "Remember that time a little kid scored an open goal? Me neither",
    "Want some salt? Ask Ishan about Sid's cherry-picking :laughing:",
    "That time Alisson scored against West Brom in the 95th minute :laughing:",
    "Fun Fact: One time, Sid tried to get fancy on an open goal and tried to roulette it in, but missed the ball. Shourya took it forward, passed to Kuhsh, who crossed it in for Arjuna (who was on the other team) who volleyed it into his own net. What a play! :rofl:",
    "Remember that time Arsenal finished in the top 4? Me neither.",
    "Ask Liverpool fans where their center backs are. They won't be able to tell you anything.",
    "What's more empty, Manchester city's fanbase or Tottenham's trophy cabinet?",
    "Tottenham Fans vs Arsenal Fans ----- Totenham fans: \'Arsenal haven't finished top 4 in like forever, they are not even in Europe next season, and you guys have such bad players. I mean look at your table position!\' Arsenal Fans: \'We won the FA cup, so we are better\'",
    "Fun Fact: To protest against hate toward LGBTQ, Ishan changed his name to Jessica with the pronouns as \'Ze\' and \'Zhem\'",
    "Fun Fact: Lord Bendter has: more wolrd cup games than George Best, more world cup goals than di stefano, more euro goals than R9, more UCL goals than pele, more premier league goals than Lionel Messi, more bundesliga goals than CR7, and more league titles than Gerrard and Reus combined. ALL HAIL LORD BENDTER",
    "Nihaal's Rocket League IQ = 0",
    "What is a ghost's favorite soccer position? Ghoul Keeper :rofl:",
    "Why can't Cinderella play soccer? Because she always runs away from the ball",
    "Where do soccer players go to dance? The Futball :rofl:",
    "What lights up a soccer stadium? A soccer match :laughing:",
    "Why did the chicken get ejected from the soccer game? For persistent fowl play.",
    "Where's the best place to shop for a soccer uniform? New Jersey :rofl:",
    "How do we know that soccer referees are happy? Because they whiste while they work :laughing:",
    "What would you get if you crossed a soccer player and the Invisible Man? He would play soccer like no one hs ever seen :rofl:"
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

def convert(lst):
    return (lst[0].split())

URL = 'https://www.google.com/search?pz=1&cf=all&ned=us&hl=en&tbm=nws&gl=us&as_q={query}&as_occt=any&as_drrb=b&as_mindate={month}%2F%{from_day}%2F{year}&as_maxdate={month}%2F{to_day}%2F{year}&tbs=cdr%3A1%2Ccd_min%3A3%2F1%2F13%2Ccd_max%3A3%2F2%2F13&as_nsrc=Gulf%20Times&authuser=0'

def run(**params):
    response = requests.get(URL.format(**params))
    return response.url
#Set discord rich presence of discord bot
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game(name= "$help for commands | Made by Goaters", type = "2"))
    print('We have logged in as {0.user}'.format(client))


@client.event
#When message sent
async def on_message(message):
    emoji = '\N{THUMBS UP SIGN}'

    if message.author == client.user:
        return
    msg = message.content
    # '$quote' command
    if msg.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)
        await message.add_reaction(emoji)

    # '$meme' command
    if msg.startswith('$meme'):
        await message.channel.send(random.choice(memes))
        await message.add_reaction(emoji)

    # '$greatestmatch' command
    if msg.startswith('$greatestmatch'):
      await message.channel.send(send_story())
      await message.add_reaction(emoji)
    
    #'pic' with barca command
    if msg.startswith("$pic barca") or msg.startswith("$pic fcb") or msg.startswith("$pic bar"):
        num = random.randint(0,6)
        if num == 0:
            with open('pics/messi_pic.jpeg', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 1:
            with open('pics/messi_2.jpeg', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 2:
            with open('pics/pique2.jpeg', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 3:
            with open('pics/griezi_cele.jpg', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 4:
            with open('pics/lord_braithwaite.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 5:
            with open('pics/cool_messi.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 6:
            with open('pics/umtiti.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        await message.add_reaction(emoji)

    #'pic' with liverpool command
    if msg.startswith("$pic liverpool") or msg.startswith("$pic liv"):
        num = random.randint(0,4)
        if num == 0:
            with open('pics/liverpool_champions.jpg', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 1:
            with open('pics/var.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 2:
            with open('pics/virgil_pfp.jpg', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 3:
            with open('pics/virgil_pfp2.jpeg', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 4:
            with open('pics/trento2.jpg', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        await message.add_reaction(emoji)
    if msg.startswith("$pic mun") or msg.startswith("$pic man united"):
        num = random.randint(0,1)
        if num == 0:
            with open('pics/phil_jones_1.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        if num == 1:
            with open('pics/phil_jones_2.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        await message.add_reaction(emoji)
    if msg.startswith("$pic tot") or msg.startswith("$pic tottenham"):
        num = random.randint(0,1)
        if num == 0:
            with open("pics/hareth_kane.png", 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 1:
            with open("pics/bele.jpeg", 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        await message.add_reaction(emoji)
    if msg.startswith("$news"):
        temp = [message.content]
        split = convert(temp)
        if len(split) ==2:
            query = str(split[1]) + " news"
        else:
            query = str(split[1]) +  " " + str(split[2]) + " news"
        websites = []
        for j in search(query):
          websites.append(j)
        await message.channel.send(random.choice(websites))
        await message.add_reaction(emoji)
    
        
    #check each message if in sad_words so we can send a meme:
    if any(word in msg.lower() for word in sad_words):

        ran = random.randint(0,1)
        if ran == 0:
            await message.channel.send(random.choice(memes))
            
        
    
    #help command
    if message.content.startswith("$help"):
        embedVar = discord.Embed(title="Commands of Fanatics Bot", description="Here are all of the commands of the Fanatics bot right now.", color=0x00ff00)
        embedVar.add_field(name = '$quote', value = 'Returns a random quote', inline = False)
        embedVar.add_field(name = "$meme", value = "Returns a soccer meme", inline = False)
        embedVar.add_field(name = "$greatestmatch", value = "Returns the greatest match in soccer history", inline = False)
        embedVar.add_field(name = "$pic [team]", value = "Returns picture related to specified team. So far supports Liverpool, Barcelona, Tottenham, and Manchester United", inline = False)
        embedVar.add_field(name = "$news [team]", value = "Returns recent news about specified team. Make sure in place of [team] you input the full team name (max two words)")
        await message.channel.send(embed=embedVar)
        await message.add_reaction(emoji)


keep_alive()
# client.run(os.getenv('TOKEN'))
client.run("ODE5NTc4NDM0OTc1ODI1OTcx.YEop5Q.FH_SQwXhfqghw7pFTe5eGOaRXYw")