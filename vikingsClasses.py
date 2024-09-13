import random


# Soldier

class Soldier:
    def __init__(self, health, strength):
        """The parent class Soldier must have 2 attributes in its constructor"""
        self.health = health # Amount of health the soldier has
        self.strength = strength # How much can the sodier damage it's opponent
    
    def attack(self):
        """This method relates soldier's strength value to his attack: his attack value will be the same as the strength value introduced first"""
        return self.strength

    def receiveDamage(self, damage):
        """This method substract damage from health, so it returns how much health has the soldier lost after being attackted by an opponent"""
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength) #Inherit Viking class to attach it to the parent class
        self.name = name # Adds a specific name for a viking
        """
        Viking is a child class of Soldier, so has the same attributes as above
        but with new features like the battle cry and a particular message
        that shows when he's damaged
        """

    def battleCry(self):
        return "Odin Owns You All!" # It's what vikings shout when going to the battle

    def receiveDamage(self, damage):
        """When a viking is damaged, first reduce health, then check if he's still alive, and then print the corresponding message"""
        self.health -= damage # Substracts damage value from health
        if self.health > 0: # If alive
            return f"{self.name} has received {damage} points of damage"
        else: # If dead
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
            return f"A Saxon has died in combat"
            

# Davicente

class War():
    """
    This Class have two methods that add soldiers to both armies
    and two methods that returns the damage of a soldier after being attacked.
    Also a final method that displays if any of the armies are defeated or if
    the battle is still on course
    """
    def __init__(self):
        self.vikingArmy = [] # Empty list to add and substract soldiers
        self.saxonArmy = [] # Same

    def addViking(self, viking):
        self.vikingArmy.append(viking) # Add a viking to its army
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon) # Add a saxon to its army
    
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy) # Pick a random viking from the army
        saxon = random.choice(self.saxonArmy) # Pick a random saxon from the army
        damage = viking.attack() # Relates viking strength (attack power) to the damage he cause
        result = saxon.receiveDamage(damage) # Apply the damage to the random saxon
        for saxon in self.saxonArmy: 
            if saxon.health <= 0: # Checks if the saxon has no health left...
                self.saxonArmy.remove(saxon) # ...and if so, then remove the dead saxon from the army 
        return result
    
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damage = saxon.attack()
        result = viking.receiveDamage(damage)
        for viking in self.vikingArmy:
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
        return result


    def showStatus(self):
        if self.saxonArmy == []: # Checks if the saxon army is an empty list, and if so that means there's no soldiers left
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else: # If both lists have elements (soldiers) means that the battle is still on course
            return "Vikings and Saxons are still in the thick of battle."
    pass
