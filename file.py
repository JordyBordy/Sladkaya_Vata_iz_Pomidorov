from Miner_Igor import Player
import pickle

Users = {
    '0': Player('Admin')
}

file = open('Users.data', 'wb')
pickle.dump(Users, file)
file.close()