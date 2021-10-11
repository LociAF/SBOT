import os, discord, json, functions as smash

client = discord.Client()

@client.event
async def on_ready():
  print("Loggato con {0.user}".format(client))


@client.event
async def on_message(message):

  if message.author == client.user:
    return

  # CONTROLLA QUALI EVENTI CI SONO IN UN TORNEO
  if message.content.startswith('!check https://smash.gg/tournament/'):
    tournamentName = message.content.replace("!check https://smash.gg/tournament/", "").split("/")[0]
    data = smash.get_tournament_info(1, 2, "tournament/" + tournamentName)
    json_data = json.loads(data.text)
    
    message_text = """{}: {} eventi totali
    """.format(json_data["data"]["tournament"]["name"], len(json_data["data"]["tournament"]["events"]))

    for event in json_data["data"]["tournament"]["events"]:
      message_text = message_text + """- {} ({})
      """.format(event["name"], event["id"])

    await message.channel.send(message_text)

  # OTTIENI RISULTATI DI UN EVENTO
  if message.content.startswith('!add '):
    event_id = message.content.replace("!add ", "")
    data = smash.get_results_info(1, 2, event_id)
    json_data = json.loads(data.text)
    await message.channel.send(data.text)

client.run(os.environ['DISCORD_TOKEN'])