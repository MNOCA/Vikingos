import random

# SOLDIER ------------------------------------------------------------------------------------------


class Soldier:
    """
    Parent class Viking and Saxon inherit from
    """

    def __init__(self, health: int, strength: int) -> None:
        """Constructor

        Args:
            health (int): health points (soldier is dead if 0 or below)
            strength (int): dammage points caused to opponent during an attack
        """
        self.health = health
        self.strength = strength

    def attack(self) -> int:
        """ Getter for the health points

        Returns:
            int: return strength points
        """
        return self.strength

    def receiveDamage(self, damage: int) -> None:
        """Substract damage points to soldier's health

        Args:
            damage (int): points to substract
        """
        self.health -= damage


# VIKING -------------------------------------------------------------------------------------------


class Viking(Soldier):
    """
    Child class of Soldier
    """

    def __init__(self, name: str, health: int, strength: int) -> None:
        """Constructor

        Args:
            name (str): viking name
            health (int): viking health points (viking is dead if 0 or below)
            strength (int): viking strength points
        """
        super().__init__(health, strength)  # initialise parent class
        self.name = name

    def battleCry(self) -> str:
        """Yells a battle cry

        Returns:
            str: battle cry text
        """
        return "Odin Owns You All!"

    def receiveDamage(self, damage: int) -> str:
        """Applies damage to the viking's health

        Args:
            damage (int): points to substract

        Returns:
            str: result of the attack
        """
        super().receiveDamage(damage)

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"

        return f"{self.name} has died in act of combat"


# SAXON --------------------------------------------------------------------------------------------


class Saxon(Soldier):
    """
    Child class of Soldier
    """

    def __init__(self, health: int, strength: int) -> None:
        """Constructor

        Args:
            health (int): health points (saxon is dead if 0 or below)
            strength (int): dammage points caused to opponent during an attack
        """
        super().__init__(health, strength)  # initialise parent class

    def receiveDamage(self, damage: int) -> str:
        """Apply damage to the saxon's health

        Args:
            damage (int): points to substract

        Returns:
            str: result of the attack
        """

        super().receiveDamage(damage)

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"

        return "A Saxon has died in combat"


# WAR ----------------------------------------------------------------------------------------------


class War():
    """
    Class to manage the war between vikings and saxons
    """

    def __init__(self) -> None:
        """Constructor"""
        self.vikingArmy = []
        self.saxonArmy = []

    def __repr__(self) -> str:
        """String representation of the current state of both armies to print

        Returns:
            str: string representation
        """

        # vikings army
        string = f'\n{len(self.vikingArmy)} VIKINGS:\n'
        for viking in self.vikingArmy:
            string += f"{viking.name}, {viking.health}, {viking.strength}\n"

        # saxons army
        string += f"{len(self.saxonArmy)} SAXONS\n"
        for saxon in self.saxonArmy:
            string += f"{saxon.health}, {saxon.strength}\n"

        return string

    def addViking(self, viking: Viking) -> None:
        """Add a viking to the viking army

        Args:
            viking (Viking): viking instance to add
        """
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon: Saxon) -> None:
        """Add a saxon to the saxon army

        Args:
            saxon (Saxon): saxon instance to add
        """
        self.saxonArmy.append(saxon)

    def vikingAttack(self) -> str:
        """Viking attacks a saxon

        Returns:
            str: result of the attack returned from receiveDamage method
        """

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

    def saxonAttack(self) -> str:
        """Saxon attacks a viking

        Returns:
            str: result of the attack returned from receiveDamage method
        """

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

    def showStatus(self) -> str:
        """Show the current status of the war

        Returns:
            str: string result of the war
        """

        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"

        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."

        return "Vikings and Saxons are still in the thick of battle."


# COMMENTING THIS PART? NOT NEEDED? ----------------------------------------------------------------
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


# INSTANCIATION TESTS ------------------------------------------------------------------------------
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
