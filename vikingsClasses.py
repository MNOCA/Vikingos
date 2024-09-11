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
        super().__init__(health, strength)

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        super().receiveDamage(damage)

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    # TODO Add Random soldier picker method?

    def vikingAttack(self):
        saxon_soldier = random.choice(self.saxonArmy)
        viking_soldier = random.choice(self.vikingArmy)
        
        result = saxon_soldier.receiveDamage(viking_soldier.attack())
        
        if saxon_soldier.health <= 0:
            self.saxonArmy.remove(saxon_soldier)

        return result
    
    def saxonAttack(self):
        saxon_soldier = random.choice(self.saxonArmy)
        viking_soldier = random.choice(self.vikingArmy)

        result = viking_soldier.receiveDamage(saxon_soldier.attack())
        
        if viking_soldier.health <= 0:
            self.vikingArmy.remove(viking_soldier)
        
        return result

    def showStatus(self):
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
        elif len(self.saxonArmy) <= 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) <= 0:
            return "Saxons have fought for their lives and survive another day..."