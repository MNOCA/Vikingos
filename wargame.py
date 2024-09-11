
from vikingsClasses import Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]

# I need to create an instance of War, using War() directly results in an error
new_war = War()

#Create 5 Vikings
for i in range(0,5):
    if i:
        new_war.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

#Create 5 Saxons
for i in range(0,5):
    if i:
        new_war.addSaxon(Saxon(100,random.randint(0,100)))
    
round = 0
while new_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    new_war.vikingAttack()
    # we need to check if there are saxons left after the viking attack, or the round is over
    if len(new_war.saxonArmy):
        new_war.saxonAttack()
    print(f"round: {round} // Viking army: {len(new_war.vikingArmy)} warriors",f"and Saxon army: {len(new_war.saxonArmy)} warriors")
    print(new_war.showStatus())
    round += 1