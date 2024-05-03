import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        #receive 2 arguments
        self.health = health
        self.strength = strength
    
    def attack(self):
        #Atack method;return the strength of the soldier
        return self.strength

    def receiveDamage(self, damage):
        # the method receive 1 argument (damage)
        #remove the received damage from the soldier's health
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # Viking is an inheritance from soldier
        self.name = name  # receivid as an input
        super().__init__(health, strength)  ## received as a soldier
        

    def battleCry(self):
        # receive 0 arguments
        return "Odin Owns You All!"

    ##Inherit attack method return strength propierty

    def receiveDamage(self, damage):
        ## receive 1 argument as the damage
        ## remove the received damage from the health
        self.health -= damage
        if self.health > 0:   # if the viking is still alive
            return f"{self.name} has received {damage} points of damage"
        else:    # if the vikings dies :(
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # curios thing: saxons has no name, nobody cares about they
        # receive 2 arguments inheric from soldier class
        super().__init__(health, strength)
    
    ## should return the strength property of the Saxon

    def receiveDamage(self, damage):
        # receive the argument as a damage
        # remove the received damage from the health
        self.health -= damage
        if self.health > 0:  ## if the saxon is still alive 
            return f"A Saxon has received {damage} points of damage"
        else:   # if the saxon dies
            return f"A Saxon has died in combat"




class War():
    def __init__(self):
        # receive 0 arguments
        # empty array to the vikingArmy property
        # an empty array to the saxonArmy property
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, viking):
        # recive the argument; viking object
        ## + viking to the viking army
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # recive saxon and add to the saxon army
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        ## random saxon from the army
        # Saxon receiveDamage() equal to the strength of a Viking
        result = random.choice(self.saxonArmy).receiveDamage(random.choice(self.vikingArmy).strength)
                ####   random saxon.receiveDamage(randomviking with his strength)
    
        for saxon in self.saxonArmy: # iterate over the saxon army
            if saxon.health <= 0:    ## remove dead saxons of the army
                self.saxonArmy.remove(saxon)
        
        return result  ## return result of calling receiveDamage() of a Saxon with the strength of a Viking
        
    
    def saxonAttack(self):
        ## A Viking receives the damage equal to the strength of a Saxon
        result2 = random.choice(self.vikingArmy).receiveDamage(random.choice(self.saxonArmy).strength)
       
        ## should return result of calling receiveDamage() of a Saxon with the strength of a Viking
        for viking in self.vikingArmy:
            if viking.health <= 0:
                self.vikingArmy.remove(viking)    ## remove dead saxons of the army
        
        return result2

    def showStatus(self):
        ## Returns the current status of the War based on the size of the armies.
        ## 0 arguments
        #if the Saxon array is empty, should return "Vikings have won the war of the century!"
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        # if the Viking array is empty, should return "Saxons have fought for their lives and survive another day..."
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        
        # if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are still in the thick of battle."
        
        if self.saxonArmy and self.vikingArmy:  # if theres an element (True)
            return "Vikings and Saxons are still in the thick of battle."
        

    
    #pass

#yop
class War2:

    def __init__(self):
        pass
        # your code here

    def addViking(self, Viking):
        pass
        # your code here
    
    def addSaxon(self, Saxon):
        pass
        # your code here
    
    def vikingAttack(self):
        pass
        # your code here

    def saxonAttack(self):
        pass
        # your code here

    def showStatus(self):
        pass
        # your code here

    pass


