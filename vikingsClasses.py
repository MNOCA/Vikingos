import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health 
        self.strength = strength 
    
    def attack(self):
        # it should return strenght
        return self.strength 
        

    def receiveDamage(self, damage):
        ## Calculates the damage to the character (damage -health)
        self.health -= damage

    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        self.name = name
        super().__init__(health, strength)
    def attack(self):
        # it should return strenght
        return self.strength         
    def battleCry(self):
        # your code here
        return f"Odin Owns You All!"
    def receiveDamage(self, damage):
        # your code here
        self.health -= damage   
        if self.health > 0 :
            return f"{self.name} has received {damage} points of damage"
        else :
            return f"{self.name} has died in act of combat"
             

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
       # your code here
       super().__init__(health, strength)
    
    def attack(self):
       #Should 
       return self.strength 
    
    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0 :
            return f"A Saxon has received {damage} points of damage"
        else :
            return f'A Saxon has died in combat'
    

# Davicente

class War():
    def __init__(self):
       # your code here
       self.vikingArmy = []
       self.saxonArmy = []
       
    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self) :
        # your code here
        viking= random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        viking_damage = viking.attack()
        result = saxon.receiveDamage(viking_damage)

        if saxon.health <= 0 :
            self.saxonArmy.remove(saxon)
            #return result
            #return f"A Saxon has died in combat"
        return result
    

    def saxonAttack(self):
        # your code here
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        saxon_damage = saxon.attack()
        result = viking.receiveDamage(saxon_damage)

        if viking.health <= 0:
            self.vikingArmy.remove(viking)
            return result
        else :
            return result
        
    def showStatus(self):
        # your code here
        if len(self.saxonArmy) <= 0:
            return f"Vikings have won the war of the century!" 
        elif len(self.vikingArmy) <= 0:
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == len(self.vikingArmy):
            return f"Vikings and Saxons are still in the thick of battle."
        else :
            return f"Something is wrong"
    #pass"""

#yop
#class War2:

 #   def __init__(self):
        # your code here

  #  def addViking(self, Viking):
        # your code here
    
   # def addSaxon(self, Saxon):
        # your code here
    
   # def vikingAttack(self):
        # your code here

   # def saxonAttack(self):
        # your code here

   # def showStatus(self):
        # your code here

    #pass


