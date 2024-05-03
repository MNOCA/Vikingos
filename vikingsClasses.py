import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        # returns the strength property of the Soldier
        return self.strength


    def receiveDamage(self, damage):
        # health = health - damage
        self.health -= damage
        # doesnt return anything
    

# Viking

class Viking(Soldier):

    # inherit from soldier
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)


    def battleCry(self):
        return "Odin Owns You All!"

    # inherits attack function and 
    # should return the strength property of the Viking
   
    def receiveDamage(self, damage):
        # health = health - damage
        self.health -= damage

        # if the Viking is still alive, it should return "NAME has received DAMAGE points of damage"
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            # if the Viking dies, it should return "NAME has died in act of combat"
            return f"{self.name} has died in act of combat"
        

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # no name
        # inherits from Soldier class
        super().__init__(health, strength)

    # attack method inherits from soldier, 0 args, 
    # return strenght property of saxon

    def receiveDamage(self, damage):
        # health = health - damage
        self.health -= damage
        # if the Saxon is still alive, it should return "A Saxon has received DAMAGE points of damage"
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            # if the Saxon dies, it should return "A Saxon has died in combat"
            return f"A Saxon has died in combat"
        

# Davicente

class War():
    def __init__(self):
        # assign an empty list to the vikingArmy property
        self.vikingArmy = []
        # assign an empty list to the saxonArmy property
        self.saxonArmy = []

    def addViking(self, viking):
        # receives 1 viking object
        # adds viking to the army
        self.vikingArmy.append(viking)
        # doesnt return
    
    def addSaxon(self, saxon):
        # same as add viking but for saxon objects
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # should make a Saxon receiveDamage() equal to the strength of a Viking
        result = random.choice(self.saxonArmy).receiveDamage(random.choice(self.vikingArmy).strength)   
        # should remove dead saxons from the army
        for saxon in self.saxonArmy:
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)

        # returns result of calling receiveDamage() of a Saxon with the strength of a Viking
        return result
    
    def saxonAttack(self):
        # same for viking taking damage
                # should make a viking receiveDamage() equal to the strength of a saxon
        result2 = random.choice(self.vikingArmy).receiveDamage(random.choice(self.saxonArmy).strength)   
        # should remove dead vikings from the army
        for viking in self.vikingArmy:
            if viking.health <= 0:
                self.vikingArmy.remove(viking)

        # returns result of calling receiveDamage() of a viking with the strength of a saxon
        return result2

    def showStatus(self):
        # if the Saxon array is empty
        if not self.saxonArmy:
            # should return "Vikings have won the war of the century!"
            return "Vikings have won the war of the century!"
        
        # if the Viking array is empty
        if not self.vikingArmy:
            # should return "Saxons have fought for their lives and survive another day..."
            return "Saxons have fought for their lives and survive another day..."
        
        # if there are at least 1 Viking and 1 Saxon
        if self.saxonArmy and self.vikingArmy:
            # should return "Vikings and Saxons are still in the thick of battle."
            return "Vikings and Saxons are still in the thick of battle."

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


