import discord
import os
import requests

client = discord.Client()

def current_weather():
  params = {
    'access_key': os.getenv('Key'),
    'query': 'Ottawa'
  }
  weather = requests.get("http://api.weatherstack.com/current",params)
  api_response = weather.json()
  weather_current = 'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature'])
  return weather_current
  



@client.event
async def on_ready():
  print('Ready to Roll')

@client.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(f'Hi {member.name}')

@client.event
async def on_message(message):
  if message.content.startswith('*weather'):
    weather_call = current_weather()
    await message.channel.send(weather_call)

client.run(os.getenv('TOKEN'))