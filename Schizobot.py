import discord

from discord.ext import commands

from discord.ext import tasks

import random

import asyncio

import re

import os


botid = "725041777211342910"

bot = discord.Client()

bot = commands.Bot(command_prefix='?')

svrcount = len(bot.guilds)

with open('responses.txt', 'r') as file: 	
  lines = file.readlines()

@tasks.loop(seconds=3600.0)
async def status_update():
   print(len(bot.guilds))
   async for guild in bot.fetch_guilds(limit=150):
    print(guild.name)
   svrcount = len(bot.guilds)
   await bot.change_presence(activity  = discord.Activity( type = discord.ActivityType.watching, name = f'{svrcount} Servers'))
@bot.event
async def on_ready(): 
  print('bot started')
  await bot.wait_until_ready()
  status_update.start()

print(botid)
@bot.event
async def on_message(message, *args):
    if message.author == bot.user:
      print("bot tried to respond to itself")
      return
    if message.content == f"<@!{botid}>":
      return 
    if message.content == f"<@{botid}>":
      return
    if bot.user.mentioned_in(message):
     choice = random.choice(lines)
     WT = choice
     WOT = re.sub('http.*?(?=\s)', '', WT)
     print(WOT)
     print(len(WOT)/3)
     print(message.content)
     async with message.channel.typing():
       if len(WOT) < 35:
         await asyncio.sleep( len(WOT)/3 )
       elif len(WOT) > 35:
         await asyncio.sleep( 11.5 )
       await message.reply(choice)
       print ('Pinged Response')
    elif random.random() < .016:
     choice = random.choice(lines)
     WT = choice
     WOT = re.sub('http.*?(?=\s)', '', WT)
     print(WOT)
     print(len(WOT)/3)
     if f"<@{botid}>" in message.content:
           return
     if f"<@!{botid}>" in message.content:
           return
     async with message.channel.typing():
       if len(WOT) < 35:
         await asyncio.sleep( len(WOT)/3 )
       elif len(WOT) > 35:
         await asyncio.sleep( 11.5 )
       await message.reply(choice)
       print ('Random Response')
    elif message.channel.type == discord.ChannelType.private:
     choice = random.choice(lines)
     WT = choice
     WOT = re.sub('http.*?(?=\s)', '', WT)
     print(WOT)
     print(len(WOT)/3)
     async with message.channel.typing():
       if len(WOT) < 35:
         await asyncio.sleep( len(WOT)/3 )
       elif len(WOT) > 35:
         await asyncio.sleep( 11.5 )
       await message.reply(choice)
       print ('DM')
       await bot.process_commands(message)
#put your bot token inside the ""
bot.run("") 
#gl hf ;)
