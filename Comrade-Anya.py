import discord

client = discord.Client()

@client.event
async def on_ready():
	print("WE HAVE  LOGGEd IN AS {0.user}.format(client)")

@client.event 
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		
			print("hello")
		
	if message.content.startswith('$Stalin-quote'):
		
			await message.channel.send('“Those who vote decide nothing. Those who count the vote decide everything.” ― Joseph Stalin')
	if message.content.startswith('$intro'):
		
			await message.channel.send('“I am Anastassia . A communist discord bot. For commands type $commands')
	
  

client.run('OTg0ODY5MjMyMTI4OTU4NDg0.GrokzH.A-XN4hfntOFgvaxsow-nDY1hYr2eQVatlemOzM')
	
	  
	
	     
	