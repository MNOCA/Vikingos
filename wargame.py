
from vikingsClasses import Soldier, Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
mywar = War()

#Create 5 Vikings
for i in range(0,5):
    if i:
        mywar.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

#Create 5 Saxons
for i in range(0,5):
    if i:
        mywar.addSaxon(Saxon(100,random.randint(0,100)))
    
round = 0
while mywar.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    mywar.vikingAttack()
    if mywar.saxonArmy != []:
        mywar.saxonAttack()
    print(f"round: {round} // Viking army: {len(mywar.vikingArmy)} warriors",f"and Saxon army: {len(mywar.saxonArmy)} warriors")
    print(mywar.showStatus())
    round += 1