import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print("Loggato con {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('wee'):
    await message.channel.send('Wee')

client.run(os.environ['DISCORD_TOKEN'])