
from .vikingsClasses import Soldier, Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]


#Create 5 Vikings
for i in range(0,5):
    if i:
        War.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

#Create 5 Saxons
for i in range(0,5):
    if i:
        War.addSaxon(Saxon(100,random.randint(0,100)))
    
round = 0
while War.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    War.vikingAttack()
    War.saxonAttack()
    print(f"round: {round} // Viking army: {len(War.vikingArmy)} warriors",f"and Saxon army: {len(War.saxonArmy)} warriors")
    print(War.showStatus())
    round += 1