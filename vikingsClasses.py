import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        
        result = random_saxon.receiveDamage(random_viking.attack())

        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
            print(f"VIKING | I am deleting random_saxon, Health:{random_saxon.health}, Strength: {random_saxon.strength}")

        return result
        
    
    def saxonAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        
        result = random_viking.receiveDamage(random_saxon.attack())

        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
            print(f"SAXON | I am deleting viking {random_viking.name}, Health:{random_viking.health}, Strength: {random_viking.strength}")
            
        return result

    def showStatus(self):
        if len(self.saxonArmy) < 1:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) < 1:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    pass
