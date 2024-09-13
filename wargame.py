from vikingsClasses import Soldier, Viking, Saxon, War
import random

soldier_names = ["albert", "andres", "archie", "dani", "david", "gerard", "german", "graham", "imanol", "laura"]

# Create an instance of the War class
war = War()

# Create 5 Vikings
for i in range(5):
    viking_name = soldier_names[random.randint(0, 9)]  # Pick a random name
    viking_strength = random.randint(0, 100)
    viking_health = random.randint(0, 100)
    viking = Viking(viking_name, viking_strength, viking_health)  # Create a Viking instance
    war.addViking(viking)  # Pass the Viking instance to the War class

# Create 5 Saxons
for i in range(5):
    saxon = Saxon(100, random.randint(0, 100))  # Create a Saxon instance
    war.addSaxon(saxon)  # Pass the Saxon instance to the War class

round = 0
while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    war.vikingAttack()
    war.saxonAttack()
    print(f"Round: {round} // Viking army: {len(war.vikingArmy)} warriors and Saxon army: {len(war.saxonArmy)} warriors")
    print(war.showStatus())
    round += 1
