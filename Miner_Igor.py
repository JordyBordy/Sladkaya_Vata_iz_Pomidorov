from setings import CHANCES, COSTS
from lists import minerals_list
import random

class Player():

    def __init__(self, username):
        self.pickaxe = 'wood'
        self.helmet = 'none'
        self.vest = 'none'
        self.pants = 'none'
        self.boots = 'none'
        self.balance = 0
        self.username = username
        self.stamina = 20
        self.stamina_max = 20
        self.current_keyboard = 'main'
        self.bank_account = 0
        self.percent = 1

    def recount_stamina_max(self):
        self.stamina_max = 20
        if self.helmet == 'old_helmet':
            self.stamina_max += 5
        elif self.helmet == 'common_helmet':
            self.stamina_max += 10
        elif self.helmet == 'helmet_with_lamp':
            self.stamina_max += 15
        elif self.helmet == 'modern_helmet':
            self.stamina_max += 20
        if self.vest == 'ragged_vest':
            self.stamina_max += 5
        elif self.vest == 'common_vest':
            self.stamina_max += 10
        elif self.vest == 'waterproof_vest':
            self.stamina_max += 15
        elif self.vest == 'waterproof_warm_vest':
            self.stamina_max += 20
        if self.pants == 'summer_shorts':
            self.stamina_max += 5
        elif self.pants == 'lightweight_pants':
            self.stamina_max += 10
        elif self.pants == 'waterproof_pants':
            self.stamina_max += 15
        elif self.pants == 'waterproof_warm_pants':
            self.stamina_max += 20
        if self.boots == 'slippers':
            self.stamina_max += 5
        elif self.boots == 'sneakers':
            self.stamina_max += 10
        elif self.boots == 'cheap_shoes':
            self.stamina_max += 15
        elif self.boots == 'expensive_shoes':
            self.stamina_max += 20

    def change_pickaxe(self, new_pickaxe):
        self.pickaxe = new_pickaxe

    def change_helmet(self, new_helmet):
        self.helmet = new_helmet
        self.recount_stamina_max()

    def change_vest(self, new_vest):
        self.vest = new_vest
        self.recount_stamina_max()

    def change_pants(self, new_pants):
        self.pants = new_pants
        self.recount_stamina_max()

    def change_boots(self, new_boots):
        self.boots = new_boots
        self.recount_stamina_max()

    def mine(self, number_of_chance):
        if self.stamina == 0:
            return 0
        self.stamina -=1
        if self.pickaxe == 'wood':
            chance_of_other = 1 - (CHANCES['CHANCE_OF_COAL'] + CHANCES['CHANCE_OF_CREEPER'])
            chance_of_coal = CHANCES['CHANCE_OF_COAL']
        elif self.pickaxe == 'stone':
            chance_of_other = 1 - (CHANCES['CHANCE_OF_COAL'] - 0.02 + CHANCES['CHANCE_OF_CREEPER'])
            chance_of_coal = CHANCES['CHANCE_OF_COAL'] - 0.02
        elif self.pickaxe == 'iron':
            chance_of_other = 1 - (CHANCES['CHANCE_OF_COAL'] - 0.05 + CHANCES['CHANCE_OF_CREEPER'])
            chance_of_coal = CHANCES['CHANCE_OF_COAL'] - 0.05
        elif self.pickaxe == 'gold':
            chance_of_other = 1 - (CHANCES['CHANCE_OF_COAL'] - 0.1 + CHANCES['CHANCE_OF_CREEPER'])
            chance_of_coal = CHANCES['CHANCE_OF_COAL'] - 0.1
        elif self.pickaxe == 'diamond':
            chance_of_other = 1 - (CHANCES['CHANCE_OF_COAL'] - 0.2 + CHANCES['CHANCE_OF_CREEPER'])
            chance_of_coal = CHANCES['CHANCE_OF_COAL'] - 0.2



        random_minerals = random.randint(1, number_of_chance)

        if 1 <= random_minerals <= number_of_chance * chance_of_coal:
            amount_of_minerals = random.randint(1, int(5 * self.percent))
            self.balance += amount_of_minerals * COSTS['COST_OF_COAL']
            return f'{minerals_list[0]} x {amount_of_minerals}'

        elif number_of_chance * chance_of_coal + 1 <= random_minerals <= number_of_chance * (chance_of_other * CHANCES['CHANCE_OF_IRON'] + chance_of_coal):
            amount_of_minerals = random.randint(1, int(5 * self.percent))  
            self.balance += amount_of_minerals * COSTS['COST_OF_IRON']
            return f'{minerals_list[1]} x {amount_of_minerals}'

        elif number_of_chance * (chance_of_other * CHANCES['CHANCE_OF_IRON'] + chance_of_coal) + 1 <= random_minerals <= number_of_chance * (chance_of_other * (CHANCES['CHANCE_OF_IRON'] + CHANCES['CHANCE_OF_GOLD']) + chance_of_coal):
            amount_of_minerals = random.randint(1, int(4 * self.percent))
            self.balance += amount_of_minerals * COSTS['COST_OF_GOLD']
            return f'{minerals_list[2]} x {amount_of_minerals}'

        elif number_of_chance * (chance_of_other * (CHANCES['CHANCE_OF_IRON'] + CHANCES['CHANCE_OF_GOLD']) + chance_of_coal) + 1 <= random_minerals <= number_of_chance * (chance_of_other * (CHANCES['CHANCE_OF_IRON'] + CHANCES['CHANCE_OF_GOLD'] + CHANCES['CHANCE_OF_DIAMOND']) + chance_of_coal):  
            amount_of_minerals = random.randint(1, int(3 * self.percent))
            self.balance += amount_of_minerals * COSTS['COST_OF_DIAMOND']
            return f'{minerals_list[3]} x {amount_of_minerals}'

        else: 
            return 'creeper'

    def income(self):
        self.balance += int(self.bank_account * 0.001)

    def info(self):
        return (self.pickaxe, 'Ваша кирка') 