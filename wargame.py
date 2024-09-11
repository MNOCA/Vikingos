
from vikingsClasses import Soldier, Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]

war_instance = War()

#Create 5 Vikings
for i in range(0,5):
    if i:
        war_instance.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

#Create 5 Saxons
for i in range(0,5):
    if i:
        war_instance.addSaxon(Saxon(100,random.randint(0,100)))
    
round = 0
while war_instance.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    war_instance.vikingAttack()
    war_instance.saxonAttack()
    print(f"round: {round} // Viking army: {len(war_instance.vikingArmy)} warriors",f"and Saxon army: {len(war_instance.saxonArmy)} warriors")
    print(war_instance.showStatus())
    round += 1