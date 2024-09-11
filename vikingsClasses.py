import random

# Soldier


class Soldier():
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
    
    def attack(self):
        # your code here
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
    

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
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"a Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = list()
        self.saxonArmy = list()

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking) 
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        Saxon_f = random.choice(self.saxonArmy)
        Viking_f = random.choice(self.vikingArmy)
        result = Saxon_f.receiveDamage(Viking_f.strength)
        if Saxon_f.health <=0:
            self.saxonArmy.remove(Saxon_f)
        return result
    
    def saxonAttack(self):
        # your code here
        Saxon_f = random.choice(self.saxonArmy)
        Viking_f = random.choice(self.vikingArmy)
        result = Viking_f.receiveDamage(Saxon_f.strength)
        if Viking_f.health <=0:
            self.vikingArmy.remove(Viking_f)
        return result
    
    def showStatus(self):
        # your code here
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."


            

#yop

class War2:

    def __init__(self):
        # your code here
        pass

    def addViking(self, Viking):
        # your code here
        pass
    
    def addSaxon(self, Saxon):
        # your code here
        pass
    def vikingAttack(self):
        # your code here
        pass
    def saxonAttack(self):
        # your code here
        pass
    def showStatus(self):
        # your code here
        pass
    pass