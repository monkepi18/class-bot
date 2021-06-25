import os
import discord
import datetime
import pytz
from schedule import getSub
#from stay_woke import keep_alive

client = discord.Client()

@client.event
async def on_ready() :
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('#hello'):
    await message.channel.send("Hemlu _/\\_")

  if message.content.startswith('#class'):
    await message.channel.send("Papa bolo tab bataenge")

  if message.content.startswith('#clamss'):
    baat= getSub()
    await message.channel.send(baat)

  if message.content.startswith('#papa'):
    baat= getSub()
    await message.channel.send(baat + " hai beta")

#keep_alive()
client.run(os.getenv('TOKEN'))
