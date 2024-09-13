import random

# Soldier

# Initializing the Soldier class
class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength   
    
    # Defining the method 'attack'
    def attack(self):
        return self.strength

    # Defining the method 'receiveDamage'
    def receiveDamage(self, damage):
            
        # Damage is substracted from the soldier's health
        self.health -= damage
        return None

        

# Viking

    # Initializing the Viking class
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    # Defining the 'battleCry'-method
    def battleCry(self):
        return "Odin Owns You All!" 

    # Defining the 'receiveDamage'-method for vikings
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        


# Saxon

# Initializing the class Saxon inheriting from the Soldier class
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    # Defining the method 'receive damage'
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# Davicente

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
        
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        if self.saxonArmy and self.vikingArmy:
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)
            damage = viking.attack()
            result = saxon.receiveDamage(damage)
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
            return result

    def saxonAttack(self):
        if self.vikingArmy and self.saxonArmy:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            damage = saxon.attack()
            result = viking.receiveDamage(damage)
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
            return result
        
    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
        pass

# Vikings
viking1 = Viking("Hallvardr", 300, 130)
viking2 = Viking("Fenrir", 300, 155)
viking3 = Viking("Ivar", 300, 160)
viking4 = Viking("Erik", 300, 170)
viking5 = Viking("Gunnar", 300, 125)

# Saxons
saxon1 = Saxon(50, 25)
saxon2 = Saxon(50, 23)
saxon3 = Saxon(50, 28)
saxon4 = Saxon(50, 24)
saxon5 = Saxon(50, 26)

# New war
war = War()

# Adding the vikings
war.addViking(viking1)
war.addViking(viking2)
war.addViking(viking3)
war.addViking(viking4)
war.addViking(viking5)

# Adding the saxons
war.addSaxon(saxon1)
war.addSaxon(saxon2)
war.addSaxon(saxon3)
war.addSaxon(saxon4)
war.addSaxon(saxon5)

# Trying the methods
print(war.vikingAttack())
print(war.saxonAttack())
print(war.showStatus())