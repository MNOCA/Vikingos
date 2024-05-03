import random

# Soldier

#build the soldier prototype
class Soldier:
    def __init__(self, health, strength): #initialize the attributes of each class instance
        self.health = health
        self.strength = strength
       
    def attack(self): #to determine the strength of an attack
        return self.strength

    def receiveDamage(self, damage): #to calculate the damage received by a combatant and adjust their health accordingly.
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def battleCry(self):
        return 'Odin Owns You All!'

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'        
        
        

# Davicente
# start battles between Vikings and Saxons. Manages the armies of Vikings and Saxons, methods for adding combatants to the armies and simulate the battle itself

class War():
    def __init__(self):
        self.vikingArmy = [] #create the list that will be populated with newly added soldiers
        self.saxonArmy = []

    def addViking(self, viking):# adds the number of a new viking to the vikingArmy list        
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self): #apply damage to the attacked soldier and remove them from the army list if their health falls to zero or below.
        saxon = random.choice(self.saxonArmy) #randomly select a soldier for attacks
        viking = random.choice(self.vikingArmy)
        damage = viking.attack() #or damage = viking.strength
        result = saxon.receiveDamage(damage)
        
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
             
    
    def saxonAttack(self): #apply damage to the attacked soldier and remove them from the army list if their health falls to zero or below.
        saxon = random.choice(self.saxonArmy) #randomly select a soldier for attacks
        viking = random.choice(self.vikingArmy)
        damage = saxon.attack() #or damage = saxon.strength
        result = viking.receiveDamage(damage)
        
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self): #summary of the war (who's the winner? if there is)
        soldiers_viking = len(self.vikingArmy)
        soldiers_saxon = len(self.saxonArmy)
        
        if soldiers_viking == 0:
            return 'Saxons have fought for their lives and survive another day...'
        elif soldiers_saxon == 0:
            return 'Vikings have won the war of the century!'
        elif soldiers_viking or soldiers_saxon >= 1:
            return 'Vikings and Saxons are still in the thick of battle.'
    pass


"""
#yop
class War2:

    def __init__(self):
        # your code here

    def addViking(self, Viking):
        # your code here
    
    def addSaxon(self, Saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here

    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here

    pass

"""
