import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    # Method for soldier attach
    def attack(self):
        return self.strength
        
    # Method for soldier receiving damage:
    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    # Method for battle cry
    def battleCry(self):
        return "Odin Owns You All!"

    # Method for viking receiving damage. Prints i) damage if alive ii) dead of viking
    def receiveDamage(self, damage):
        if damage < self.health:
            self.health -= damage
            return f"{self.name} has received {damage} points of damage"
        else:
            self.health -= damage
            return f"{self.name} has died in act of combat"

     # Method for Viking attack
    def attack(self):
        # Call the function attack from Mother Class Soldier
        return super().attack()

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    # Method for Saxon receiving damage. Prints i) damage if alive ii) dead of Saxon
    def receiveDamage(self, damage):
        if damage < self.health:
            self.health -= damage
            return f"A Saxon has received {damage} points of damage"
        else:
            self.health -= damage
            return f"A Saxon has died in combat"
    
    # Method for Saxon attack
    def attack(self):
        # Call the function attack from Mother Class Soldier
        return super().attack()
        

# War

class War():
    # Initiates the War with an empty Viking Army and empty Saxon Army
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    # Method to add 1 Viking to the vikingArmy
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    # Method to add 1 Saxon to the saxonArmy
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        # Choosing a random Saxon from saxonArmy
        random_saxon = random.choice(self.saxonArmy)
        
        # Choosing a random Viking from vikingArmy
        random_viking = random.choice(self.vikingArmy)

        # Random Saxon receiving damage = random Viking strength
        random_saxon_health=random_saxon.receiveDamage(random_viking.strength)

        # Remove saxon from list if health=0
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)

        # Retorna o resultado de receiveDamage() of a Saxon with the strength of a Viking
        return random_saxon_health
    
    def saxonAttack(self):
        # Choosing a random Saxon from saxonArmy
        random_saxon = random.choice(self.saxonArmy)
        
        # Choosing a random Viking from vikingArmy
        random_viking = random.choice(self.vikingArmy)

        # Random Viking receiving damage = random Saxon strength
        random_viking_health=random_viking.receiveDamage(random_saxon.strength)

        # Remove viking from list if health=0
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)

        # Retorna o resultado de receiveDamage() of a Saxon with the strength of a Viking
        return random_viking_health

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

