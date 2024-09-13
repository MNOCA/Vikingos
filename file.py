from greatWar import Soldier, Viking, Saxon, War
import random

soldier_names = ["Kerem","Carlos","Tiago","Dani", "Julia","Caroline","Joao","Saul","Dusan", "Jaime"]
great_war = War()

#Create 5 Vikings
for i in range(0,5):
    if i:
        great_war.addViking(Viking(soldier_names[random.randint(0,9)],300,random.randint(0,100)))

#Create 5 Saxons
for i in range(0,5):
    if i:
        great_war.addSaxon(Saxon(300,random.randint(0,100)))
    
round = 0
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    great_war.vikingAttack()
    
    if len(great_war.saxonArmy) != 0:
        great_war.saxonAttack()
    print(f"round: {round} // Viking army: {len(great_war.vikingArmy)} warriors",f"and Saxon army: {len(great_war.saxonArmy)} warriors")
    print(great_war.showStatus())
    round += 1