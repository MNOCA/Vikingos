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
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"

        return f"{self.name} has died in act of combat"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"

        return "A Saxon has died in combat"



# Davicente

class War():

    def __init__(self):

        self.vikingArmy = []
        self.saxonArmy = []

    def __repr__(self):
        
        string = f'\n{len(self.vikingArmy)} VIKINGS:\n'
        for viking in self.vikingArmy:
            string += f"{viking.name}, {viking.health}, {viking.strength}\n"
        
        string += f"{len(self.saxonArmy)} SAXONS\n"
        for saxon in self.saxonArmy:
            string += f"{saxon.health}, {saxon.strength}\n"
        
        return string

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):

        if len(self.vikingArmy) <= 0 or len(self.saxonArmy) <= 0:
            return

        # pick a random viking and saxon
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        # apply damage
        attack_result = saxon.receiveDamage(viking.attack())

        # remove dead saxons from the list
        self.saxonArmy = [saxon for saxon in self.saxonArmy if saxon.health > 0]

        return attack_result

    def saxonAttack(self):

        if len(self.vikingArmy) <= 0 or len(self.saxonArmy) <= 0:
            return

        # pick a random viking and saxon
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        # apply damage
        attack_result = viking.receiveDamage(saxon.attack())

        # remove dead viking from the list
        self.vikingArmy = [viking for viking in self.vikingArmy if viking.health > 0]

        return attack_result

    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"

        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."

        return "Vikings and Saxons are still in the thick of battle."

#yop
# class War2:

#     def __init__(self):
#         # your code here

#     def addViking(self, Viking):
#         # your code here
    
#     def addSaxon(self, Saxon):
#         # your code here
    
#     def vikingAttack(self):
#         # your code here

#     def saxonAttack(self):
#         # your code here

#     def showStatus(self):
#         # your code here

#     pass


if __name__ == "__main__":

    def generateViking():
        return Viking("Harald", 300, 150)

    def generateSaxon():
        return Saxon(60, 25)

    viking = generateViking()
    saxon = generateSaxon()
    war = War()
    war.addViking(viking)
    war.addSaxon(saxon)

    print(war)
