import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength

    def attack(self) -> int:
        return self.strength

    def receiveDamage(self, damage: int):
        # your code here
        self.health -= abs(damage)


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health=health, strength=strength)
        self.name = name

    def battleCry(self) -> str:
        return "Odin Owns You All!"

    def receiveDamage(self, damage) -> str:
        self.health -= abs(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health=health, strength=strength)

    def receiveDamage(self, damage) -> str:
        self.health -= abs(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


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

    def vikingAttack(self) -> str:
        # your code here
        attackingViking: Viking = random.choice(self.vikingArmy)
        defendingSaxon: Saxon = random.choice(self.saxonArmy)
        fight_result = defendingSaxon.receiveDamage(attackingViking.strength)
        if "died" in fight_result:
            self.saxonArmy.remove(defendingSaxon)
        return fight_result

    def saxonAttack(self) -> str:
        # your code here
        attackingSaxon: Saxon = random.choice(self.saxonArmy)
        defendingViking: Viking = random.choice(self.vikingArmy)
        fight_result = defendingViking.receiveDamage(attackingSaxon.strength)
        if "died" in fight_result:
            self.vikingArmy.remove(defendingViking)
        return fight_result

    def showStatus(self) -> str:
        # your code here
        m = ""
        if len(self.saxonArmy) == 0:
            m = "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            m = "Saxons have fought for their lives and survive another day..."
        else:
            m = "Vikings and Saxons are still in the thick of battle."
        return m
