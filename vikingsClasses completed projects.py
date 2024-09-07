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
        self.name = name 
        super().__init__(health, strength) 


    def battleCry(self):
        # your code here
        return "Odin Owns You All"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
    
        if self.health > 0: 
            return f"{self.name} has received {damage} points of damage" 
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super()._init_(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else: 
            return " A saxon has died in combat"

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
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        damage = random_viking.attack()
        result = random_saxon.receiveDamage(damage)
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return result
    
    def saxonAttack(self):
        # your code here
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        damage = random_saxon.attack()
        result = random_viking.receiveDamage(damage)
        if random_viking.health <= 0:
            self.saxonArmy.remove(random_viking)
        return result

    def showStatus(self):
        # your code here
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of the battle"
        elif self.saxonArmy == [] :
            return " Vikings have won the war of the century!"
        elif self.vikingArmy == [] : 
            return " Saxons have  fought for their lives and survive another day . . ."

#yop
