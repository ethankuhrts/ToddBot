import json

class GameManager:
	def __init__ (self):
		self.map = json.load(open('Game/map.json'))
		self.users = json.load(open('Game/users.json'))
		self.items = json.load(open('Game/items.json'))

	def load_map(self):
		self.map = json.load(open('Game/map.json'))
		return self.map
	
	def load_users(self):
		self.users = json.load(open('Game/users.json'))
		return self.users
	def load_items(self):
		self.items = json.load(open('Game/items.json'))
		return self.items

	def getUser(self, id):
		self.load_users()
		if id in self.users:
			return self.users[id]
	def getItem(self, name):
		self.load_items()
		if name in self.items:
			return self.items[name]

	def addUser(self, user, id):
		users = self.load_users()
		users[str(id)] = user
		with open('Game/users.json', 'w+') as file:
			json.dump(users, file)
