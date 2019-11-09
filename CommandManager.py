import Command
import Game.GameCommands as GameCommands
class CommandManager ():
	commands = []
	
	def __init__(self, client):
		self.client = client
		self.commands.append(Command.Info(client, self))
		self.commands.append(Command.Help(client, self))
		self.commands.append(GameCommands.Start(client, self))

	async def execute(self, message):
		msg = message.content.split(self.client.config['prefix'])[1]
		cmd = msg.split()[0]
		args = msg.split(cmd)[1].split()

		for command in self.commands:
			for alias in command.aliases:
				if cmd == alias:
					await command.execute(message, cmd, args)
					break