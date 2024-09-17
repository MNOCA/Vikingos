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
        return

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        self.name = name
        self.health = health
        self.strength = strength

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

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
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War
class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        if type(viking) == Viking:
            self.vikingArmy.append(viking)
        else:
            print(f"{viking} is not a Viking!")
            return
    
    def addSaxon(self, saxon):
        # your code here
        if type(saxon) == Saxon:
            self.saxonArmy.append(saxon)
        else:
            print(f"{saxon} is not a Saxon!")
            return
        
    def vikingAttack(self):
        # your code here
        attacker = random.choice(self.vikingArmy)
        victim = random.choice(self.saxonArmy)

        result = victim.receiveDamage(attacker.strength)
        for saxon in self.saxonArmy:
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
            else:
                continue
        return result
    
    def saxonAttack(self):
        # your code here
        attacker = random.choice(self.saxonArmy)
        victim = random.choice(self.vikingArmy)

        result = victim.receiveDamage(attacker.strength)
        for viking in self.vikingArmy:
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
            else:
                continue
        return result

    def showStatus(self):
        # your code here
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        
