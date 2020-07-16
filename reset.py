import pickle
from Miner_Igor import Player

file = open('Users.data', 'rb')
Users = pickle.load(file)
file.close()

Users['0'] = Player('Admin')

for i in Users:
	Users[i].balance = 0
	Users[i].change_pickaxe('wood')
	Users[i].stamina = 20
	Users[i].change_helmet('none')
	Users[i].change_vest('none')
	Users[i].change_pants('none')
	Users[i].change_boots('none')
	Users[i].stamina_max = 20

file = open('Users.data', 'wb')
pickle.dump(Users, file)
file.close()