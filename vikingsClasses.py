import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"


    	
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)


    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health <= 0:
            return "A Saxon has died in combat"
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"



# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        # your code here
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
        
    def saxonAttack(self):
        # your code here
        if len(self.saxonArmy) > 0:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            result = viking.receiveDamage(saxon.strength)
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
            return result
        else:
            return "No Saxons left to attack"
        

    def showStatus(self):
        # your code here
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        

