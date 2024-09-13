import random

# Soldier


class Soldier:
    # Arguments:
    def __init__(self, health: int, strength: int):
        """
        Class soldier is initialized! Every soldier will have a set health and strength
        arg1: Class int. Health
        arg2: Class int. Strength
        """
        if health <= 0 or strength <= 0: # Make sure the user provides positive values for health and strength
            assert ValueError
            return "Health & Strength levels must be greater than 0"
        else:
            self.health = health
            self.strength = strength


    # Methods:
    def attack(self):
        """Defines an attack method to perform an attack and imply some damage to enemies"""

        return self.strength # this amount will be the damage received by the victim
        
    def receiveDamage(self, damage):
        """
        Defines a method for the soldier to recieve damage and substract it from the health
        arg1: int. Damage
        """

        self.health -= damage # substract the amount of damage to the Soldier's health
        
        
    
    


# Viking

class Viking(Soldier):
    
    # Arguments:
    def __init__(self, name, health: int, strength: int):
        """
        Viking soldier is defined here
        arg1: Name
        arg2: int. Health
        arg3: int. Strength
        """
        self.name = name
        self.health = health
        self.strength = strength
        self.shield = 0

        self.battleCry == True # Special ability for Vikings (health +50)
        self.shieldWall == True # Can activate the special ability (shield +50)

        self.berserkerRage == False # special ability for Vikings (strength x2)


    def receiveDamage(self, damage):
        """
        Defines a method for the soldier to recieve damage and substract it from the health
        It inherints the method recieve_damage() from the Soldier Class
        arg1: int. Damage
        """
        self.health -= (damage - self.shield) # substract the amount of the result (damage - shield)
        if self.health > 0:
            return self.name + f" has received {damage} points of damage"
        elif self.health <= 0:
            return self.name + " has died in act of combat"       
        
    def battleCry(self):
        """
        Effect: When a Viking activates his Battlecry, his health increases 50 points. ONCE
        """

        if self.battleCry == True:
            
            health_recovery = 50 # Battle Cry restores vikings health +50 points
            self.health += health_recovery
            self.battleCry = False
            return f"For Valhalla! Health +{health_recovery} points. Health: {self.health}"
        else:
            return f"{self.name} can't use Battlecry"

    def berserkerRage(self):
        """
        Effect: when health drops bellow 30 points. Vikings enter a state of rage, 
        where their strength doubles for one turn.
        """

        self.strength *= 2 # Strength doubles
        return f"{self.name} has enter Berserker Rage Mode"
    
    def shieldWall(self):
        """
        Effect: when 50% of vikings have died, Shield Wall is activated
        and viking's protective shield increases to 50 points (damage =  damage - 50)
        """
        self.shield += 50


# Saxon

class Saxon(Soldier):

    # Arguments:
    def __init__(self, health, strength):
        """
        Saxon soldier is defined here
        arg1: int. Health
        arg2: int. Strength
        """

        self.health = health
        self.strength = strength

    # Methods:
    def receiveDamage(self, damage):

        self.health -= damage # substract the amount of damage to the Saxon's health and check if it's more than 0
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health <= 0:
            return "A Saxon has died in combat"    
    
    def arrowBarrage(self):
        """
        Effect: Saxons can unleash a rain of arrows hitting multiple enemies at once. activates only once.
        """
        barrage_damage = 50 # standard damage to all enemies 
        return barrage_damage
        


# Davicente

class War():
    def __init__(self):
        """
        Define the War settings and builds the two armies:
        We defined the 2 properties as empty arrays:
        arr1: Vikings Army
        arr2: Saxons Army
        """
        
        self.vikingArmy = [] # Define Viking's Army. Empty until addViking() or if all Viking's die
        self.saxonArmy = []

    def addViking(self, viking):
        """
        Creates a viking class soldier and add it to the Vikings Army
        arg: class. viking
        """
        self.vikingArmy.append(viking) # adds Viking to the viking's Army
    
    def addSaxon(self, saxon):
        """
        Creates a Saxon class soldier and add it to the Saxon Army
        arg: class. saxon
        """
        self.saxonArmy.append(saxon) # adds Saxon to the Saxon's Army

    def vikingAttack(self):
        """
        Initializes attack() method from a random Viking to a random Saxon
        appying damage equal to the Viking's strength
        """

        viking = random.choice(self.vikingArmy) # select random viking that will attack
        damage = viking.strength # store the viking's strength in damage to substract it from the saxon's health
        saxon = random.choice(self.saxonArmy) # select random saxon to be attacked

        if viking.berserkerRage == True: # check if viking has entered special ability Berserker Rage Mode (strength x2)
            viking.berserkerRage() # Activate special ability 
            viking.berserkerRage == False # Deactivates special ability
        else:
            pass
        attack_result = saxon.receiveDamage(damage) # Saxon received damaged and health is depleted an amount of "damage"
        
        if saxon.health <= 0: # Check if the Saxon is still alive (health > 0)
            self.saxonArmy.remove(saxon) # Saxon dies and is removed from the army
            return attack_result
        else:
            return attack_result
        
    
    def saxonAttack(self):
        """
        Initializes attack() method from a random Saxon to a random Viking
        appying damage equal to the Saxon's strength
        """        

        saxon = random.choice(self.saxonArmy) # select random Saxon that will attack

        # Chance to activate Arrow Barrage before the atacck
        chance_arrowBarrage = random.randint(0,5)
        if chance_arrowBarrage == 0:
            saxon.arrowBarrage() # return {damage = 50}
            for viking in self.vikingArmy:
                viking.health -= 50

        else:
            damage = saxon.strength # store the saxon's strength in damage to substract it from the vikings's health
            viking = random.choice(self.vikingArmy) # select random viking to be attacked

            # chance to activate Battlecry before the attack
            if viking.battleCry == True: # Checks ability to activate special ability Battlecry
                chance = random.choice(1,2) # 50% chance to Activate special ability Battlecry
                if chance == 1:
                    return viking.battleCry() # viking's health restored +50 points
                else:
                    pass
            else:
                pass

            attack_result = viking.receiveDamage(damage) # Viking received damaged and health is depleted an amount of "damage"

            if viking.health <= 0: # Check if the Viking is still alive (health > 0)
                self.vikingArmy.remove(viking) # Viking dies and is removed from the army

            else:
                if viking.health <= 30: 
                    viking.berserkerRage == True # viking has entered Berserker Rage Mode
                    return attack_result
                else:
                    return attack_result

    def showStatus(self):
        """
        Returns the current status of the `War` based on the size of the armies.
        **if the `Saxon` array is empty**, should return _**"Vikings have won the war of the century!"**_
        **if the `Viking` array is empty**, should return _**"Saxons have fought for their lives and survive another day..."**_
        **if there are at least 1 `Viking` and 1 `Saxon`**, should return _**"Vikings and Saxons are still in the thick of battle."**_
        """

        if len(self.saxonArmy) == 0: # Vikings WIN
            return "Vikings have won the war of the century!"
        
        elif len(self.vikingArmy) == 0: # Saxon WIN
            return "Saxons have fought for their lives and survive another day..."
        
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0: # BATTLE STILL ON
            if len(self.vikingArmy) < 3:
                for viking in self.vikingArmy:
                    if viking.shieldWall == True:
                        viking.shieldWall()
                        print(f"{viking.name} has activated shield Wall")
                        viking.shieldWall == False
                    else:
                        pass
            else:
                pass
            return "Vikings and Saxons are still in the thick of battle."