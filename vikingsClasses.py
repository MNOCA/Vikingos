import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        # Modify the Soldier constructor function and add 2 methods to its prototype: attack(), and receiveDamage()
        return self.strength

    def receiveDamage(self, damage):
        #health = health - damage
        self.health = self.health - damage
        #dont return anything
    

# Viking

class Viking(Soldier):

    #inherit from soldier
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def battleCry(self):
        #"Odin Owns You All!"
        return "Odin Owns You All!"
    
    #inherit attack function and return the strenght

    def receiveDamage(self, damage):
        # health = health - damage
        self.health = self.health - damage
        #if the Viking is still alive, it should return "NAME has received DAMAGE points of damage"
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        #if the Viking dies, it should return "NAME has died in act of combat"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):

    #Saxon should inherit from Soldier
    def __init__(self, health, strength):
        #inherit from soldiers class
        super().__init__(health, strength)

    #attack method inherited from soldier, 0 args, return the strength property of the Saxon

    def receiveDamage(self, damage):
        #not inherited
        # health = health - damage
        self.health = self.health - damage
        #if the Saxon is still alive, it should return "A Saxon has received DAMAGE points of damage"
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        #if the Saxon dies, it should return "A Saxon has died in combat"
        else:
            return "A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        #should assign an empty list to the vikingArmy property
        self.vikingArmy = []
        #should assign an empty list to the saxonArmy property
        self.saxonArmy = []

    def addViking(self, viking):
        #recieves one viking object

        #add vikings to the army
        self.vikingArmy.append(viking)
        #doesnt return
    
    def addSaxon(self, saxon):
        #same as viking but for saxon objects
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        #should make a Saxon receiveDamage() equal to the strength of a Viking
        result = random.choice(self.saxonArmy).receiveDamage(random.choice(self.vikingArmy).strength)
        #should remove dead saxons from the army
        for saxon in self.saxonArmy:
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)

        #should return result of calling receiveDamage() of a Saxon with the strength of a Viking
        return result
    
    def saxonAttack(self):
        #same for viking taking damage
        result2 = random.choice(self.vikingArmy).receiveDamage(random.choice(self.saxonArmy).strength)

        for viking in self.vikingArmy:
            if viking.health <= 0:
                self.vikingArmy.remove(viking)

        return result2

    def showStatus(self):
        #if the Saxon list is empty, should return "Vikings have won the war of the century!"
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        
        #if the Viking array is empty, should return "Saxons have fought for their lives and survive another day..."
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        
        #if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are still in the thick of battle."
        if self.saxonArmy and self.vikingArmy:
            return "Vikings and Saxons are still in the thick of battle."
    #pass

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

    #def showStatus(self):
        #if not self.saxonArmy:
            #return "Vikings have won the war of the century!"
        #else:
            #if not self.vikingArmy:
                #return "Saxons have fought for their lives and survive another day..."
            #else:
                #return "Vikings and Saxons are still in the thick of battle."