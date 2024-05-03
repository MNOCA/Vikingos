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
        super().__init__(health, strength)
        self.name = name
        
    def battleCry(self):
        return "Odin Owns You ALL!"

    def receiveDamage(self, damage):
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
# Davicente

class War():
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
        
    def addViking(self, viking):
        self.viking_army.append(viking)
    
    def addSaxon(self, saxon):
        self.saxon_army.append(saxon)
    
    def vikingAttack(self):
        viking = random.choice(self.viking_army)
        saxon = random.choice(self.saxon_army)
        damage = viking.attack()
        result = saxon.receiveDamage(damage)
        if saxon.health <= 0:
            self.saxon_army.remove(saxon)
        return result
    
    def saxonAttack(self):
        if not self.saxon_army:
            return "Vikings have won the war of the century!"
        elif not self.viking_army:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    def showStatus(self):
        if len(self.saxon_army) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.viking_army) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass
