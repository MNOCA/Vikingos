
from vikingsClasses import Soldier, Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
current_war = War()

#Create 5 Vikings
for i in range(0,5):
    current_war.addViking(
        Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

#Create 5 Saxons
for i in range(0,5):
    current_war.addSaxon(Saxon(100,random.randint(0,100)))
    
round = 0
while current_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    print(current_war.vikingAttack())
    print(current_war.saxonAttack())
    print(f"round: {round} // Viking army: {len(current_war.vikingArmy)} warriors",f"and Saxon army: {len(current_war.saxonArmy)} warriors")
    print(current_war.showStatus())
    print("")
    round += 1