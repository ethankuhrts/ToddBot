import Command
import discord

class Start(Command.Command):
	name = "start"
	aliases = ["start"]
	category = Command.Category['game']
	description = "create a character to play"

	async def execute(self, message, cmd, args):
		await super().execute(message, cmd, args) 	
		self.gManager = self.manager.client.GameManager
	
		author = message.author
		if len(args) < 1:
			await message.channel.send("Missing required argument: Name")
			return
		
		if not self.gManager.getUser(author.id):
			user = {	
				"name": args[0],
				"inventory": [self.gManager.getItem("iron_sword")],
				"level": 1,
				"upgrades": 5,
				"money": 0,
				"stats": {
					"strength": 1,		
					"speed": 1,
					"luck": 1,
					"endurance": 1,
					"magic": 1,
					"inteligence": 1
				}
			}
			await message.channel.send("Created a character use ;profile command to view")
			self.gManager.addUser(user, author.id)
			
		else:
			await message.channel.send("You have already created a character!")

class Profile(Command.Command):
	name = "profile"
	aliases = ["profile", "character"]
	category = Command.Category['game']
	description = "create a character to play"

	async def execute(self, message, cmd, args):
		author = message.author
		user = self.gManager.getUser(author.id)
		if not user:
			await message.channel.send("You have not created a character, create one with ;start")
			return
		embed = discord.Embed(title=user['name']+"'s Profile", color=0x00ff00)
		