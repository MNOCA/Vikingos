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
    

# Viking - this inherits from the soldier and has a name parameter,. Also has a battleCry() method and receiveDamage() method that provies custom input

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        pass

    def battleCry(self):
        # your code here
        pass

    def receiveDamage(self, damage):
        # your code here
        pass

# Saxon - inherits from the soldier , has no name parameter nut also a receiveDamage() methood that outpouts a custom message

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        pass

    def receiveDamage(self, damage):
        # your code here
        pass

# Davicente

class War():
    def __init__(self):
        # your code here
        pass

    def addViking(self, viking):
        # your code here
        pass
    
    def addSaxon(self, saxon):
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


