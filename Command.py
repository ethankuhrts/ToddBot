import discord

print("aaaa")

Category = {
	'information': {
		'display': '📓 Bot Information'
	},
	'game': {
		'display': '🎮 Game Commands'
	}
}



class Command ():
	name = ""
	aliases = []
	category = ""
	description = ""
	def __init__(self, client, manager):
		self.client = client
		self.manager = manager

	async def execute(self, message, cmd, args):
		print(self.name)



class Help(Command):
	name = "help"
	aliases = ["help"]
	category=Category['information']
	description = "list of commands for the bot"
	async def execute(self, message, cmd, args):
		await super().execute(message, cmd, args)
		embed = discord.Embed(title="Help", description=f"Commands  -  prefix: {self.manager.client.config['prefix']}", color=0x00ff00)

		helpList = []
		for key in Category:
			cmds = ""
			for command in self.manager.commands:
				if command.category == Category[key]:
					cmds += f"{command.name} - {command.description}\n"
			if cmds == "":
				cmds = "None"
			print(cmds)
			embed.add_field(name=Category[key]['display'], value=cmds)
		await message.channel.send(embed=embed)

class Info(Command):
	name = "info"
	aliases = ["info", "information"]
	category=Category['information']
	description = "information about the bot"
	async def execute(self, message, cmd, args):
		await super().execute(message, cmd, args)
		await message.channel.send("this is a HiImTodd's first python bot")