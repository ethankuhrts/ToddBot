import discord
import json
import Game.GameManager as GameManager

from CommandManager import CommandManager

config = json.load(open("config.json"))

class Client(discord.Client):
	async def on_ready(self):
		print('Logged in as', self.user)
		activity = discord.Activity(name='my creator fail', type=discord.ActivityType.watching)
		await client.change_presence(activity=activity)

		self.commandManager = CommandManager(self)
		self.GameManager = GameManager.GameManager()
		self.config = config

		


	async def on_message(self, message):
		if message.author == self.user:
			return

		if message.content[0] == config['prefix']:
			await self.commandManager.execute(message)

client = Client()
client.run(config['token'])

#Maso n         <lol dumbass u dont even know how to do python comments