import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health 
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name  

    # The receiveDamage method has different behavior for a Viking
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    # The battleCry method returns a Viking battle cry
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

# Saxon class (inherits from Soldier)
class Saxon(Soldier):
    def __init__(self, health, strength):
        # Call the parent constructor to set health and strength
        Soldier.__init__(self, health, strength)

    # The receiveDamage method has different behavior for a Saxon
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"



# Davicente

class War:
    def __init__(self):
        self.vikingArmy = []  # Initially, no Vikings
        self.saxonArmy = []   # Initially, no Saxons

    def addViking(self, viking):
        self.vikingArmy.append(viking)  # Add the Viking to the army

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)  # Add the Saxon to the army

    def vikingAttack(self):
        # Randomly choose a Viking and a Saxon
        import random
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        # Saxon receives damage equal to Viking's strength
        result = saxon.receiveDamage(viking.strength)

        # Remove dead Saxons
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)

        return result

    def saxonAttack(self):
        # Randomly choose a Viking and a Saxon
        import random
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        # Viking receives damage equal to Saxon's strength
        result = viking.receiveDamage(saxon.strength)

        # Remove dead Vikings
        if viking.health <= 0:
            self.vikingArmy.remove(viking)

        return result

    def showStatus(self):
        # Check if the Saxon army is empty
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        # Check if the Viking army is empty
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        # If both armies still have soldiers
        else:
            return "Vikings and Saxons are still in the thick of battle."


